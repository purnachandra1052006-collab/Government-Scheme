import uuid
from typing import Dict, Optional, Any, List
from backend.models.schemas import (
    UserProfile,
    IntakeQuestion,
    IntakeQuestionOption,
    ChatIntakeSession,
    ChatMessage,
)

# Adaptive question bank with dynamic conditions
QUESTIONS_CONFIG = [
    {
        "id": "q_occupation_goal",
        "field": "occupation",
        "step": 1,
        "question": "Welcome! Let's find the government schemes, grants, and subsidies you're eligible for. What best describes your primary occupation or current status?",
        "helper_text": "Select your current occupational category to help us personalize scheme rules.",
        "input_type": "select",
        "options": [
            {"label": "💼 Entrepreneur / Business Owner", "value": "Entrepreneur", "description": "Running or launching an enterprise, MSME, or startup"},
            {"label": "🎓 Student / Scholar", "value": "Student", "description": "Enrolled in school, college, university, or competitive exams"},
            {"label": "🌾 Farmer / Agri Worker", "value": "Farmer", "description": "Agricultural landholder, tenant farmer, or allied dairy/fisheries worker"},
            {"label": "🛒 Street Vendor / Hawkers", "value": "Street Vendor", "description": "Engaged in urban/peri-urban retail vending or carts"},
            {"label": "⚒️ Traditional Artisan / Craftsperson", "value": "Artisan", "description": "Carpenter, blacksmith, potter, tailor, goldsmith, weaver, etc."},
            {"label": "🔍 Jobseeker / Unemployed", "value": "Unemployed", "description": "Looking for skill training, apprenticeships, or livelihood support"},
            {"label": "🏢 Salaried / Working Professional", "value": "Salaried", "description": "Employed in private/public sector looking for housing/education benefits"}
        ],
    },
    {
        "id": "q_age_gender",
        "field": "age",
        "step": 2,
        "question": "Great! What is your age and gender?",
        "helper_text": "Age and gender criteria determine specific targeted benefits like Stand-Up India or youth schemes.",
        "input_type": "number",
        "min_val": 14,
        "max_val": 90,
        "unit": "years",
        "options": [
            {"label": "18 - 25 years (Youth / Student)", "value": 22},
            {"label": "26 - 35 years (Young Entrepreneur)", "value": 30},
            {"label": "36 - 55 years (Established Adult)", "value": 42},
            {"label": "56+ years (Senior Citizen)", "value": 60}
        ]
    },
    {
        "id": "q_gender",
        "field": "gender",
        "step": 3,
        "question": "Please select your gender:",
        "helper_text": "Many central schemes offer higher subsidies and reservations for women entrepreneurs.",
        "input_type": "select",
        "options": [
            {"label": "👩 Female", "value": "Female", "description": "Eligible for specialized Stand-Up India & women MSME subsidy tiers"},
            {"label": "👨 Male", "value": "Male", "description": "General & reserved category schemes"},
            {"label": "⚧ Other / Transgender", "value": "Other", "description": "Eligible for all inclusive social welfare programs"}
        ]
    },
    {
        "id": "q_caste_category",
        "field": "caste",
        "step": 4,
        "question": "Which social category do you belong to?",
        "helper_text": "Government schemes often offer elevated subsidies (e.g. 35% in PMEGP) and reserved quotas for SC/ST/OBC/EWS.",
        "input_type": "select",
        "options": [
            {"label": "General", "value": "General", "description": "Standard central & state scheme eligibility"},
            {"label": "OBC (Other Backward Class)", "value": "OBC", "description": "Eligible for scholarships & special credit subventions"},
            {"label": "SC (Scheduled Caste)", "value": "SC", "description": "Highest subsidy tier (up to 35%) & Stand-Up India access"},
            {"label": "ST (Scheduled Tribe)", "value": "ST", "description": "Highest subsidy tier & priority tribal welfare allocations"},
            {"label": "EWS (Economically Weaker Section)", "value": "EWS", "description": "Income-assessed general category benefits"}
        ]
    },
    {
        "id": "q_annual_income",
        "field": "annual_income",
        "step": 5,
        "question": "What is your approximate gross Annual Household Income?",
        "helper_text": "Used to verify income caps on scholarships (₹2.5L-₹4.5L), housing subsidies (₹6L), etc.",
        "input_type": "currency",
        "options": [
            {"label": "Below ₹1.5 Lakhs / year", "value": 120000, "description": "BPL / Economically vulnerable tier"},
            {"label": "₹1.5 Lakhs - ₹2.5 Lakhs / year", "value": 220000, "description": "Eligible for 100% Post-Matric scholarships"},
            {"label": "₹2.5 Lakhs - ₹4.5 Lakhs / year", "value": 380000, "description": "Eligible for CSSS scholarships & PMAY housing"},
            {"label": "₹4.5 Lakhs - ₹6 Lakhs / year", "value": 550000, "description": "Eligible for PMAY CLSS interest subsidy"},
            {"label": "Above ₹6 Lakhs / year", "value": 800000, "description": "PMEGP, MUDRA, Startup India, & Stand-Up India (No income cap)"}
        ]
    },
    # Adaptive Questions based on Occupation:
    # 1. If Student:
    {
        "id": "q_student_edu",
        "field": "education_level",
        "step": 6,
        "condition": lambda p: p.occupation == "Student",
        "question": "What is your current or highest completed educational level?",
        "helper_text": "Scholarships like Post-Matric and CSSS require matriculation or 12th pass status.",
        "input_type": "select",
        "options": [
            {"label": "10th Pass (Matriculation)", "value": "10th Pass", "description": "Applying for Diploma or 10+2"},
            {"label": "12th Pass (Higher Secondary)", "value": "12th Pass", "description": "Applying for Degree or Professional courses"},
            {"label": "Undergraduate Degree", "value": "Graduate", "description": "Pursuing PG, Masters, or competitive research"},
            {"label": "Post Graduate / Doctorate", "value": "Post Graduate", "description": "Advanced research or fellowships"}
        ]
    },
    # 2. If Entrepreneur:
    {
        "id": "q_entrepreneur_project",
        "field": "is_new_project",
        "step": 6,
        "condition": lambda p: p.occupation == "Entrepreneur",
        "question": "Are you starting a brand new venture (Greenfield) or expanding an existing business?",
        "helper_text": "PMEGP and Stand-Up India strictly fund new greenfield projects; MUDRA funds both.",
        "input_type": "select",
        "options": [
            {"label": "🌱 Brand New Venture (Greenfield)", "value": True, "description": "Setting up a fresh enterprise from scratch"},
            {"label": "📈 Existing Business Expansion", "value": False, "description": "Scaling, buying machinery, or working capital for existing unit"}
        ]
    },
    {
        "id": "q_entrepreneur_funding",
        "field": "funding_required",
        "step": 7,
        "condition": lambda p: p.occupation == "Entrepreneur",
        "question": "How much funding or loan amount are you seeking?",
        "helper_text": "Helps match with Shishu (<₹50k), Kishore (<₹5L), Tarun (<₹20L), PMEGP (<₹50L), or Stand-Up India (<₹1 Cr).",
        "input_type": "currency",
        "options": [
            {"label": "Micro-loan up to ₹50,000 (MUDRA Shishu)", "value": 50000},
            {"label": "₹50,000 to ₹5 Lakhs (MUDRA Kishore)", "value": 350000},
            {"label": "₹5 Lakhs to ₹20 Lakhs (MUDRA Tarun / PMEGP)", "value": 1500000},
            {"label": "₹20 Lakhs to ₹50 Lakhs (PMEGP Manufacturing)", "value": 4500000},
            {"label": "₹50 Lakhs to ₹1 Crore+ (Stand-Up India / SISFS)", "value": 8500000}
        ]
    },
    # 3. If Farmer:
    {
        "id": "q_farmer_tax",
        "field": "is_tax_payer",
        "step": 6,
        "condition": lambda p: p.occupation == "Farmer",
        "question": "Do you or any immediate family member pay income tax?",
        "helper_text": "PM-KISAN eligibility mandates non-taxpayer status for smallholder farmer direct benefit transfers.",
        "input_type": "select",
        "options": [
            {"label": "No, we are non-taxpayers", "value": False, "description": "Fully eligible for PM-KISAN ₹6,000/yr and subsidized KCC"},
            {"label": "Yes, we pay Income Tax", "value": True, "description": "Exempt from PM-KISAN, eligible for agri-infrastructure loans"}
        ]
    },
    # 4. If Artisan / Street Vendor / Unemployed:
    {
        "id": "q_education_general",
        "field": "education_level",
        "step": 6,
        "condition": lambda p: p.occupation in ["Artisan", "Street Vendor", "Unemployed", "Salaried"] and p.education_level is None,
        "question": "What is your highest educational qualification?",
        "helper_text": "Some schemes (PMKVY / NAPS) cater to school dropouts and 8th/10th pass candidates.",
        "input_type": "select",
        "options": [
            {"label": "Below 8th Pass / No formal schooling", "value": "Below 8th"},
            {"label": "8th Pass", "value": "8th Pass"},
            {"label": "10th Pass (Matriculation)", "value": "10th Pass"},
            {"label": "12th Pass / ITI / Diploma", "value": "12th Pass"},
            {"label": "Graduate & Above", "value": "Graduate"}
        ]
    },
    # 5. Housing check for Salaried / Unemployed
    {
        "id": "q_housing",
        "field": "owns_pucca_house",
        "step": 7,
        "condition": lambda p: p.occupation in ["Salaried", "Unemployed"] and p.owns_pucca_house is False,
        "question": "Does your family currently own a permanent pucca house anywhere in India?",
        "helper_text": "Determines eligibility for Pradhan Mantri Awas Yojana (PMAY) ₹2.67 Lakhs housing subsidy.",
        "input_type": "select",
        "options": [
            {"label": "No, we live in rent or kutcha house (Seeking first home)", "value": False, "description": "Eligible for PMAY housing grants and interest subsidy"},
            {"label": "Yes, family owns a pucca house", "value": True, "description": "Eligible for other MSME and educational welfare programs"}
        ]
    }
]


