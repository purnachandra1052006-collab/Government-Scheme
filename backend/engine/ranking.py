import math
from typing import List
from backend.models.schemas import SchemeMatch, Scheme, UserProfile

MAX_BENEFIT_SCALE = 10000000.0  # ₹1 Crore scaling factor


class RankingEngine:
    @staticmethod
    def calculate_scores(
        match_type: str,
        matched_criteria: List[str],
        failed_criteria: List[str],
        scheme: Scheme,
        user: UserProfile,
    ) -> tuple[float, float, float]:
        """
        Calculates match_score, financial_score, and total_rank_score.
        """
        # 1. Base Match Score
        if match_type == "direct":
            base_match = 85.0
            # Bonus for strong targeted demographic matches
            bonus = 0.0
            if user.caste and user.caste in ["SC", "ST", "OBC"] and len(scheme.caste_category) < 5:
                bonus += 5.0
            if user.gender == "Female" and "Female" in scheme.gender_preference:
                bonus += 5.0
            if user.occupation and user.occupation in scheme.target_audience and len(scheme.target_audience) <= 2:
                bonus += 5.0
            match_score = min(100.0, base_match + bonus)
        else:
            # Near miss gets between 50 and 70 based on soft failures
            penalty = len(failed_criteria) * 12.0
            match_score = max(40.0, 75.0 - penalty)

        # 2. Financial Benefit Score (Logarithmic scaling so ₹50L doesn't completely overwhelm ₹1L but ranks higher)
        fin_val = scheme.financial_benefit_value or 10000.0
        # Use log10 scale: log10(1,000) ~ 3, log10(100,000) = 5, log10(10,000,000) = 7
        min_log = math.log10(5000)
        max_log = math.log10(MAX_BENEFIT_SCALE)
        curr_log = math.log10(max(5000.0, fin_val))
        financial_score = min(100.0, max(10.0, ((curr_log - min_log) / (max_log - min_log)) * 100.0))

        # 3. Weighted Total Rank Score
        # Direct matches receive massive priority over near misses
        type_weight = 1000.0 if match_type == "direct" else 0.0
        total_rank_score = type_weight + (match_score * 0.6) + (financial_score * 0.4)

        return round(match_score, 1), round(financial_score, 1), round(total_rank_score, 1)

    @classmethod
    def rank_matches(cls, matches: List[SchemeMatch]) -> List[SchemeMatch]:
        """
        Sorts matches in descending order of total_rank_score.
        """
        return sorted(matches, key=lambda m: m.total_rank_score, reverse=True)
