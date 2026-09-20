import json
import os
from typing import List, Dict, Any, Tuple, Optional
from backend.models.schemas import UserProfile, Scheme

QUALIFICATION_RANKS = {
    "none": 0,
    "below 8th": 1,
    "8th pass": 2,
    "10th pass": 3,
    "12th pass": 4,
    "diploma": 5,
    "graduate": 6,
    "post graduate": 7,
    "doctorate": 8,
}


def get_qualification_rank(qual_str: Optional[str]) -> int:
    if not qual_str:
        return 0
    norm = qual_str.strip().lower()
    for key, rank in QUALIFICATION_RANKS.items():
        if key in norm:
            return rank
    return 0


def load_schemes_db(db_path: Optional[str] = None) -> List[Scheme]:
    if db_path is None:
        db_path = os.path.join(os.path.dirname(__file__), "..", "data", "schemes_db.json")
    with open(db_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Scheme(**item) for item in data]


class RuleEngine:
    def __init__(self, schemes: Optional[List[Scheme]] = None):
        self.schemes = schemes if schemes is not None else load_schemes_db()

    def evaluate_scheme(self, user: UserProfile, scheme: Scheme) -> Tuple[bool, List[str], List[str]]:
        """
        Evaluates a scheme against a user profile using multi-attribute decoupled criteria.
        Returns:
            is_direct_match (bool): True if satisfies all mandatory hard criteria
            matched_criteria (List[str]): List of criteria user satisfied
            failed_criteria (List[str]): List of criteria user failed
        """
        matched: List[str] = []
        failed: List[str] = []
        rules = scheme.eligibility_rules or {}

        # 1. Target Audience / Occupation check (Decoupled: 'All' allows any citizen)
        if scheme.target_audience and user.occupation:
            target_list = [aud.lower() for aud in scheme.target_audience]
            user_occ = user.occupation.lower()
            if "all" in target_list or user_occ in target_list:
                matched.append(f"Occupation matches eligible group ({user.occupation})")
            else:
                # Check if user has specific status matching the scheme
                matches_status = False
                if "farmer" in target_list and (user.is_farmer or user_occ == "farmer"):
                    matches_status = True
                elif "unemployed" in target_list and (user.employment_status == "Unemployed" or user_occ == "unemployed"):
                    matches_status = True
                elif "artisan" in target_list and (user.is_artisan_weaver or user_occ in ["artisan", "weaver"]):
                    matches_status = True
                elif "construction worker" in target_list and (user.is_construction_worker or user_occ == "construction worker"):
                    matches_status = True
                elif "fisherman" in target_list and (user.is_fisherfolk or user_occ == "fisherman"):
                    matches_status = True

                if matches_status:
                    matched.append(f"Specialized vocational status satisfied ({user.occupation})")
                else:
                    failed.append(
                        f"Target audience requires {', '.join(scheme.target_audience)}, but user is {user.occupation}"
                    )

        # 2. Age limit check
        if user.age is not None:
            age_ok = True
            if scheme.min_age is not None and user.age < scheme.min_age:
                age_ok = False
                failed.append(f"Minimum age required is {scheme.min_age} years (user is {user.age})")
            if scheme.max_age is not None and user.age > scheme.max_age:
                age_ok = False
                failed.append(f"Maximum age limit is {scheme.max_age} years (user is {user.age})")
            if age_ok:
                matched.append(f"Age {user.age} falls within eligible bracket ({scheme.min_age or 0} - {scheme.max_age or 'No limit'} yrs)")

        # 3. Income check
        if user.annual_income is not None:
            if scheme.max_income is not None:
                if user.annual_income <= scheme.max_income:
                    matched.append(
                        f"Annual income ₹{user.annual_income:,.0f} is within ceiling limit of ₹{scheme.max_income:,.0f}"
                    )
                else:
                    failed.append(
                        f"Annual income ₹{user.annual_income:,.0f} exceeds maximum ceiling of ₹{scheme.max_income:,.0f}"
                    )
            else:
                matched.append("No maximum household income cap specified for this scheme")

        # 4. Gender preference check
        if user.gender and scheme.gender_preference:
            pref = scheme.gender_preference.lower()
            user_gen = user.gender.lower()
            user_caste = (user.caste or "").lower()

            if pref == "all":
                matched.append("Open to all genders")
            elif "female or sc/st male" in pref:
                if user_gen == "female" or user_caste in ["sc", "st"]:
                    matched.append(f"Satisfies demographic mandate ({user.gender} / {user.caste})")
                else:
                    failed.append("Targeted exclusively for Women entrepreneurs or SC/ST Male entrepreneurs")
            elif pref == user_gen:
                matched.append(f"Gender requirement met ({user.gender})")
            else:
                failed.append(f"Requires gender {scheme.gender_preference} (user is {user.gender})")

        # 5. Social Category (Caste) check
        if user.caste and scheme.caste_category:
            scheme_castes = [c.lower() for c in scheme.caste_category]
            if user.caste.lower() in scheme_castes:
                matched.append(f"Social category '{user.caste}' is eligible")
            else:
                failed.append(f"Category '{user.caste}' not eligible. Applicable: {', '.join(scheme.caste_category)}")

        # 6. State / Location check
        if user.state and scheme.states_applicable:
            scheme_states = [s.lower() for s in scheme.states_applicable]
            if "all india" in scheme_states or user.state.lower() in scheme_states:
                matched.append(f"Applicable in your state ({user.state})")
            else:
                failed.append(f"Not applicable in {user.state}. Applicable states: {', '.join(scheme.states_applicable)}")

        # 7. Area Applicability (Rural / Urban)
        if scheme.area_applicability and scheme.area_applicability != "All" and user.area_type and user.area_type != "All":
            if scheme.area_applicability.lower() == user.area_type.lower():
                matched.append(f"Area criterion satisfied ({user.area_type} resident)")
            else:
                failed.append(f"Scheme is designated strictly for {scheme.area_applicability} areas (user is in {user.area_type})")

        # 8. Disability / Divyangjan Requirement
        if rules.get("is_differently_abled") is True:
            if user.is_differently_abled:
                min_pct = rules.get("min_disability_percentage", 40)
                if user.disability_percentage is None or user.disability_percentage >= min_pct:
                    matched.append(f"Benchmark disability requirement satisfied ({user.disability_percentage or min_pct}%+)")
                else:
                    failed.append(f"Requires minimum benchmark disability of {min_pct}% (user has {user.disability_percentage}%)")
            else:
                failed.append("Scheme is reserved exclusively for Persons with Benchmark Disabilities (Divyangjan)")

        # 9. Pregnancy / Maternity Requirement (PMMVY)
        if rules.get("pregnancy_or_lactating") is True:
            if user.is_pregnant_or_lactating:
                matched.append("Pregnant / Lactating mother status verified")
            else:
                failed.append("Scheme is reserved exclusively for Pregnant Women and Lactating Mothers")

        # 10. Girl Child Criteria (Sukanya Samriddhi)
        if rules.get("has_girl_child") is True:
            if user.has_girl_child:
                max_age = rules.get("girl_child_max_age", 10)
                if user.girl_child_age is None or user.girl_child_age <= max_age:
                    matched.append(f"Parent/guardian of girl child under {max_age} years verified")
                else:
                    failed.append(f"Girl child must be 10 years or younger (child is {user.girl_child_age} yrs)")
            else:
                failed.append("Scheme requires having a girl child under 10 years of age")

        # 11. Unorganised Worker (PM-SYM / e-Shram)
        if rules.get("unorganised_worker") is True:
            if user.is_unorganised_worker or user.occupation in ["Street Vendor", "Artisan", "Construction Worker", "Farmer", "Unemployed"]:
                matched.append("Unorganised sector worker status satisfied")
            else:
                failed.append("Scheme is reserved for unorganised workers not covered by formal EPFO/ESIC/NPS")

        # 12. Greenfield / New Project requirement
        if rules.get("new_project_only") is True:
            if user.is_new_project is False:
                failed.append("Scheme is reserved strictly for new (greenfield) business setups, not existing unit expansion")
            else:
                matched.append("Applicant is setting up a new venture (greenfield project)")

        # 13. Pucca house restriction for Housing Schemes
        if "pucca_house" in rules:
            if user.owns_pucca_house is True:
                failed.append("Family already owns a permanent pucca house; scheme is reserved for homeless or kutcha house residents")
            else:
                matched.append("Applicant / Family does not own a pucca house")

        # 14. Income Tax Payer restriction (PM-KISAN, PM-SYM)
        if rules.get("income_tax_payer") is False or rules.get("not_income_tax_payer") is True:
            if user.is_tax_payer is True:
                failed.append("Income tax paying individuals/families are excluded from this benefit")
            else:
                matched.append("Non-taxpayer eligibility criterion satisfied")

        # 15. Min Educational Qualification check
        min_qual_text = rules.get("min_qualification", "")
        if min_qual_text and "8th" in min_qual_text:
            req_rank = QUALIFICATION_RANKS["8th pass"]
            user_rank = get_qualification_rank(user.education_level)
            if user_rank >= req_rank:
                matched.append(f"Educational qualification ({user.education_level or 'Satisfied'}) meets requirement (8th Pass+)")
            elif user.education_level:
                if user.funding_required and user.funding_required <= 1000000:
                    matched.append("Project funding <= ₹10L waives minimum 8th pass requirement")
                else:
                    failed.append("Requires at least 8th Pass for projects above ₹10L")

        if min_qual_text and "10th" in min_qual_text:
            req_rank = QUALIFICATION_RANKS["10th pass"]
            user_rank = get_qualification_rank(user.education_level)
            if user_rank >= req_rank:
                matched.append(f"Educational qualification ({user.education_level}) satisfies 10th Pass minimum")
            elif user.education_level:
                failed.append("Requires at least 10th Pass (Matriculation)")

        if min_qual_text and "12th" in min_qual_text:
            req_rank = QUALIFICATION_RANKS["12th pass"]
            user_rank = get_qualification_rank(user.education_level)
            if user_rank >= req_rank:
                matched.append(f"Educational qualification ({user.education_level}) satisfies 12th Pass minimum")
            elif user.education_level:
                failed.append("Requires at least 12th Pass (Higher Secondary)")

        is_direct = (len(failed) == 0)
        return is_direct, matched, failed
