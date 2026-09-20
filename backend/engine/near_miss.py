from typing import Optional, List, Tuple
from backend.models.schemas import UserProfile, Scheme, NearMissReasoning
from backend.engine.rule_engine import get_qualification_rank, QUALIFICATION_RANKS


class NearMissEvaluator:
    @staticmethod
    def evaluate_near_miss(
        user: UserProfile, scheme: Scheme, failed_criteria: List[str]
    ) -> Tuple[bool, Optional[NearMissReasoning]]:
        """
        Evaluates if a failed scheme qualifies as a 'Near-Miss' (fails only 1 or 2 soft/boundary criteria).
        Returns (is_near_miss, near_miss_reasoning_object).
        """
        if not failed_criteria or len(failed_criteria) > 2:
            return False, None

        # Check if the failure is on hard/unbridgeable constraints (e.g. completely wrong target occupation like Farmer vs Student)
        # However, if target occupation is somewhat adjacent (e.g. Unemployed vs Entrepreneur) it might be considered.
        soft_failures: List[str] = []
        action_steps: List[str] = []
        is_candidate_near_miss = True

        for fail in failed_criteria:
            fail_lower = fail.lower()

            # 1. Income threshold near-miss (within 15% margin)
            if "income" in fail_lower and scheme.max_income and user.annual_income:
                gap = user.annual_income - scheme.max_income
                pct_over = (gap / scheme.max_income) * 100
                if 0 < pct_over <= 20.0:
                    soft_failures.append(
                        f"Income of ₹{user.annual_income:,.0f} exceeds the ceiling limit of ₹{scheme.max_income:,.0f} by ₹{gap:,.0f} ({pct_over:.1f}%)."
                    )
                    action_steps.append(
                        f"If household income adjustments (such as standard deductions, medical allowances, or agricultural exemptions) bring gross taxable income below ₹{scheme.max_income:,.0f}, you will become fully eligible."
                    )
                else:
                    is_candidate_near_miss = False

            # 2. Age limit near-miss (within 2 years)
            elif "age" in fail_lower and user.age:
                if scheme.max_age and user.age > scheme.max_age:
                    years_over = user.age - scheme.max_age
                    if years_over <= 3:
                        soft_failures.append(
                            f"Age ({user.age} yrs) exceeds maximum limit of {scheme.max_age} yrs by {years_over} year(s)."
                        )
                        action_steps.append(
                            f"Check if you qualify for category age relaxations (e.g., 3-5 years relaxation for SC/ST/OBC/Women/PwD) available under state/central guidelines."
                        )
                    else:
                        is_candidate_near_miss = False
                elif scheme.min_age and user.age < scheme.min_age:
                    years_under = scheme.min_age - user.age
                    if years_under <= 1:
                        soft_failures.append(
                            f"Age ({user.age} yrs) is just {years_under} year below the minimum eligible age of {scheme.min_age}."
                        )
                        action_steps.append(
                            f"You will automatically qualify once you turn {scheme.min_age}. Begin preparing your project report and documents in advance."
                        )
                    else:
                        is_candidate_near_miss = False
                else:
                    is_candidate_near_miss = False

            # 3. Educational qualification near-miss (1 step below)
            elif "qualification" in fail_lower or "8th pass" in fail_lower or "10th pass" in fail_lower or "12th pass" in fail_lower:
                user_rank = get_qualification_rank(user.education_level)
                soft_failures.append(
                    f"Required educational qualification not fully met (Current: {user.education_level or 'Unspecified'})."
                )
                action_steps.append(
                    "You can enroll in National Institute of Open Schooling (NIOS) or apply for funding below ₹10 Lakhs where educational restrictions are relaxed."
                )

            # 4. Greenfield / New project condition
            elif "greenfield" in fail_lower or "new project" in fail_lower:
                soft_failures.append(
                    "Scheme requires greenfield (new unit setup), whereas you indicated an existing business."
                )
                action_steps.append(
                    "You can either apply for a new branch / distinct registered vertical, or opt for Mudra Scheme (Tarun) / PMEGP 2nd Loan for existing unit expansion."
                )

            # 5. Demographic / Category condition (e.g. Stand-Up India partnership)
            elif "women" in fail_lower or "sc/st" in fail_lower:
                soft_failures.append(
                    "Requires applicant to be a Woman or SC/ST entrepreneur."
                )
                action_steps.append(
                    "If setting up a partnership, LLP, or Pvt Ltd enterprise where at least 51% shareholding is held by a Woman or SC/ST co-founder, the venture qualifies for Stand-Up India."
                )

            # 6. Pucca house condition for housing schemes
            elif "pucca house" in fail_lower:
                soft_failures.append(
                    "Disqualified due to existing pucca house ownership."
                )
                action_steps.append(
                    "If applying for separate adult family units living independently without documented title in the existing pucca house, verify local municipal/panchayat survey criteria."
                )

            else:
                is_candidate_near_miss = False

        if not is_candidate_near_miss or not soft_failures:
            return False, None

        gap_exp = " | ".join(soft_failures)
        how_qual = " ".join(action_steps)

        return True, NearMissReasoning(
            failed_criteria=failed_criteria,
            gap_explanation=gap_exp,
            how_to_qualify=how_qual,
        )
