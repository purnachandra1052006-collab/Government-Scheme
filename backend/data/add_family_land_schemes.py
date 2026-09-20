import json
import os

FAMILY_LAND_SCHEMES = [
    {
        "id": "pmay_gramin_housing",
        "name": "Pradhan Mantri Awas Yojana - Gramin (PMAY-G Housing for All)",
        "category": "Housing & Shelter",
        "domain": "Housing & Shelter",
        "ministry": "Ministry of Rural Development",
        "beneficiary_level": "Family / Household",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Construction Worker", "Fisherman"],
        "target_beneficiaries": ["Houseless families and households living in Kutcha / dilapidated houses in rural India"],
        "min_age": 18,
        "max_age": 100,
        "max_income": 200000,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["All India"],
        "area_applicability": "Rural",
        "central_or_state": "Centrally Sponsored",
        "max_subsidy_or_loan": "₹1,20,000 to ₹1,30,000 direct construction grant + ₹26,000 MGNREGA wages + ₹12,000 SBM toilet aid",
        "financial_benefit_value": 168000,
        "subsidy_percentage": "100% Direct DBT Family Housing Grant",
        "description": "Flagship national rural housing mission providing direct grant of ₹1.20 Lakhs (plain areas) and ₹1.30 Lakhs (hilly/NE states) directly to family bank accounts to construct a minimum 25 sq.m hygienic pucca house.",
        "eligibility_rules": {
            "pucca_house": False,
            "no_four_wheeler": True,
            "not_income_tax_payer": True,
            "requires_house_site_plot": True,
            "max_annual_income": 200000
        },
        "key_benefits": [
            "₹1,20,000 (plains) / ₹1,30,000 (hilly/IAP districts) direct financial assistance in 3 installments",
            "₹26,000 additional wage support for 90-95 person days of un-skilled labour under MGNREGA",
            "₹12,000 dedicated Swachh Bharat Mission grant for toilet construction + free LPG connection via Ujjwala"
        ],
        "required_documents": [
            "Aadhaar Card of all family members",
            "SECC / Awas+ Household Registration Number or Ration Card",
            "Bank Account linked with Aadhaar & Mobile",
            "Geo-tagged photograph of existing Kutcha house / land site"
        ],
        "application_process": "Gram Sabha / Block Development Officer / AwasApp / PMAY-G Portal",
        "apply_link": "https://pmayg.nic.in/",
        "official_source_url": "https://rural.nic.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "svamitva_land_property",
        "name": "SVAMITVA Scheme (Survey & Legal Property Titles for Rural Families)",
        "category": "Rural Development",
        "domain": "Rural Development",
        "ministry": "Ministry of Panchayati Raj",
        "beneficiary_level": "Family / Household",
        "target_audience": ["All", "Farmer", "Artisan", "Unemployed"],
        "target_beneficiaries": ["Rural families owning inhabited residential land (Abadi area) across all Indian villages"],
        "min_age": 18,
        "max_age": 100,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["All India"],
        "area_applicability": "Rural",
        "central_or_state": "Central Government",
        "max_subsidy_or_loan": "Free high-precision drone mapping & official legal 'Property Card' (Sampatti Patra)",
        "financial_benefit_value": 50000,
        "subsidy_percentage": "100% Free Drone Land Title Demarcation",
        "description": "Revolutionary central scheme deploying high-resolution drone mapping to provide village household families with official legal property cards (Ghar Ka Patta), enabling bank loans, property monetization, and zero land disputes.",
        "eligibility_rules": {
            "rural_resident": True
        },
        "key_benefits": [
            "Official digital Property Card (Sampatti Patra) conferring unassailable legal title to village home and land",
            "Enables village families to use residential property as financial asset / collateral for bank loans",
            "Accurate drone demarcation eliminates boundary disputes with centimeter-level GPS precision"
        ],
        "required_documents": [
            "Aadhaar Card of Head of Household",
            "Gram Panchayat tax receipt / Chulha tax / electricity bill",
            "Family Member Details"
        ],
        "application_process": "Survey of India village survey / Gram Panchayat validation",
        "apply_link": "https://svamitva.nic.in/",
        "official_source_url": "https://svamitva.nic.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "pedalandariki_illu_ap",
        "name": "Navaratnalu - Pedalandariki Illu (Free House Site Pattas & Housing AP)",
        "category": "Housing & Shelter",
        "domain": "Housing & Shelter",
        "ministry": "Housing Department, Government of Andhra Pradesh",
        "beneficiary_level": "Family / Household",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Construction Worker"],
        "target_beneficiaries": ["Homeless BPL resident families of Andhra Pradesh (House registered in Woman's name)"],
        "min_age": 18,
        "max_age": 100,
        "max_income": 300000,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Andhra Pradesh"],
        "state_name": "Andhra Pradesh",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "Free house site land patta (1.5 cents rural / 1.0 cent urban) + ₹1,80,000 construction grant",
        "financial_benefit_value": 450000,
        "subsidy_percentage": "100% Free Land Site Patta + Construction Grant",
        "description": "Distributes free registered house site land pattas to over 30 lakh poor families registered exclusively in the woman head's name, plus ₹1.80 Lakhs construction financial aid.",
        "eligibility_rules": {
            "domicile_andhra_pradesh": True,
            "pucca_house": False,
            "no_four_wheeler": True,
            "not_income_tax_payer": True,
            "max_annual_income": 300000
        },
        "key_benefits": [
            "Free registered house site patta (worth ₹2 to ₹5 Lakhs) registered in the female family head's name",
            "₹1,80,000 cash grant for pucca construction with free sand and subsidized cement/steel",
            "Includes piped drinking water, underground drainage, and electricity connection in YSR Jagananna layouts"
        ],
        "required_documents": [
            "Rice Card (BPL Card)",
            "Aadhaar Card of Woman Head & Spouse",
            "Non-possession of pucca house self-declaration"
        ],
        "application_process": "Village / Ward Secretariat (Grama / Ward Sachivalayam)",
        "apply_link": "https://housing.ap.gov.in/",
        "official_source_url": "https://housing.ap.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "mission_basundhara_assam",
        "name": "Mission Basundhara (Land Rights & Homestead Settlement for Landless Families)",
        "category": "Housing & Shelter",
        "domain": "Housing & Shelter",
        "ministry": "Revenue & Disaster Management Department, Government of Assam",
        "beneficiary_level": "Family / Household",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan"],
        "target_beneficiaries": ["Indigenous landless families and non-patta homestead dwellers in Assam"],
        "min_age": 18,
        "max_age": 100,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Assam"],
        "state_name": "Assam",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "Legal settlement of homestead land up to 1 Bigha with periodic permanent patta",
        "financial_benefit_value": 300000,
        "subsidy_percentage": "100% Free / Subsidized Legal Land Title Settlement",
        "description": "Massive mission in Assam converting government khas land and unclassified homestead lands into permanent registered land titles (Periodic Pattas) for indigenous landless families.",
        "eligibility_rules": {
            "domicile_assam": True,
            "requires_landless": True
        },
        "key_benefits": [
            "Converts occupied homestead land into permanent legal land patta (Periodic Patta)",
            "Protects indigenous and landless families from eviction and land tenure insecurity",
            "100% digital transparent application through Sewa Setu / Basundhara portal"
        ],
        "required_documents": [
            "Assam Domicile / Voter Card / Land occupation proof before cut-off date",
            "Aadhaar Card of Family Head",
            "Panchayat / Circle Office NOC"
        ],
        "application_process": "Online (Basundhara / Sewa Setu Portal - Assam)",
        "apply_link": "https://basundhara.assam.gov.in/",
        "official_source_url": "https://landrevenue.assam.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "vasundhara_odisha",
        "name": "Vasundhara Scheme (Free Homestead Land Distribution to Landless - Odisha)",
        "category": "Housing & Shelter",
        "domain": "Housing & Shelter",
        "ministry": "Revenue and Disaster Management Department, Government of Odisha",
        "beneficiary_level": "Family / Household",
        "target_audience": ["All", "Farmer", "Unemployed", "Construction Worker", "Artisan"],
        "target_beneficiaries": ["Rural landless and homeless families in Odisha who do not own homestead land"],
        "min_age": 18,
        "max_age": 100,
        "max_income": 100000,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Odisha"],
        "state_name": "Odisha",
        "area_applicability": "Rural",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "Free 4 Decimals (0.04 Acres) homestead land title + ₹20,000 site development grant",
        "financial_benefit_value": 200000,
        "subsidy_percentage": "100% Free Government Homestead Land Allotment",
        "description": "Distributes 4 decimals of free government homestead land with a permanent registered title (RoR Patta) to every rural homeless and landless family in Odisha.",
        "eligibility_rules": {
            "domicile_odisha": True,
            "requires_landless": True,
            "pucca_house": False,
            "max_annual_income": 100000
        },
        "key_benefits": [
            "Free 4 decimals of registered homestead land in village layout",
            "Joint legal title in the name of husband and wife (or woman head)",
            "Automatic linkage with Biju Pucca Ghar / PMAY housing assistance"
        ],
        "required_documents": [
            "Aadhaar Card of Family Head & Spouse",
            "Ration Card",
            "Certificate of Landlessness from Tahsildar / Revenue Inspector"
        ],
        "application_process": "Tahsil Office / Revenue Inspector Camp / Mo Seva Kendra",
        "apply_link": "https://revenue.odisha.gov.in/",
        "official_source_url": "https://revenue.odisha.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "ashraya_karnataka",
        "name": "Rajiv Gandhi Rural Housing / Ashraya Scheme (Karnataka)",
        "category": "Housing & Shelter",
        "domain": "Housing & Shelter",
        "ministry": "Housing Department, Government of Karnataka",
        "beneficiary_level": "Family / Household",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Construction Worker"],
        "target_beneficiaries": ["Siteless and houseless rural families in Karnataka below poverty line"],
        "min_age": 18,
        "max_age": 100,
        "max_income": 120000,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Karnataka"],
        "state_name": "Karnataka",
        "area_applicability": "Rural",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "Free housing site plot + ₹1,50,000 (General) / ₹1,75,000 (SC/ST) construction grant",
        "financial_benefit_value": 250000,
        "subsidy_percentage": "100% Free Site Allotment & Housing Construction Grant",
        "description": "Karnataka state housing mission providing free residential site allotment and ₹1.5L to ₹1.75L financial subsidy for constructing a permanent pucca house for siteless and houseless rural BPL families.",
        "eligibility_rules": {
            "domicile_karnataka": True,
            "pucca_house": False,
            "not_income_tax_payer": True,
            "no_four_wheeler": True,
            "max_annual_income": 120000
        },
        "key_benefits": [
            "Free residential site allotment in Ashraya village layouts",
            "₹1,50,000 (General/OBC) or ₹1,75,000 (SC/ST) direct financial assistance via DBT",
            "GPS geo-tagged stage-wise digital payments linked with beneficiary Aadhaar"
        ],
        "required_documents": [
            "Karnataka BPL Ration Card",
            "Aadhaar Card of Family Head and Spouse",
            "Income Certificate (<= ₹1.20 Lakhs per annum)",
            "Caste Certificate (if SC/ST)"
        ],
        "application_process": "Grama Panchayat / Seva Sindhu Portal / Ashraya Portal",
        "apply_link": "https://ashraya.karnataka.gov.in/",
        "official_source_url": "https://rghcl.karnataka.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "fra_tribal_land_titles",
        "name": "Forest Rights Act (FRA) Individual & Community Land Titles",
        "category": "Social Justice & Empowerment",
        "domain": "Social Justice & Empowerment",
        "ministry": "Ministry of Tribal Affairs",
        "beneficiary_level": "Family / Household",
        "target_audience": ["Farmer", "Artisan", "Unemployed"],
        "target_beneficiaries": ["Scheduled Tribe families and Other Traditional Forest Dwellers (OTFD) residing on forest land"],
        "min_age": 18,
        "max_age": 100,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["ST", "General", "OBC", "SC", "EWS"],
        "states_applicable": ["All India"],
        "area_applicability": "Rural",
        "central_or_state": "Central Government",
        "max_subsidy_or_loan": "Heritable, legal ownership title/patta over forest cultivable & homestead land up to 4 hectares (10 acres)",
        "financial_benefit_value": 500000,
        "subsidy_percentage": "100% Legal Ownership Title Demarcation",
        "description": "Historic national legislation legally recognizing and vesting heritable ownership land titles/pattas up to 4 hectares for forest-dwelling Scheduled Tribes and traditional forest dwelling families.",
        "eligibility_rules": {
            "forest_dwelling_st_or_otfd": True
        },
        "key_benefits": [
            "Permanent legal land ownership title (Patta) over self-cultivated forest land up to 4 hectares",
            "Joint title registered in the names of husband and wife with full heritable rights",
            "Entitles family to government farm subsidies, crop insurance, PM-KISAN, and irrigation borewells"
        ],
        "required_documents": [
            "ST Certificate (or proof of 75-year/3-generation forest dwelling for OTFD)",
            "Aadhaar Card of Family Head and Spouse",
            "Gram Sabha / Forest Rights Committee (FRC) resolution"
        ],
        "application_process": "Gram Sabha / Forest Rights Committee / Sub-Divisional Level Committee (SDLC)",
        "apply_link": "https://tribal.nic.in/",
        "official_source_url": "https://tribal.nic.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    }
]

# Load current schemes and update beneficiary_level on all schemes
db_path = os.path.join(os.path.dirname(__file__), "schemes_db.json")
with open(db_path, "r", encoding="utf-8") as f:
    schemes = json.load(f)

# Mark family schemes based on domain / keywords
FAMILY_KEYWORDS = [
    "health insurance", "jan arogya", "aarogyasri", "swasthya", "chiranjeevi",
    "ration", "anna yojana", "awas", "housing", "pucca house", "property card",
    "svamitva", "patta", "land", "homestead", "ujjwala", "gruha lakshmi",
    "ladki bahin", "ladli behna", "mahtari", "maiyan", "orunodoi", "griha aadhar",
    "surya ghar", "solar"
]

for s in schemes:
    s_name = s.get("name", "").lower()
    s_desc = s.get("description", "").lower()
    s_cat = s.get("category", "").lower()
    
    # Check if already has beneficiary_level
    if "beneficiary_level" not in s:
        is_family = False
        if any(kw in s_name or kw in s_desc for kw in FAMILY_KEYWORDS):
            is_family = True
        elif s_cat in ["housing & shelter", "water, sanitation & utilities", "food, nutrition & basic needs"]:
            is_family = True
            
        s["beneficiary_level"] = "Family / Household" if is_family else "Individual"

# Add the new family land & housing schemes
existing_ids = {s["id"] for s in schemes}
added = 0
for fs in FAMILY_LAND_SCHEMES:
    if fs["id"] not in existing_ids:
        schemes.append(fs)
        added += 1

with open(db_path, "w", encoding="utf-8") as f:
    json.dump(schemes, f, indent=2, ensure_ascii=False)

print(f"Updated all schemes with beneficiary_level and added {added} Family Land & Housing schemes! Total schemes: {len(schemes)}")
