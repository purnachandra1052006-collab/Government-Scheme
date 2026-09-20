import json
import logging
import re
from typing import List, Dict, Any, Optional, Tuple
from openai import OpenAI
from backend.config import config
from backend.models.schemas import (
    UserProfile,
    Scheme,
    MatchReasoning,
)

logger = logging.getLogger(__name__)


class LLMExplainer:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or config.GROQ_API_KEY
        self.client = None
        if self.api_key:
            try:
                self.client = OpenAI(
                    api_key=self.api_key,
                    base_url=config.GROQ_BASE_URL,
                )
            except Exception as e:
                logger.warning(f"Failed to initialize Groq client: {e}")
                self.client = None

    def update_api_key(self, api_key: str):
        self.api_key = api_key
        if self.api_key:
            try:
                self.client = OpenAI(
                    api_key=self.api_key,
                    base_url=config.GROQ_BASE_URL,
                )
            except Exception as e:
                logger.warning(f"Failed to re-initialize Groq client: {e}")
                self.client = None

    def process_conversational_turn(
        self,
        user_message: str,
        current_profile: UserProfile,
        chat_history: List[Dict[str, str]],
        schemes_summary: str = "",
    ) -> Tuple[UserProfile, str, List[str], bool]:
        """
        Processes natural language user dialogue with the LLM:
        1. Extracts profile attributes mentioned in text.
        2. Answers citizen questions about schemes.
        3. Returns conversational reply + smart dynamic quick-reply suggestions.
        """
        profile_dict = current_profile.model_dump()
        extracted_updates = {}
        assistant_reply = ""
        suggested_replies = []
        is_ready_to_evaluate = False

        if self.client:
            try:
                prompt = f"""You are GovScheme.AI, an empathetic, expert government welfare and scheme advisor for Indian citizens.
Your job is to have a natural, helpful conversation with the citizen, extract their profile attributes into structured data, answer any questions they have about government schemes, and guide them towards discovering all schemes they are eligible for.

Current Citizen Profile state:
{json.dumps(profile_dict, indent=2)}

Available National Schemes Context (Brief):
{schemes_summary[:3000]}

Conversation History:
{json.dumps(chat_history[-6:], indent=2)}

Citizen's Latest Message:
"{user_message}"

Task:
1. Extract any newly provided or updated profile attributes from the citizen's message.
   Possible fields to extract:
   - age (int, e.g. 28)
   - gender ("Female" | "Male" | "Other")
   - caste ("General" | "OBC" | "SC" | "ST" | "EWS")
   - occupation ("Entrepreneur" | "Student" | "Farmer" | "Street Vendor" | "Artisan" | "Construction Worker" | "Unemployed" | "Salaried")
   - annual_income (float in INR, e.g. 250000)
   - state (e.g. "Karnataka", "Maharashtra", "Uttar Pradesh", "Bihar", etc.)
   - area_type ("Rural" | "Urban" | "Semi-Urban")
   - education_level ("Below 8th" | "8th Pass" | "10th Pass" | "12th Pass" | "Diploma" | "Graduate" | "Post Graduate")
   - specific_goal (string describing primary goal)
   - is_pregnant_or_lactating (boolean)
   - has_girl_child (boolean) & girl_child_age (int)
   - is_differently_abled (boolean) & disability_percentage (float)
   - has_solar_rooftop_space (boolean)
   - has_bpl_ration_card (boolean)
   - is_unorganised_worker (boolean)
   - business_type (string, e.g. "Manufacturing", "Dairy", "Solar", "Tech")
   - funding_required (float)
   - is_new_project (boolean)
   - land_holding_acres (float)

2. If the user asked a question about a scheme or benefit (e.g., "What is PM Surya Ghar?", "Can I get loan for my business?"), answer it clearly, concisely, and encouragingly.

3. Formulate a friendly, natural assistant reply that:
   - Confirms what you understood.
   - Answers their query (if any).
   - Asks for the next most relevant missing profile detail (such as income, age, or state) to complete their eligibility evaluation.

4. Provide 2-4 context-aware suggested quick-reply buttons (e.g., ["Income is under ₹2.5L", "Income is ₹5L+", "Tell me about Dairy loans", "Run Eligibility Match"]).

5. Set "is_ready_to_evaluate": true if the user explicitly asks to see eligible schemes / results, OR if core attributes (occupation, age, income/caste) are sufficiently provided.

Return STRICT JSON matching:
{{
  "extracted_attributes": {{}},
  "assistant_reply": "string",
  "suggested_quick_replies": ["string", "string"],
  "is_ready_to_evaluate": boolean
}}"""

                response = self.client.chat.completions.create(
                    model=config.GROQ_MODEL,
                    messages=[
                        {"role": "system", "content": "You are a specialized government scheme advisor that outputs strict JSON."},
                        {"role": "user", "content": prompt}
                    ],
                    response_format={"type": "json_object"},
                    temperature=0.3,
                    max_tokens=800,
                )
                data = json.loads(response.choices[0].message.content)
                extracted_updates = data.get("extracted_attributes", {})
                assistant_reply = data.get("assistant_reply", "")
                suggested_replies = data.get("suggested_quick_replies", [])
                is_ready_to_evaluate = data.get("is_ready_to_evaluate", False)

            except Exception as e:
                logger.warning(f"Groq conversational extraction error, using rule-based NLP fallback: {e}")

        # Rule-based NLP extraction fallback to guarantee 100% reliability
        text_lower = user_message.lower()

        # Extract Age
        age_match = re.search(r'\b(?:i am |age is |age |i\'m )?(\d{1,2})\s*(?:years?|yrs?|yr)?\s*(?:old)?\b', text_lower)
        if age_match:
            try:
                val = int(age_match.group(1))
                if 10 <= val <= 95 and "age" not in extracted_updates:
                    extracted_updates["age"] = val
            except ValueError:
                pass

        # Extract Gender
        if "female" in text_lower or "woman" in text_lower or "girl" in text_lower or "mother" in text_lower:
            extracted_updates.setdefault("gender", "Female")
        elif "male" in text_lower or " man" in text_lower or "boy" in text_lower or "father" in text_lower:
            extracted_updates.setdefault("gender", "Male")

        # Extract Social Category
        if "sc category" in text_lower or "scheduled caste" in text_lower or "\bsc\b" in text_lower:
            extracted_updates.setdefault("caste", "SC")
        elif "st category" in text_lower or "scheduled tribe" in text_lower or "\bst\b" in text_lower:
            extracted_updates.setdefault("caste", "ST")
        elif "obc" in text_lower or "backward class" in text_lower:
            extracted_updates.setdefault("caste", "OBC")
        elif "ews" in text_lower or "economically weaker" in text_lower:
            extracted_updates.setdefault("caste", "EWS")
        elif "general category" in text_lower or "general" in text_lower:
            extracted_updates.setdefault("caste", "General")

        # Extract Income
        lakh_match = re.search(r'(?:income|earning|salary|make|revenue)?\s*(?:is|of|about|around)?\s*(?:₹|rs\.?|inr)?\s*([0-9.]+)\s*(?:lakhs?|lac|lacs?|l)\b', text_lower)
        if lakh_match:
            try:
                lakh_val = float(lakh_match.group(1)) * 100000
                extracted_updates.setdefault("annual_income", lakh_val)
            except ValueError:
                pass

        # Extract Occupation
        if any(w in text_lower for w in ["student", "studying", "college", "bca", "btech", "bsc", "school", "degree", "exam"]):
            extracted_updates.setdefault("occupation", "Student")
        elif any(w in text_lower for w in ["farmer", "farming", "agriculture", "crop", "dairy", "land", "cultivat"]):
            extracted_updates.setdefault("occupation", "Farmer")
            extracted_updates.setdefault("is_farmer", True)
        elif any(w in text_lower for w in ["business", "entrepreneur", "startup", "shop", "msme", "factory", "store", "company"]):
            extracted_updates.setdefault("occupation", "Entrepreneur")
        elif any(w in text_lower for w in ["vendor", "hawker", "thela", "street vendor", "cart"]):
            extracted_updates.setdefault("occupation", "Street Vendor")
        elif any(w in text_lower for w in ["artisan", "craft", "potter", "weaver", "tailor", "carpenter", "blacksmith"]):
            extracted_updates.setdefault("occupation", "Artisan")
            extracted_updates.setdefault("is_artisan_weaver", True)
        elif any(w in text_lower for w in ["construction", "labour", "worker", "daily wage", "mason"]):
            extracted_updates.setdefault("occupation", "Construction Worker")
            extracted_updates.setdefault("is_construction_worker", True)
            extracted_updates.setdefault("is_unorganised_worker", True)

        # Extract Domain Requirements / Goals (Medical, Solar, Scholarship, Loan, etc.)
        current_interests = list(current_profile.interested_domains or [])

        # 1. Health & Medical
        if any(w in text_lower for w in ["medical", "health", "hospital", "doctor", "treatment", "disease", "illness", "ayushman", "surgery", "medicine", "patient", "clinic", "cure"]):
            if "Health & Medical" not in current_interests:
                current_interests.append("Health & Medical")
            extracted_updates.setdefault("specific_goal", "Medical treatment and healthcare coverage")

        # 2. Education & Scholarships
        if any(w in text_lower for w in ["scholarship", "college fee", "school fee", "tuition", "study loan", "higher education", "fellowship"]):
            if "Education & Scholarships" not in current_interests:
                current_interests.append("Education & Scholarships")
            extracted_updates.setdefault("specific_goal", "Higher education & scholarship support")

        # 3. Environment & Solar Rooftop
        if any(w in text_lower for w in ["solar", "rooftop", "electricity bill", "solar panel", "muft bijli", "sun power"]):
            if "Environment & Sustainability" not in current_interests:
                current_interests.append("Environment & Sustainability")
            extracted_updates.setdefault("has_solar_rooftop_space", True)
            extracted_updates.setdefault("specific_goal", "Rooftop solar subsidy & free electricity")

        # 4. MSME & Business Loans
        if any(w in text_lower for w in ["business loan", "startup fund", "shop loan", "msme grant", "working capital", "pmebg", "mudra", "stand up"]):
            if "MSME, Business & Entrepreneurship" not in current_interests:
                current_interests.append("MSME, Business & Entrepreneurship")
            extracted_updates.setdefault("specific_goal", "Business setup loan & capital subsidy")

        # 5. Agriculture & Farming
        if any(w in text_lower for w in ["crop insurance", "kisan loan", "tractor subsidy", "fertilizer subsidy", "farm equipment", "pm kisan"]):
            if "Agriculture & Allied Activities" not in current_interests:
                current_interests.append("Agriculture & Allied Activities")
            extracted_updates.setdefault("is_farmer", True)
            extracted_updates.setdefault("specific_goal", "Agricultural financial support & crop insurance")

        # 6. Women & Child
        if any(w in text_lower for w in ["daughter", "girl child", "sukanya", "maternity", "pregnant", "lakhpati didi"]):
            if "Women & Child Welfare" not in current_interests:
                current_interests.append("Women & Child Welfare")

        # 7. Housing & Land Allotment
        if any(w in text_lower for w in ["house loan", "housing subsidy", "pmay", "pucca house", "awas yojana", "home construction", "land allotment", "patta", "homestead", "property card", "svamitva", "plot"]):
            if "Housing & Shelter" not in current_interests:
                current_interests.append("Housing & Shelter")
            extracted_updates.setdefault("specific_goal", "Affordable family housing & land title patta allotment")
            if any(w in text_lower for w in ["land", "patta", "plot", "homestead"]):
                extracted_updates.setdefault("beneficiary_type", "Family / Household")

        # 8. Disability
        if any(w in text_lower for w in ["disabled", "disability", "divyang", "tricycle", "wheelchair", "hearing aid", "adip"]):
            if "Disability & Accessibility" not in current_interests:
                current_interests.append("Disability & Accessibility")
            extracted_updates.setdefault("is_differently_abled", True)

        # 9. Senior Citizens
        if any(w in text_lower for w in ["old age pension", "senior citizen", "pension scheme", "elderly"]):
            if "Senior Citizens & Elderly Welfare" not in current_interests:
                current_interests.append("Senior Citizens & Elderly Welfare")

        # 10. Family vs Individual Beneficiary Level
        if any(w in text_lower for w in ["family", "household", "my family", "entire family", "for whole family", "land for family", "house for family"]):
            extracted_updates["beneficiary_type"] = "Family / Household"
        elif any(w in text_lower for w in ["individual", "for myself", "personal scholarship", "personal loan"]):
            extracted_updates["beneficiary_type"] = "Individual"

        # 11. Land Ownership / Landless Status
        if any(w in text_lower for w in ["landless", "no land", "don't have land", "no agricultural land"]):
            extracted_updates["is_landless"] = True
            extracted_updates["owns_agricultural_land"] = False
        elif any(w in text_lower for w in ["own land", "have farmland", "agricultural land", "acres", "farm land"]):
            extracted_updates["owns_agricultural_land"] = True
            extracted_updates["is_landless"] = False

        # 12. Motorized Vehicle Ownership
        if any(w in text_lower for w in ["own a car", "have a car", "own a tractor", "have a 4 wheeler", "4-wheeler"]):
            extracted_updates["owns_motorized_vehicle"] = True
        elif any(w in text_lower for w in ["no car", "no vehicle", "don't have car", "no 4 wheeler"]):
            extracted_updates["owns_motorized_vehicle"] = False

        # 13. Income Tax / ITR Status
        if any(w in text_lower for w in ["income tax payer", "pay income tax", "file itr", "paying tax", "itr filer"]):
            extracted_updates["is_tax_payer"] = True
        elif any(w in text_lower for w in ["non tax payer", "don't pay tax", "no income tax", "itr exempt", "exempt from tax"]):
            extracted_updates["is_tax_payer"] = False

        if current_interests:
            extracted_updates["interested_domains"] = current_interests

        # Specialized Vulnerabilities
        if "pregnant" in text_lower or "expecting" in text_lower or "lactating" in text_lower or "maternity" in text_lower:
            extracted_updates.setdefault("is_pregnant_or_lactating", True)
            extracted_updates.setdefault("gender", "Female")

        if "daughter" in text_lower or "girl child" in text_lower:
            extracted_updates.setdefault("has_girl_child", True)
            gc_age = re.search(r'(?:daughter|girl|child)\s*(?:is|of|age)?\s*(\d{1,2})', text_lower)
            if gc_age:
                extracted_updates.setdefault("girl_child_age", int(gc_age.group(1)))

        if "disabled" in text_lower or "disability" in text_lower or "handicapped" in text_lower or "divyang" in text_lower:
            extracted_updates.setdefault("is_differently_abled", True)

        if "bpl" in text_lower or "ration card" in text_lower or "antyodaya" in text_lower:
            extracted_updates.setdefault("has_bpl_ration_card", True)

        if "rural" in text_lower or "village" in text_lower or "panchayat" in text_lower:
            extracted_updates.setdefault("area_type", "Rural")
        elif "urban" in text_lower or "city" in text_lower or "metro" in text_lower:
            extracted_updates.setdefault("area_type", "Urban")

        # Merge extracted updates into current profile
        updated_dict = current_profile.model_dump()
        for k, v in extracted_updates.items():
            if v is not None:
                updated_dict[k] = v
        new_profile = UserProfile(**updated_dict)


        # Fallback assistant reply if LLM didn't produce one
        if not assistant_reply:
            extracted_keys = list(extracted_updates.keys())
            if extracted_keys:
                items_str = ", ".join([f"{k}: {extracted_updates[k]}" for k in extracted_keys])
                assistant_reply = f"Thank you! I have recorded your details ({items_str}). "
            else:
                assistant_reply = "I understand. "

            # Determine next missing piece
            if new_profile.occupation is None:
                assistant_reply += "What is your primary occupation or current status (e.g. Student, Entrepreneur, Farmer, Artisan, Salaried)?"
                suggested_replies = ["💼 Entrepreneur", "🎓 Student", "🌾 Farmer", "🛒 Street Vendor", "⚒️ Artisan"]
            elif new_profile.annual_income is None:
                assistant_reply += f"To check income caps for scholarships and subsidies, what is your approximate gross Annual Household Income?"
                suggested_replies = ["Under ₹1.5 Lakhs", "₹2.5 Lakhs - ₹4.5 Lakhs", "₹5 Lakhs - ₹8 Lakhs", "Above ₹8 Lakhs"]
            elif new_profile.age is None:
                assistant_reply += "What is your current age?"
                suggested_replies = ["18-25 yrs", "26-35 yrs", "36-50 yrs", "60+ yrs (Senior)"]
            elif new_profile.caste is None:
                assistant_reply += "Which social category do you belong to (General, OBC, SC, ST, or EWS)?"
                suggested_replies = ["General", "OBC", "SC (35% Subsidies)", "ST", "EWS"]
            else:
                assistant_reply += "Great! We have collected key eligibility attributes. You can tell me about specific goals (like Solar panels, Business loan, Maternity, or Higher studies), or click below to evaluate your eligible schemes!"
                suggested_replies = ["🚀 Run Scheme Eligibility Match", "☀️ Tell me about Solar Subsidy", "💼 Business Loan Subsidy", "🎓 Scholarship Schemes"]
                is_ready_to_evaluate = True

        # Check if user explicitly asked for evaluation
        if any(term in text_lower for term in ["evaluate", "check scheme", "show scheme", "my schemes", "qualify", "find scheme", "run match"]):
            is_ready_to_evaluate = True

        return new_profile, assistant_reply, suggested_replies, is_ready_to_evaluate

    def generate_scheme_reasoning(
        self, user: UserProfile, scheme: Scheme, matched_criteria: List[str]
    ) -> MatchReasoning:
        """
        Generates transparent 'Why You Qualify' and benefit summary using Groq LLM or deterministic fallback.
        """
        if self.client:
            try:
                prompt = f"""You are a senior government welfare advisor. Explain why this citizen qualifies for the scheme in simple, encouraging, and clear terms.

Citizen Profile:
- Age: {user.age}
- Gender: {user.gender}
- Social Category: {user.caste}
- Occupation: {user.occupation}
- Annual Household Income: ₹{user.annual_income or 'Not specified'}
- State: {user.state}
- Education: {user.education_level or 'Not specified'}
- Specific Goal: {user.specific_goal or 'Not specified'}
- Business/Project Details: {user.business_type or 'General'} (New Project: {user.is_new_project})

Scheme Details:
- Name: {scheme.name}
- Category: {scheme.category}
- Ministry: {scheme.ministry}
- Benefits: {scheme.max_subsidy_or_loan}
- Matched Rule Criteria: {json.dumps(matched_criteria)}
- Key Scheme Features: {json.dumps(scheme.key_benefits)}

Return ONLY a JSON object matching this exact schema:
{{
  "why_you_qualify": [
    "string: specific point about how citizen's age/income/category matches",
    "string: specific point about how occupation/qualification satisfies scheme rules",
    "string: additional eligibility synergy"
  ],
  "key_benefits_highlight": [
    "string: key financial benefit or subsidy detail",
    "string: training, collateral waiver, or ancillary perk"
  ],
  "action_items": [
    "string: concrete next step to apply",
    "string: key document to prepare"
  ]
}}"""

                response = self.client.chat.completions.create(
                    model=config.GROQ_MODEL,
                    messages=[
                        {"role": "system", "content": "You are a specialized government scheme advisor that returns strict JSON output."},
                        {"role": "user", "content": prompt}
                    ],
                    response_format={"type": "json_object"},
                    temperature=0.2,
                    max_tokens=600,
                )
                content = response.choices[0].message.content
                data = json.loads(content)
                return MatchReasoning(
                    why_you_qualify=data.get("why_you_qualify", matched_criteria),
                    key_benefits_highlight=data.get("key_benefits_highlight", scheme.key_benefits[:2]),
                    action_items=data.get("action_items", ["Gather required identity and category documents", f"Apply directly on official portal: {scheme.apply_link}"]),
                )
            except Exception as e:
                logger.warning(f"Groq API call failed or rate limited, falling back to deterministic reasoning: {e}")

        # Deterministic Rule-Based Fallback Reasoning
        why_list = []
        if matched_criteria:
            why_list.extend(matched_criteria[:4])
        else:
            why_list.append(f"Your profile as a {user.occupation or 'citizen'} satisfies all core eligibility constraints.")

        if user.caste and user.caste in scheme.caste_category:
            why_list.append(f"Your category ({user.caste}) entitles you to full scheme provisions and applicable subsidies.")

        benefits_list = scheme.key_benefits if scheme.key_benefits else [scheme.max_subsidy_or_loan]

        action_list = [
            "Prepare your Aadhaar and proof of bank account.",
            f"Review required documents and submit application on official portal ({scheme.apply_link}).",
        ]

        return MatchReasoning(
            why_you_qualify=why_list,
            key_benefits_highlight=benefits_list,
            action_items=action_list,
        )

    def generate_overall_summary(
        self, user: UserProfile, direct_count: int, near_miss_count: int, top_schemes: List[Scheme]
    ) -> str:
        """
        Generates a 2-sentence executive intake summary insight for the citizen.
        """
        scheme_names = ", ".join([s.name for s in top_schemes[:3]])
        if self.client:
            try:
                prompt = f"""Write an encouraging, professional 2-sentence summary for a citizen profile:
Occupation: {user.occupation}, Caste: {user.caste}, Income: ₹{user.annual_income or 'N/A'}.
Found {direct_count} directly eligible schemes and {near_miss_count} near-miss opportunities.
Top schemes: {scheme_names}. Highlight total financial impact potential."""

                response = self.client.chat.completions.create(
                    model=config.GROQ_MODEL,
                    messages=[
                        {"role": "system", "content": "You are a helpful government welfare advisor. Write concise 2 sentences."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.3,
                    max_tokens=150,
                )
                return response.choices[0].message.content.strip()
            except Exception:
                pass

        if direct_count > 0:
            return f"Great news! Based on your profile ({user.occupation or 'Applicant'}, {user.caste or 'Citizen'}), you qualify for {direct_count} government schemes with high financial assistance like {scheme_names}. Review your personalized document checklist to apply."
        else:
            return f"We identified {near_miss_count} near-miss government schemes. With slight eligibility adjustments (such as category relaxation or income thresholds), you can become eligible for high-impact schemes like {scheme_names}."


# Singleton explainer instance
llm_explainer = LLMExplainer()
