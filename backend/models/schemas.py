from typing import List, Optional, Dict, Any, Literal
from pydantic import BaseModel, Field

# 24 Major Indian Scheme Domains
SCHEME_DOMAINS = [
    "Education & Scholarships",
    "Health & Medical",
    "Housing & Shelter",
    "Banking, Finance & Insurance",
    "Women & Child Welfare",
    "Agriculture & Allied Activities",
    "MSME, Business & Entrepreneurship",
    "Employment & Skill Development",
    "Disability & Accessibility",
    "Senior Citizens & Elderly Welfare",
    "Social Justice & Empowerment",
    "Rural Development",
    "Urban Development",
    "Science, Technology & Digital",
    "Sports & Youth",
    "Arts, Culture & Heritage",
    "Environment & Sustainability",
    "Water, Sanitation & Utilities",
    "Transport & Mobility",
    "Fisheries & Coastal Livelihoods",
    "Handloom, Handicrafts & Traditional Industries",
    "Construction & Unorganised Workers",
    "Tourism & Hospitality",
    "Food, Nutrition & Basic Needs",
]


class UserProfile(BaseModel):
    # Core Demographics
    age: Optional[int] = Field(None, description="Age in years")
    gender: Optional[str] = Field(None, description="Gender (Male, Female, Other)")
    caste: Optional[str] = Field(None, description="Social Category (General, OBC, SC, ST, EWS)")
    state: Optional[str] = Field("All India", description="State or Union Territory of Residence")
    district: Optional[str] = Field(None, description="District of Residence")
    area_type: Optional[str] = Field("All", description="Area type (Rural, Urban, Semi-Urban)")
    marital_status: Optional[str] = Field(None, description="Marital Status (Single, Married, Widowed, Divorced)")

    # Occupation & Employment
    occupation: Optional[str] = Field(
        None,
        description="Current Primary Occupation (Entrepreneur, Student, Farmer, Unemployed, Salaried, Street Vendor, Artisan, Construction Worker, Fisherman, Weaver, Healthcare/Asha, Domestic Worker)",
    )
    employment_status: Optional[str] = Field(None, description="Employment Status (Employed, Self-Employed, Unemployed, Student, Retired)")
    education_level: Optional[str] = Field(
        None,
        description="Highest Educational Qualification (Below 8th, 8th Pass, 10th Pass, 12th Pass, Diploma, Graduate, Post Graduate, Doctorate)",
    )
    specific_goal: Optional[str] = Field(
        None,
        description="Primary goal (e.g. Higher Education, Business Loan, Housing, Health Cover, Solar Subsidy, Pension, Farm Equipment)",
    )

    # Economic & Household
    annual_income: Optional[float] = Field(None, description="Annual Gross Household Income in INR")
    has_bpl_ration_card: Optional[bool] = Field(False, description="Whether family holds BPL / Antyodaya / Ration Card")
    owns_pucca_house: Optional[bool] = Field(False, description="Whether family already owns a permanent pucca house")
    is_tax_payer: Optional[bool] = Field(False, description="Whether applicant or spouse pays Income Tax")

    # Business / MSME (If Entrepreneur / Artisan)
    business_type: Optional[str] = Field(None, description="Business Sector (Manufacturing, Service, Trading, Tech/Startup, Traditional Craft, Handloom)")
    funding_required: Optional[float] = Field(None, description="Target funding/loan amount in INR")
    is_new_project: Optional[bool] = Field(True, description="Whether venture is a new greenfield project")

    # Agriculture & Allied (If Farmer / Fisherfolk)
    land_holding_acres: Optional[float] = Field(None, description="Agricultural landholding size in acres")
    is_farmer: Optional[bool] = Field(False, description="Whether engaged in farming / agriculture")
    is_fisherfolk: Optional[bool] = Field(False, description="Whether engaged in inland/marine fisheries")

    # Vulnerability & Special Criteria
    is_differently_abled: Optional[bool] = Field(False, description="Whether person has benchmark disability (Divyangjan)")
    disability_percentage: Optional[float] = Field(None, description="Disability percentage if applicable (e.g. 40%+)")
    is_pregnant_or_lactating: Optional[bool] = Field(False, description="Whether applicant is pregnant or lactating mother")
    has_girl_child: Optional[bool] = Field(False, description="Whether applicant has a girl child")
    girl_child_age: Optional[int] = Field(None, description="Age of the girl child in years (e.g. < 10 yrs for Sukanya)")
    is_unorganised_worker: Optional[bool] = Field(False, description="Registered on e-Shram / Unorganised sector worker")
    is_construction_worker: Optional[bool] = Field(False, description="Registered under BOCW / Construction worker")
    is_artisan_weaver: Optional[bool] = Field(False, description="Traditional artisan, weaver, or craftsman")
    has_solar_rooftop_space: Optional[bool] = Field(False, description="Has roof space available for solar panel installation")
    is_sportsperson: Optional[bool] = Field(False, description="State/National level athlete or sportsperson")
    is_ex_serviceman: Optional[bool] = Field(False, description="Ex-serviceman or defense veteran/widow")
    marks_percentage: Optional[float] = Field(None, description="Academic marks percentage if Student")

    # Domain Filtering
    interested_domains: Optional[List[str]] = Field(None, description="Optional target scheme domains of user interest")


class Scheme(BaseModel):
    id: str
    name: str
    category: str = Field(..., description="Primary domain / category")
    domain: Optional[str] = None
    ministry: str
    target_audience: List[str] = []
    target_beneficiaries: List[str] = []
    min_age: Optional[int] = None
    max_age: Optional[int] = None
    max_income: Optional[float] = None
    gender_preference: str = "All"
    caste_category: List[str] = ["General", "OBC", "SC", "ST", "EWS"]
    states_applicable: List[str] = ["All India"]
    area_applicability: str = "All"  # All, Rural, Urban
    central_or_state: str = "Central Government"
    max_subsidy_or_loan: str
    financial_benefit_value: float = 0.0
    subsidy_percentage: Optional[str] = None
    description: str
    eligibility_rules: Dict[str, Any] = {}
    key_benefits: List[str] = []
    required_documents: List[str] = []
    application_process: str = "Online (Portal)"
    apply_link: str
    official_source_url: Optional[str] = None
    last_verified_date: Optional[str] = "2026-09"
    scheme_status: str = "Active"


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
    match_type: Literal["direct", "near_miss", "potential"]
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
    user_message: Optional[str] = None
    field: Optional[str] = None
    value: Optional[Any] = None


class ChatIntakeSession(BaseModel):
    session_id: str
    profile: UserProfile
    history: List[ChatMessage] = []
    current_step: int = 1
    total_steps: int = 7
    is_complete: bool = False
    is_ready_to_evaluate: bool = False
    suggested_quick_replies: Optional[List[str]] = None
    next_question: Optional[IntakeQuestion] = None

