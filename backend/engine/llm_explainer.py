import json
import logging
from typing import List, Dict, Any, Optional
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
            return f"Great news! Based on your {user.occupation or 'applicant'} profile ({user.caste or 'Citizen'}, Age {user.age or 'Eligible'}), you qualify for {direct_count} government schemes with high financial grants and subsidies like {scheme_names}. Review your personalized document checklist to apply immediately."
        else:
            return f"We found {near_miss_count} near-miss government schemes. With minor adjustments (such as category relaxation or income thresholds), you can become eligible for high-impact schemes like {scheme_names}."


# Singleton explainer instance
llm_explainer = LLMExplainer()
