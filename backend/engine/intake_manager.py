import uuid
from typing import Dict, Optional, Any, List
from backend.models.schemas import (
    UserProfile,
    IntakeQuestion,
    IntakeQuestionOption,
    ChatIntakeSession,
    ChatMessage,
)
from backend.engine.llm_explainer import llm_explainer
from backend.engine.rule_engine import load_schemes_db

schemes_db_cache = load_schemes_db()
SCHEMES_SUMMARY_TEXT = "\n".join([f"- {s.name} ({s.category}): {s.max_subsidy_or_loan}. Target: {', '.join(s.target_audience)}" for s in schemes_db_cache])


class IntakeManager:
    def __init__(self):
        self.sessions: Dict[str, ChatIntakeSession] = {}

    def create_session(self) -> ChatIntakeSession:
        session_id = str(uuid.uuid4())
        profile = UserProfile()
        
        welcome_content = "Namaste & Welcome to GovScheme.AI! I am your AI Government Welfare Advisor. Tell me about yourself (for example: your occupation, age, state, or any specific support you are looking for), and I will guide you to all matching schemes, grants, and subsidies."
        suggested_replies = [
            "💼 I am an Entrepreneur seeking business loans",
            "🎓 I am a Student looking for scholarships",
            "🌾 I am a Farmer looking for crop & income support",
            "☀️ I want Solar Rooftop subsidies for my home",
            "🤰 I am an expecting mother looking for maternity benefits"
        ]

        session = ChatIntakeSession(
            session_id=session_id,
            profile=profile,
            current_step=1,
            total_steps=7,
            is_complete=False,
            is_ready_to_evaluate=False,
            suggested_quick_replies=suggested_replies,
            history=[
                ChatMessage(
                    role="assistant",
                    content=welcome_content,
                    quick_options=suggested_replies
                )
            ]
        )
        self.sessions[session_id] = session
        return session

    def process_turn(
        self,
        session_id: str,
        user_message: Optional[str] = None,
        field: Optional[str] = None,
        value: Optional[Any] = None,
        current_profile: Optional[UserProfile] = None
    ) -> ChatIntakeSession:
        session = self.sessions.get(session_id)
        if not session:
            session = self.create_session()
            session.session_id = session_id
            self.sessions[session_id] = session

        active_profile = current_profile or session.profile

        # If user selected a structured button
        if field and value is not None:
            if hasattr(active_profile, field):
                setattr(active_profile, field, value)
            user_text = user_message or f"{field}: {value}"
        else:
            user_text = user_message or ""

        # Record user message in history
        session.history.append(
            ChatMessage(role="user", content=user_text)
        )

        # Build message history for LLM
        formatted_history = [
            {"role": msg.role, "content": msg.content}
            for msg in session.history
        ]

        # Use LLM to extract attributes, answer questions, and formulate conversational reply
        updated_profile, assistant_reply, suggested_replies, is_ready = llm_explainer.process_conversational_turn(
            user_message=user_text,
            current_profile=active_profile,
            chat_history=formatted_history,
            schemes_summary=SCHEMES_SUMMARY_TEXT,
        )

        session.profile = updated_profile
        session.is_ready_to_evaluate = is_ready
        session.suggested_quick_replies = suggested_replies

        # Count completed core fields to calculate step
        filled_count = sum(1 for v in [
            updated_profile.occupation,
            updated_profile.age,
            updated_profile.gender,
            updated_profile.caste,
            updated_profile.annual_income,
            updated_profile.state
        ] if v is not None)

        session.current_step = min(7, filled_count + 1)
        if filled_count >= 5 and is_ready:
            session.is_complete = True

        session.history.append(
            ChatMessage(
                role="assistant",
                content=assistant_reply,
                quick_options=suggested_replies,
            )
        )

        return session


intake_manager = IntakeManager()
