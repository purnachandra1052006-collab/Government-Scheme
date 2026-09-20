import unittest
import sys
import os

# Ensure workspace root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from backend.models.schemas import UserProfile, SchemeMatch, MatchReasoning
from backend.engine.rule_engine import RuleEngine, load_schemes_db
from backend.engine.near_miss import NearMissEvaluator
from backend.engine.ranking import RankingEngine
from backend.engine.document_checklist import DocumentChecklistManager


class TestRuleEngineAndLogic(unittest.TestCase):
    def setUp(self):
        self.schemes = load_schemes_db()
        self.rule_engine = RuleEngine(self.schemes)

    def test_student_scholarship_direct_match(self):
        user = UserProfile(
            age=20,
            gender="Male",
            caste="SC",
            occupation="Student",
            annual_income=180000,
            state="Maharashtra",
            education_level="12th Pass",
        )
        direct_ids = []
        for scheme in self.rule_engine.schemes:
            is_direct, matched, failed = self.rule_engine.evaluate_scheme(user, scheme)
            if is_direct:
                direct_ids.append(scheme.id)

        self.assertIn("post_matric_04", direct_ids)
        self.assertIn("csss_10", direct_ids)

    def test_entrepreneur_pmegp_and_standup(self):
        user = UserProfile(
            age=28,
            gender="Female",
            caste="SC",
            occupation="Entrepreneur",
            annual_income=400000,
            state="Karnataka",
            education_level="Graduate",
            is_new_project=True,
            funding_required=2500000,
        )
        direct_ids = []
        for scheme in self.rule_engine.schemes:
            is_direct, matched, failed = self.rule_engine.evaluate_scheme(user, scheme)
            if is_direct:
                direct_ids.append(scheme.id)

        self.assertIn("pmegp_01", direct_ids)
        self.assertIn("standup_03", direct_ids)
        self.assertIn("mudra_02", direct_ids)

    def test_near_miss_income_overflow(self):
        user = UserProfile(
            age=21,
            gender="Female",
            caste="OBC",
            occupation="Student",
            annual_income=260000,
            state="Delhi",
            education_level="12th Pass",
        )
        post_matric = next(s for s in self.rule_engine.schemes if s.id == "post_matric_04")
        is_direct, matched, failed = self.rule_engine.evaluate_scheme(user, post_matric)

        self.assertFalse(is_direct)
        is_near_miss, reason = NearMissEvaluator.evaluate_near_miss(user, post_matric, failed)
        self.assertTrue(is_near_miss)
        self.assertIsNotNone(reason)
        self.assertTrue("₹260,000" in reason.gap_explanation or "260,000" in reason.gap_explanation)
        self.assertIn("household income", reason.how_to_qualify.lower())

    def test_farmer_pm_kisan_match(self):
        user = UserProfile(
            age=45,
            gender="Male",
            caste="General",
            occupation="Farmer",
            annual_income=120000,
            state="Uttar Pradesh",
            is_tax_payer=False,
        )
        pm_kisan = next(s for s in self.rule_engine.schemes if s.id == "pm_kisan_05")
        is_direct, matched, failed = self.rule_engine.evaluate_scheme(user, pm_kisan)

        self.assertTrue(is_direct)

    def test_artisan_vishwakarma_match(self):
        user = UserProfile(
            age=35,
            gender="Male",
            caste="OBC",
            occupation="Artisan",
            annual_income=150000,
            state="Rajasthan",
        )
        vishwakarma = next(s for s in self.rule_engine.schemes if s.id == "pm_vishwakarma_07")
        is_direct, matched, failed = self.rule_engine.evaluate_scheme(user, vishwakarma)

        self.assertTrue(is_direct)

    def test_document_consolidation(self):
        user = UserProfile(
            age=24,
            gender="Female",
            caste="SC",
            occupation="Entrepreneur",
            annual_income=300000,
            state="Tamil Nadu",
            education_level="Graduate",
            is_new_project=True,
        )
        direct = []
        for scheme in self.rule_engine.schemes:
            is_d, m, f = self.rule_engine.evaluate_scheme(user, scheme)
            if is_d:
                direct.append(scheme)

        direct_matches = [
            SchemeMatch(
                scheme=s,
                match_type="direct",
                match_score=90.0,
                financial_score=80.0,
                total_rank_score=1085.0,
                reasoning=MatchReasoning(why_you_qualify=[], key_benefits_highlight=[], action_items=[])
            )
            for s in direct
        ]
        docs = DocumentChecklistManager.generate_consolidated_checklist(direct_matches, [])
        self.assertTrue(len(docs.universal_documents) > 0)
        self.assertTrue(any("Aadhaar" in doc for doc in docs.universal_documents))


if __name__ == "__main__":
    unittest.main(verbosity=2)
