import pytest
from backend.models.schemas import UserProfile
from backend.engine.rule_engine import RuleEngine, load_schemes_db
from backend.engine.near_miss import NearMissEvaluator
from backend.engine.ranking import RankingEngine
from backend.engine.document_checklist import DocumentChecklistManager


@pytest.fixture
def rule_engine():
    schemes = load_schemes_db()
    return RuleEngine(schemes)


def test_student_scholarship_direct_match(rule_engine):
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
    for scheme in rule_engine.schemes:
        is_direct, matched, failed = rule_engine.evaluate_scheme(user, scheme)
        if is_direct:
            direct_ids.append(scheme.id)

    # Post-Matric Scholarship should match
    assert "post_matric_04" in direct_ids


def test_entrepreneur_pmegp_and_standup(rule_engine):
    # Female SC Entrepreneur starting new venture
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
    for scheme in rule_engine.schemes:
        is_direct, matched, failed = rule_engine.evaluate_scheme(user, scheme)
        if is_direct:
            direct_ids.append(scheme.id)

    assert "pmegp_01" in direct_ids
    assert "standup_03" in direct_ids
    assert "mudra_02" in direct_ids


def test_near_miss_income_overflow(rule_engine):
    # Student with income ₹2,60,000 (just 4% above ₹2.5L cap of Post-Matric)
    user = UserProfile(
        age=21,
        gender="Female",
        caste="OBC",
        occupation="Student",
        annual_income=260000,
        state="Delhi",
        education_level="12th Pass",
    )
    post_matric = next(s for s in rule_engine.schemes if s.id == "post_matric_04")
    is_direct, matched, failed = rule_engine.evaluate_scheme(user, post_matric)

    assert not is_direct
    assert any("exceeds maximum ceiling" in f for f in failed)

    is_near_miss, reason = NearMissEvaluator.evaluate_near_miss(user, post_matric, failed)
    assert is_near_miss is True
    assert reason is not None
    assert "₹260,000" in reason.gap_explanation or "260,000" in reason.gap_explanation
    assert "household income" in reason.how_to_qualify.lower()


def test_farmer_pm_kisan_match(rule_engine):
    user = UserProfile(
        age=45,
        gender="Male",
        caste="General",
        occupation="Farmer",
        annual_income=120000,
        state="Uttar Pradesh",
        is_tax_payer=False,
    )
    pm_kisan = next(s for s in rule_engine.schemes if s.id == "pm_kisan_05")
    is_direct, matched, failed = rule_engine.evaluate_scheme(user, pm_kisan)

    assert is_direct is True


def test_artisan_vishwakarma_match(rule_engine):
    user = UserProfile(
        age=35,
        gender="Male",
        caste="OBC",
        occupation="Artisan",
        annual_income=150000,
        state="Rajasthan",
    )
    vishwakarma = next(s for s in rule_engine.schemes if s.id == "pm_vishwakarma_07")
    is_direct, matched, failed = rule_engine.evaluate_scheme(user, vishwakarma)

    assert is_direct is True


def test_document_consolidation(rule_engine):
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
    for scheme in rule_engine.schemes:
        is_d, m, f = rule_engine.evaluate_scheme(user, scheme)
        if is_d:
            direct.append(scheme)

    from backend.models.schemas import SchemeMatch, MatchReasoning
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
    assert len(docs.universal_documents) > 0
    assert any("Aadhaar" in doc for doc in docs.universal_documents)