class IntakeManager:
    def __init__(self):
        self.sessions: Dict[str, ChatIntakeSession] = {}

    def create_session(self) -> ChatIntakeSession:
        session_id = str(uuid.uuid4())
        profile = UserProfile()
        first_q = self._get_next_question(profile)
        session = ChatIntakeSession(
            session_id=session_id,
            profile=profile,
            current_step=1,
            total_steps=7,
            is_complete=False,
            next_question=first_q,
            history=[
                ChatMessage(
                    role="assistant",
                    content=first_q.question if first_q else "Welcome to Scheme Matcher!",
                    question_payload=first_q,
                    quick_options=[opt.label for opt in first_q.options] if (first_q and first_q.options) else None
                )
            ]
        )
        self.sessions[session_id] = session
        return session

    def process_answer(
        self, session_id: str, field: str, value: Any, current_profile: Optional[UserProfile] = None
    ) -> ChatIntakeSession:
        session = self.sessions.get(session_id)
        if not session:
            session = self.create_session()
            session.session_id = session_id
            self.sessions[session_id] = session

        if current_profile:
            session.profile = current_profile

        # Update profile with answer
        if hasattr(session.profile, field):
            setattr(session.profile, field, value)

        # Record user message in history
        val_str = str(value)
        session.history.append(
            ChatMessage(role="user", content=f"{field}: {val_str}")
        )

        # Determine next question
        next_q = self._get_next_question(session.profile)
        if next_q is None:
            session.is_complete = True
            session.next_question = None
            session.history.append(
                ChatMessage(
                    role="assistant",
                    content="🎉 Perfect! All your profile details have been collected. We are now running our deterministic rule engine and AI reasoning model to find your matching schemes.",
                )
            )
        else:
            session.next_question = next_q
            session.current_step = next_q.step
            session.history.append(
                ChatMessage(
                    role="assistant",
                    content=next_q.question,
                    question_payload=next_q,
                    quick_options=[opt.label for opt in next_q.options] if next_q.options else None,
                )
            )

        return session

    def _get_next_question(self, profile: UserProfile) -> Optional[IntakeQuestion]:
        # Filter applicable questions based on conditions and unset fields in profile
        applicable_questions = []
        for q_cfg in QUESTIONS_CONFIG:
            field = q_cfg["field"]
            # Check condition if present
            condition_fn = q_cfg.get("condition")
            if condition_fn and not condition_fn(profile):
                continue

            current_val = getattr(profile, field, None)
            # Special case for boolean values (where False is a valid value, not None)
            if current_val is None:
                applicable_questions.append(q_cfg)

        if not applicable_questions:
            return None

        # Pick the first applicable question
        selected = applicable_questions[0]
        options = [
            IntakeQuestionOption(
                label=opt["label"],
                value=opt["value"],
                description=opt.get("description"),
            )
            for opt in selected.get("options", [])
        ] if selected.get("options") else None

        return IntakeQuestion(
            id=selected["id"],
            field=selected["field"],
            question=selected["question"],
            helper_text=selected.get("helper_text"),
            input_type=selected["input_type"],
            options=options,
            min_val=selected.get("min_val"),
            max_val=selected.get("max_val"),
            unit=selected.get("unit"),
            step=selected.get("step", 1),
            total_steps=7,
        )


intake_manager = IntakeManager()
