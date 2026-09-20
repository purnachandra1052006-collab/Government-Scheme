from typing import List, Optional, Dict, Any, Literal
from pydantic import BaseModel, Field


class UserProfile(BaseModel):
    age: Optional[int] = Field(None, description="Age in years")
    gender: Optional[str] = Field(None, description="Gender (Male, Female, Other)")
    caste: Optional[str] = Field(None, description="Social Category (General, OBC, SC, ST, EWS)")
    occupation: Optional[str] = Field(
        None,
        description="Current Occupation (Entrepreneur, Student, Farmer, Unemployed, Salaried, Street Vendor, Artisan)",
    )
    annual_income: Optional[float] = Field(None, description="Annual Household Income in INR")
    state: Optional[str] = Field("All India", description="State or Union Territory of Residence")
    education_level: Optional[str] = Field(
        None,
        description="Highest Educational Qualification (Below 8th, 8th Pass, 10th Pass, 12th Pass, Diploma, Graduate, Post Graduate)",
    )
    specific_goal: Optional[str] = Field(
        None,
        description="Primary financial or developmental goal (e.g. Higher Education, Business Setup, Equipment, Housing)",
    )
    business_type: Optional[str] = Field(
        None,
        description="Type of business (Manufacturing, Service, Trading, Tech/Startup, Traditional Craft)",
    )
    funding_required: Optional[float] = Field(None, description="Target funding or loan amount in INR")
    is_new_project: Optional[bool] = Field(
        True,
        description="Whether the business/venture is a new greenfield project or existing unit",
    )
    land_holding_acres: Optional[float] = Field(
        None, description="Agricultural landholding size in acres (if Farmer)"
    )
    owns_pucca_house: Optional[bool] = Field(
        False, description="Whether family already owns a permanent pucca house"
    )
    is_tax_payer: Optional[bool] = Field(
        False, description="Whether the applicant pays income tax"
    )
    marks_percentage: Optional[float] = Field(
        None, description="Academic marks/percentile percentage (if Student)"
    )


class Scheme(BaseModel):
    id: str
    name: str
    category: str
    ministry: str
    target_audience: List[str]
    min_age: Optional[int] = None
    max_age: Optional[int] = None
    max_income: Optional[float] = None
    gender_preference: str = "All"
    caste_category: List[str] = ["General", "OBC", "SC", "ST", "EWS"]
    states_applicable: List[str] = ["All India"]
    max_subsidy_or_loan: str
    financial_benefit_value: float = 0.0
    subsidy_percentage: Optional[str] = None
    description: str
    eligibility_rules: Dict[str, Any] = {}
    key_benefits: List[str] = []
    required_documents: List[str] = []
    apply_link: str


class MatchReasoning(BaseModel):
    why_you_qualify: List[str]
    key_benefits_highlight: List[str]
    action_items: List[str]


class NearMissReasoning(BaseModel):
    failed_criteria: List[str]
    gap_explanation: str
    how_to_qualify: str


class SchemeMatch(BaseModel):
    scheme: Scheme
    match_type: Literal["direct", "near_miss"]
    match_score: float = 0.0
    financial_score: float = 0.0
    total_rank_score: float = 0.0
    reasoning: MatchReasoning
    near_miss_info: Optional[NearMissReasoning] = None


class ConsolidatedDocuments(BaseModel):
    universal_documents: List[str]
    scheme_specific_documents: Dict[str, List[str]]
    total_unique_documents: int


class EvaluationResponse(BaseModel):
    user_profile: UserProfile
    direct_matches: List[SchemeMatch]
    near_miss_matches: List[SchemeMatch]
    total_direct_count: int
    total_near_miss_count: int
    consolidated_documents: ConsolidatedDocuments
    summary_insight: str


class IntakeQuestionOption(BaseModel):
    label: str
    value: Any
    description: Optional[str] = None


class IntakeQuestion(BaseModel):
    id: str
    field: str
    question: str
    helper_text: Optional[str] = None
    input_type: Literal["select", "number", "text", "boolean", "currency"]
    options: Optional[List[IntakeQuestionOption]] = None
    min_val: Optional[float] = None
    max_val: Optional[float] = None
    unit: Optional[str] = None
    step: int
    total_steps: int


class ChatMessage(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str
    question_payload: Optional[IntakeQuestion] = None
    quick_options: Optional[List[str]] = None


class IntakeAnswerPayload(BaseModel):
    session_id: Optional[str] = None
    current_profile: UserProfile
    field: str
    value: Any


class ChatIntakeSession(BaseModel):
    session_id: str
    profile: UserProfile
    history: List[ChatMessage] = []
    current_step: int = 1
    total_steps: int = 7
    is_complete: bool = False
    next_question: Optional[IntakeQuestion] = None
