import unittest
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from backend.models.schemas import UserProfile, SchemeMatch, MatchReasoning
from backend.engine.rule_engine import RuleEngine, load_schemes_db
from backend.engine.near_miss import NearMissEvaluator
from backend.engine.ranking import RankingEngine
from backend.engine.document_checklist import DocumentChecklistManager


class TestMultiDomainRuleEngine(unittest.TestCase):
    def setUp(self):
        self.schemes = load_schemes_db()
        self.rule_engine = RuleEngine(self.schemes)

    def test_health_ayushman_bharat_match(self):
        # Low income family should match Ayushman Bharat PM-JAY regardless of occupation
        user = UserProfile(
            age=34,
            gender="Male",
            caste="OBC",
            occupation="Salaried",
            annual_income=220000,
            state="Bihar",
        )
        direct_ids = []
        for scheme in self.rule_engine.schemes:
            is_direct, matched, failed = self.rule_engine.evaluate_scheme(user, scheme)
            if is_direct:
                direct_ids.append(scheme.id)

        self.assertIn("pm_jay_health", direct_ids)

    def test_maternity_pmmvy_match(self):
        # Pregnant female should match PMMVY
        user = UserProfile(
            age=24,
            gender="Female",
            caste="General",
            occupation="Unemployed",
            annual_income=300000,
            state="Uttar Pradesh",
            is_pregnant_or_lactating=True,
        )
        direct_ids = []
        for scheme in self.rule_engine.schemes:
            is_direct, matched, failed = self.rule_engine.evaluate_scheme(user, scheme)
            if is_direct:
                direct_ids.append(scheme.id)

        self.assertIn("pmmvy_maternity", direct_ids)

    def test_solar_rooftop_pm_surya_ghar(self):
        # Homeowner with solar rooftop space
        user = UserProfile(
            age=40,
            gender="Male",
            caste="General",
            occupation="Salaried",
            annual_income=700000,
            state="Maharashtra",
            has_solar_rooftop_space=True,
        )
        direct_ids = []
        for scheme in self.rule_engine.schemes:
            is_direct, matched, failed = self.rule_engine.evaluate_scheme(user, scheme)
            if is_direct:
                direct_ids.append(scheme.id)

        self.assertIn("pm_surya_ghar", direct_ids)

    def test_disability_adip_scheme(self):
        # Differently abled citizen with 50% disability
        user = UserProfile(
            age=22,
            gender="Male",
            caste="SC",
            occupation="Student",
            annual_income=150000,
            state="Tamil Nadu",
            is_differently_abled=True,
            disability_percentage=50.0,
        )
        direct_ids = []
        for scheme in self.rule_engine.schemes:
            is_direct, matched, failed = self.rule_engine.evaluate_scheme(user, scheme)
            if is_direct:
                direct_ids.append(scheme.id)

        self.assertIn("adip_divyangjan", direct_ids)

    def test_girl_child_sukanya_samriddhi(self):
        # Parent of a 6-year-old girl child
        user = UserProfile(
            age=32,
            gender="Male",
            caste="General",
            occupation="Entrepreneur",
            annual_income=500000,
            state="Karnataka",
            has_girl_child=True,
            girl_child_age=6,
        )
        direct_ids = []
        for scheme in self.rule_engine.schemes:
            is_direct, matched, failed = self.rule_engine.evaluate_scheme(user, scheme)
            if is_direct:
                direct_ids.append(scheme.id)

        self.assertIn("ssy_girl_child", direct_ids)

    def test_senior_citizen_pension(self):
        # 65-year-old BPL senior citizen
        user = UserProfile(
            age=65,
            gender="Female",
            caste="SC",
            occupation="Unemployed",
            annual_income=90000,
            state="Rajasthan",
            has_bpl_ration_card=True,
        )
        direct_ids = []
        for scheme in self.rule_engine.schemes:
            is_direct, matched, failed = self.rule_engine.evaluate_scheme(user, scheme)
            if is_direct:
                direct_ids.append(scheme.id)

        self.assertIn("ignoaps_pension", direct_ids)

    def test_unorganised_worker_pension(self):
        # Construction / unorganised worker
        user = UserProfile(
            age=29,
            gender="Male",
            caste="OBC",
            occupation="Construction Worker",
            annual_income=140000,
            state="Madhya Pradesh",
            is_unorganised_worker=True,
            is_tax_payer=False,
        )
        direct_ids = []
        for scheme in self.rule_engine.schemes:
            is_direct, matched, failed = self.rule_engine.evaluate_scheme(user, scheme)
            if is_direct:
                direct_ids.append(scheme.id)

        self.assertIn("pm_sym_pension", direct_ids)

    def test_maharashtra_state_scheme_match(self):
        # Maharashtra resident female
        user = UserProfile(
            age=28,
            gender="Female",
            caste="OBC",
            occupation="Unemployed",
            annual_income=200000,
            state="Maharashtra",
        )
        direct_ids = []
        for scheme in self.rule_engine.schemes:
            is_direct, matched, failed = self.rule_engine.evaluate_scheme(user, scheme)
            if is_direct:
                direct_ids.append(scheme.id)

        # Should match Central PM-JAY AND Maharashtra MJPJAY AND Maharashtra Majhi Ladki Bahin
        self.assertIn("pm_jay_health", direct_ids)
        self.assertIn("mjpjay_maharashtra", direct_ids)
        self.assertIn("majhi_ladki_bahin_maharashtra", direct_ids)
        # Should NOT match Karnataka or Tamil Nadu state schemes
        self.assertNotIn("gruha_lakshmi_karnataka", direct_ids)
        self.assertNotIn("cmchis_tamil_nadu", direct_ids)

    def test_bihar_udyami_scheme(self):
        # Bihar resident entrepreneur
        user = UserProfile(
            age=22,
            gender="Female",
            caste="SC",
            occupation="Entrepreneur",
            annual_income=250000,
            state="Bihar",
            education_level="Graduate",
            is_new_project=True,
        )
        direct_ids = []
        for scheme in self.rule_engine.schemes:
            is_direct, matched, failed = self.rule_engine.evaluate_scheme(user, scheme)
            if is_direct:
                direct_ids.append(scheme.id)

        self.assertIn("udyami_yojana_bihar", direct_ids)
        self.assertIn("kanya_utthan_bihar", direct_ids)
        self.assertNotIn("mjpjay_maharashtra", direct_ids)

    def test_odisha_bsky_and_kalia(self):
        # Odisha farmer
        user = UserProfile(
            age=42,
            gender="Male",
            caste="OBC",
            occupation="Farmer",
            annual_income=120000,
            state="Odisha",
            is_farmer=True,
            has_bpl_ration_card=True,
        )
        direct_ids = []
        for scheme in self.rule_engine.schemes:
            is_direct, matched, failed = self.rule_engine.evaluate_scheme(user, scheme)
            if is_direct:
                direct_ids.append(scheme.id)

        self.assertIn("bsky_odisha", direct_ids)
        self.assertIn("kalia_odisha", direct_ids)
        self.assertNotIn("kisan_sahay_gujarat", direct_ids)

    def test_family_land_and_housing_scheme(self):
        # Rural houseless family in Andhra Pradesh
        user = UserProfile(
            age=36,
            gender="Female",
            caste="OBC",
            occupation="Construction Worker",
            annual_income=140000,
            state="Andhra Pradesh",
            area_type="Rural",
            owns_pucca_house=False,
            has_homestead_plot=True,
            owns_motorized_vehicle=False,
            is_tax_payer=False,
            has_bpl_ration_card=True,
            beneficiary_type="Family / Household",
        )
        direct_ids = []
        for scheme in self.rule_engine.schemes:
            is_direct, matched, failed = self.rule_engine.evaluate_scheme(user, scheme)
            if is_direct:
                direct_ids.append(scheme.id)

        # Should match national PMAY-G and AP Pedalandariki Illu (free house site + construction)
        self.assertIn("pmay_gramin_housing", direct_ids)
        self.assertIn("pedalandariki_illu_ap", direct_ids)

    def test_four_wheeler_and_itr_disqualification(self):
        # High asset household owning a car and paying income tax
        user = UserProfile(
            age=38,
            gender="Male",
            caste="General",
            occupation="Salaried",
            annual_income=900000,
            state="Maharashtra",
            owns_motorized_vehicle=True,
            is_tax_payer=True,
            owns_pucca_house=True,
        )
        pmay = next(s for s in self.rule_engine.schemes if s.id == "pmay_gramin_housing")
        is_direct, matched, failed = self.rule_engine.evaluate_scheme(user, pmay)

        self.assertFalse(is_direct)
        self.assertTrue(any("4-wheeler" in f or "car" in f for f in failed))
        self.assertTrue(any("Income Tax" in f or "ITR" in f for f in failed))
        self.assertTrue(any("pucca house" in f for f in failed))

    def test_landless_family_land_allotment(self):
        # Landless rural family in Odisha
        user = UserProfile(
            age=40,
            gender="Male",
            caste="SC",
            occupation="Unemployed",
            annual_income=80000,
            state="Odisha",
            area_type="Rural",
            is_landless=True,
            owns_agricultural_land=False,
            owns_pucca_house=False,
        )
        direct_ids = []
        for scheme in self.rule_engine.schemes:
            is_direct, matched, failed = self.rule_engine.evaluate_scheme(user, scheme)
            if is_direct:
                direct_ids.append(scheme.id)

        # Should match Vasundhara homestead land distribution
        self.assertIn("vasundhara_odisha", direct_ids)

    def test_near_miss_girl_child_age(self):
        # Girl child is 11 years old (exceeds 10-year limit by 1 year)
        user = UserProfile(
            age=35,
            gender="Female",
            caste="General",
            occupation="Salaried",
            annual_income=400000,
            state="Delhi",
            has_girl_child=True,
            girl_child_age=11,
        )
        ssy = next(s for s in self.rule_engine.schemes if s.id == "ssy_girl_child")
        is_direct, matched, failed = self.rule_engine.evaluate_scheme(user, ssy)
        self.assertFalse(is_direct)

        is_near, reason = NearMissEvaluator.evaluate_near_miss(user, ssy, failed)
        self.assertTrue(is_near)
        self.assertIn("11", reason.gap_explanation)


if __name__ == "__main__":
    unittest.main(verbosity=2)
