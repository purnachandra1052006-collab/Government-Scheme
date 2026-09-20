import os
import sys
from typing import List, Dict, Any, Optional

# Ensure project root is in sys.path regardless of execution directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.config import config
from backend.models.schemas import (
    UserProfile,
    Scheme,
    SchemeMatch,
    EvaluationResponse,
    ChatIntakeSession,
    IntakeAnswerPayload,
    MatchReasoning,
)
from backend.engine.rule_engine import RuleEngine, load_schemes_db
from backend.engine.near_miss import NearMissEvaluator
from backend.engine.ranking import RankingEngine
from backend.engine.llm_explainer import llm_explainer
from backend.engine.intake_manager import intake_manager
from backend.engine.document_checklist import DocumentChecklistManager

app = FastAPI(
    title="Government Scheme-Matching Assistant API",
    description="Deterministic rule verification, near-miss intelligence, and LLM-powered transparent reasoning for Indian government schemes.",
    version="1.0.0",
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load schemes database
schemes_db: List[Scheme] = load_schemes_db()
rule_engine = RuleEngine(schemes_db)


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "schemes_loaded": len(schemes_db),
        "groq_configured": bool(llm_explainer.api_key),
        "groq_model": config.GROQ_MODEL,
    }


@app.get("/api/schemes", response_model=List[Scheme])
def get_all_schemes():
    return schemes_db


@app.get("/api/schemes/{scheme_id}", response_model=Scheme)
def get_scheme(scheme_id: str):
    for s in schemes_db:
        if s.id == scheme_id:
            return s
    raise HTTPException(status_code=404, detail="Scheme not found")


@app.post("/api/chat/start", response_model=ChatIntakeSession)
def start_chat_session():
    return intake_manager.create_session()


@app.post("/api/chat/message", response_model=ChatIntakeSession)
def process_chat_message(payload: IntakeAnswerPayload):
    session_id = payload.session_id or "default_session"
    return intake_manager.process_turn(
        session_id=session_id,
        user_message=payload.user_message,
        field=payload.field,
        value=payload.value,
        current_profile=payload.current_profile,
    )



@app.post("/api/evaluate", response_model=EvaluationResponse)
def evaluate_profile(profile: UserProfile):
    direct_matches: List[SchemeMatch] = []
    near_miss_matches: List[SchemeMatch] = []

    for scheme in schemes_db:
        is_direct, matched_criteria, failed_criteria = rule_engine.evaluate_scheme(
            profile, scheme
        )

        if is_direct:
            match_score, fin_score, total_rank = RankingEngine.calculate_scores(
                match_type="direct",
                matched_criteria=matched_criteria,
                failed_criteria=[],
                scheme=scheme,
                user=profile,
            )
            reasoning = llm_explainer.generate_scheme_reasoning(
                profile, scheme, matched_criteria
            )
            direct_matches.append(
                SchemeMatch(
                    scheme=scheme,
                    match_type="direct",
                    match_score=match_score,
                    financial_score=fin_score,
                    total_rank_score=total_rank,
                    reasoning=reasoning,
                    near_miss_info=None,
                )
            )
        else:
            is_near_miss, near_miss_info = NearMissEvaluator.evaluate_near_miss(
                profile, scheme, failed_criteria
            )
            if is_near_miss and near_miss_info:
                match_score, fin_score, total_rank = RankingEngine.calculate_scores(
                    match_type="near_miss",
                    matched_criteria=matched_criteria,
                    failed_criteria=failed_criteria,
                    scheme=scheme,
                    user=profile,
                )
                reasoning = MatchReasoning(
                    why_you_qualify=matched_criteria,
                    key_benefits_highlight=scheme.key_benefits[:2],
                    action_items=[near_miss_info.how_to_qualify],
                )
                near_miss_matches.append(
                    SchemeMatch(
                        scheme=scheme,
                        match_type="near_miss",
                        match_score=match_score,
                        financial_score=fin_score,
                        total_rank_score=total_rank,
                        reasoning=reasoning,
                        near_miss_info=near_miss_info,
                    )
                )

    # Rank both lists
    ranked_direct = RankingEngine.rank_matches(direct_matches)
    ranked_near_miss = RankingEngine.rank_matches(near_miss_matches)

    # Separate into Primary Requirement Matches vs Additional Opportunities
    user_interests = [d.lower() for d in (profile.interested_domains or [])]
    user_goal = (profile.specific_goal or "").lower()

    primary_matches: List[SchemeMatch] = []
    other_matches: List[SchemeMatch] = []

    for match in ranked_direct:
        s_domain = (match.scheme.category or match.scheme.domain or "").lower()
        s_name = match.scheme.name.lower()
        s_desc = match.scheme.description.lower()

        is_primary = False
        if user_interests:
            if any(interest in s_domain for interest in user_interests):
                is_primary = True
        elif user_goal:
            if any(term in s_domain or term in s_name or term in s_desc for term in user_goal.split()):
                is_primary = True

        if is_primary:
            primary_matches.append(match)
        else:
            other_matches.append(match)

    # If user didn't specify a narrow target, all direct matches are primary
    if not user_interests and not user_goal:
        primary_matches = ranked_direct
        other_matches = []
    elif not primary_matches:
        # If no strict domain matched, keep top direct as primary
        primary_matches = ranked_direct[:3]
        other_matches = ranked_direct[3:]

    # Generate consolidated documents checklist
    consolidated_docs = DocumentChecklistManager.generate_consolidated_checklist(
        ranked_direct, ranked_near_miss
    )

    # Generate overall summary insight
    top_schemes = [m.scheme for m in primary_matches] if primary_matches else [m.scheme for m in ranked_direct]
    summary_insight = llm_explainer.generate_overall_summary(
        profile, len(ranked_direct), len(ranked_near_miss), top_schemes
    )

    return EvaluationResponse(
        user_profile=profile,
        direct_matches=ranked_direct,
        primary_matches=primary_matches,
        other_matches=other_matches,
        near_miss_matches=ranked_near_miss,
        total_direct_count=len(ranked_direct),
        total_near_miss_count=len(ranked_near_miss),
        expressed_requirements=profile.interested_domains or ([profile.specific_goal] if profile.specific_goal else []),
        target_domain_labels=profile.interested_domains or [],
        consolidated_documents=consolidated_docs,
        summary_insight=summary_insight,
    )



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.HOST, port=config.PORT)
