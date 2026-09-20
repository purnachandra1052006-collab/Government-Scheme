import json
import os

ALL_NEW_STATE_SCHEMES = [
    # ==================== GUJARAT ====================
    {
        "id": "maa_yojana_gujarat",
        "name": "Mukhyamantri Amrutam (MA / MAA Vatsalya) Yojana (Gujarat)",
        "category": "Health & Medical",
        "domain": "Health & Medical",
        "ministry": "Health and Family Welfare Department, Government of Gujarat",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Salaried", "Construction Worker", "Street Vendor"],
        "target_beneficiaries": ["BPL and Lower Middle Class Families of Gujarat with income <= ₹4 Lakhs"],
        "min_age": 0,
        "max_age": 100,
        "max_income": 400000,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Gujarat"],
        "state_name": "Gujarat",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹5,00,000 cashless health insurance coverage per family per year",
        "financial_benefit_value": 500000,
        "subsidy_percentage": "100% Free Government Cashless Hospitalization",
        "description": "Provides ₹5 Lakhs annual cashless medical coverage for catastrophic illnesses, cardiology, oncology, neurosurgery, burns, and pediatric surgeries in Gujarat.",
        "eligibility_rules": {
            "domicile_gujarat": True,
            "max_annual_income": 400000
        },
        "key_benefits": [
            "₹5,00,000 cashless tertiary medical coverage per family per year",
            "Covers 1,700+ procedures across public and private empanelled hospitals",
            "Includes ₹300 transportation allowance per hospital visit"
        ],
        "required_documents": [
            "Aadhaar Card",
            "Gujarat Income Certificate (<= ₹4 Lakhs) or BPL / NFSA Ration Card",
            "Family Photo & Doctor Referral"
        ],
        "application_process": "Taluka Civic Center / District Hospital MA Kiosk / E-Gram Center",
        "apply_link": "https://magujarat.gujarat.gov.in/",
        "official_source_url": "https://magujarat.gujarat.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "mysy_gujarat",
        "name": "Mukhyamantri Yuva Swavalamban Yojana (MYSY Gujarat)",
        "category": "Education & Scholarships",
        "domain": "Education & Scholarships",
        "ministry": "Education Department, Government of Gujarat",
        "target_audience": ["Student"],
        "target_beneficiaries": ["Meritorious Gujarat students pursuing Medical, Engineering, Diploma, Degree courses"],
        "min_age": 16,
        "max_age": 26,
        "max_income": 600000,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Gujarat"],
        "state_name": "Gujarat",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "Tuition fee assistance up to ₹2,00,000/yr + ₹12,000/yr hostel + ₹10,000 book grant",
        "financial_benefit_value": 222000,
        "subsidy_percentage": "50% Tuition Fee Subsidy (Up to ₹2L/year)",
        "description": "Empowers meritorious higher education students in Gujarat whose family income is under ₹6 Lakhs by covering 50% tuition fees, hostel boarding, and book allowances.",
        "eligibility_rules": {
            "domicile_gujarat": True,
            "min_qualification": "10th Pass",
            "max_annual_income": 600000,
            "min_percentage_board": 80
        },
        "key_benefits": [
            "Up to ₹2,00,000/year for MBBS/Dental, ₹50,000/year for Engineering/Pharmacy, ₹25,000 for Diploma",
            "₹1,200/month (₹12,000/year) hostel & food assistance for outstation students",
            "One-time ₹10,000 instrument & book purchase assistance"
        ],
        "required_documents": [
            "10th / 12th Board Marksheet with 80+ percentile",
            "Gujarat Domicile / Income Certificate (<= ₹6 Lakhs)",
            "College Admission Allotment Letter & Fee Receipt",
            "Student Aadhaar Card & Bank Account"
        ],
        "application_process": "Online (MYSY Gujarat Portal)",
        "apply_link": "https://mysy.guj.nic.in/",
        "official_source_url": "https://mysy.guj.nic.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "kisan_sahay_gujarat",
        "name": "Mukhyamantri Kisan Sahay Yojana (Gujarat)",
        "category": "Agriculture & Allied Activities",
        "domain": "Agriculture & Allied Activities",
        "ministry": "Agriculture, Farmers Welfare & Co-operation Department, Gujarat",
        "target_audience": ["Farmer"],
        "target_beneficiaries": ["All landholding farmers registered in 8-A and 7/12 land records in Gujarat"],
        "min_age": 18,
        "max_age": 100,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Gujarat"],
        "state_name": "Gujarat",
        "area_applicability": "Rural",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹20,000 to ₹25,000 per hectare direct disaster crop compensation",
        "financial_benefit_value": 50000,
        "subsidy_percentage": "100% Zero-Premium State Funded Crop Disaster Protection",
        "description": "Comprehensive zero-premium crop compensation scheme protecting 56 lakh Gujarat farmers against drought, unseasonal rainfall, and excess precipitation.",
        "eligibility_rules": {
            "domicile_gujarat": True,
            "is_farmer": True,
            "owns_agricultural_land": True
        },
        "key_benefits": [
            "Zero insurance premium required from farmers (100% State borne)",
            "₹20,000/hectare for 33% to 60% crop damage; ₹25,000/hectare for >60% damage (up to 4 hectares)",
            "Direct digital bank transfer within 15 days of disaster assessment"
        ],
        "required_documents": [
            "7/12, 8-A Land Record extract",
            "Aadhaar Card",
            "Bank Passbook (Aadhaar linked)"
        ],
        "application_process": "Online (E-Gram Center / Kisan Sahay Portal)",
        "apply_link": "https://ikhedut.gujarat.gov.in/",
        "official_source_url": "https://agri.gujarat.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # ==================== KERALA ====================
    {
        "id": "kasp_kerala",
        "name": "Karunya Arogya Suraksha Padhathi (KASP - Kerala)",
        "category": "Health & Medical",
        "domain": "Health & Medical",
        "ministry": "Health and Family Welfare Department, Government of Kerala",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Salaried", "Construction Worker", "Fisherman"],
        "target_beneficiaries": ["Over 42 Lakh low-income & vulnerable families of Kerala"],
        "min_age": 0,
        "max_age": 100,
        "max_income": 300000,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Kerala"],
        "state_name": "Kerala",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹5,00,000 cashless hospitalization coverage per family per year",
        "financial_benefit_value": 500000,
        "subsidy_percentage": "100% Free Government Cashless Care",
        "description": "Kerala's integrated health assurance scheme providing ₹5 Lakhs per family per year for secondary and tertiary hospital treatment in 600+ empaneled hospitals.",
        "eligibility_rules": {
            "domicile_kerala": True,
            "max_annual_income": 300000
        },
        "key_benefits": [
            "₹5,00,000 cashless health insurance cover per family per year",
            "Covers 1,574 medical packages including cardiac, kidney dialysis, and oncology",
            "Paperless admission through KASP helpdesks in all major govt and private hospitals"
        ],
        "required_documents": [
            "Aadhaar Card",
            "Kerala Ration Card (Pink / Yellow / Blue)",
            "Income Certificate or KASP Card"
        ],
        "application_process": "Akshaya Centers / Empanelled Hospital KASP Kiosk",
        "apply_link": "https://sha.kerala.gov.in/",
        "official_source_url": "https://sha.kerala.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "auegs_kerala",
        "name": "Ayyankali Urban Employment Guarantee Scheme (AUEGS Kerala)",
        "category": "Employment & Skill Development",
        "domain": "Employment & Skill Development",
        "ministry": "Local Self Government Department, Government of Kerala",
        "target_audience": ["Unemployed", "Construction Worker", "Street Vendor", "Artisan"],
        "target_beneficiaries": ["Urban poor, manual laborers, and unemployed adults in Kerala municipalities"],
        "min_age": 18,
        "max_age": 65,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Kerala"],
        "state_name": "Kerala",
        "area_applicability": "Urban",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "100 days guaranteed wage employment at statutory state daily wage (₹340/day)",
        "financial_benefit_value": 34000,
        "subsidy_percentage": "100% Guaranteed Urban Wage Employment",
        "description": "First-of-its-kind urban employment guarantee in India offering 100 days of guaranteed manual wage work to adult members of urban households in Kerala.",
        "eligibility_rules": {
            "domicile_kerala": True,
            "min_age": 18,
            "max_age": 65,
            "urban_resident": True
        },
        "key_benefits": [
            "100 days of guaranteed manual wage employment per household per year",
            "Statutory minimum wage credited directly into beneficiary's bank account weekly",
            "Enhances urban civic amenities, tree planting, flood canal cleaning, and green works"
        ],
        "required_documents": [
            "Aadhaar Card",
            "Urban Local Body / Municipality Residence Proof",
            "AUEGS Job Card / Bank Account Details"
        ],
        "application_process": "Respective Urban Municipal Corporation / Municipality Office",
        "apply_link": "https://lsgkerala.gov.in/",
        "official_source_url": "https://lsgkerala.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # ==================== PUNJAB ====================
    {
        "id": "sehat_bima_punjab",
        "name": "Ayushman Bharat Mukh Mantri Sehat Bima Yojana (Punjab)",
        "category": "Health & Medical",
        "domain": "Health & Medical",
        "ministry": "Department of Health & Family Welfare, Government of Punjab",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Salaried", "Construction Worker"],
        "target_beneficiaries": ["Over 45 Lakh families in Punjab including NFSA card holders, J-Form farmers, small traders, accredited journalists, and construction workers"],
        "min_age": 0,
        "max_age": 100,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Punjab"],
        "state_name": "Punjab",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹5,00,000 cashless health insurance cover per family per year",
        "financial_benefit_value": 500000,
        "subsidy_percentage": "100% Cashless Hospital Care",
        "description": "Flagship health protection scheme of Punjab covering 80% of the state's population with ₹5 Lakhs cashless treatment across 900+ empanelled hospitals.",
        "eligibility_rules": {
            "domicile_punjab": True
        },
        "key_benefits": [
            "₹5,00,000 per family per year cashless treatment",
            "Covers 1,579 medical and surgical treatments including daycare surgeries and knee replacements",
            "Extends to Mandi Board J-form farmers, excise registered traders, and BOCW workers"
        ],
        "required_documents": [
            "Aadhaar Card",
            "Punjab Smart Ration Card / J-Form / BOCW Registration Card",
            "Mobile Number for e-KYC"
        ],
        "application_process": "Sewa Kendra / Empanelled Hospital Helpdesk / SHA Punjab Portal",
        "apply_link": "https://sha.punjab.gov.in/",
        "official_source_url": "https://sha.punjab.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "ashirwad_punjab",
        "name": "Ashirwad Scheme (Shagun Yojana Punjab)",
        "category": "Social Justice & Empowerment",
        "domain": "Social Justice & Empowerment",
        "ministry": "Department of Social Justice, Empowerment and Minorities, Punjab",
        "target_audience": ["All", "Unemployed", "Farmer", "Artisan", "Construction Worker"],
        "target_beneficiaries": ["Daughters of SC/BC/EWS and Christian/Muslim low-income families in Punjab"],
        "min_age": 18,
        "max_age": 40,
        "max_income": 32790,
        "gender_preference": "Female",
        "caste_category": ["SC", "OBC", "EWS", "General"],
        "states_applicable": ["Punjab"],
        "state_name": "Punjab",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹51,000 one-time direct bank financial grant on marriage",
        "financial_benefit_value": 51000,
        "subsidy_percentage": "100% State Financial Marriage Grant",
        "description": "Provides ₹51,000 one-time financial assistance directly into the bank account of low-income parents in Punjab on the marriage of their daughter aged 18+.",
        "eligibility_rules": {
            "domicile_punjab": True,
            "min_age": 18,
            "max_annual_income": 32790,
            "marriage_assistance": True
        },
        "key_benefits": [
            "₹51,000 direct bank transfer before or on the marriage ceremony",
            "Covers up to two daughters per family",
            "Relieves debt burden of wedding expenses for underprivileged families"
        ],
        "required_documents": [
            "Punjab Domicile Certificate",
            "Aadhaar Card of Bride and Groom",
            "Age Proof of Bride (18+ years)",
            "Income Certificate (Annual family income <= ₹32,790)"
        ],
        "application_process": "Online (Sewa Kendra / Dr. Ambedkar Portal Punjab)",
        "apply_link": "https://punjabx.gov.in/",
        "official_source_url": "https://punjab.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # ==================== HARYANA ====================
    {
        "id": "chirayu_haryana",
        "name": "Chirayu Haryana Health Scheme (Ayushman Bharat Expansion)",
        "category": "Health & Medical",
        "domain": "Health & Medical",
        "ministry": "Health and Family Welfare Department, Government of Haryana",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Salaried", "Construction Worker"],
        "target_beneficiaries": ["Resident families of Haryana with verified Parivar Pehchan Patra (PPP) income up to ₹3 Lakhs"],
        "min_age": 0,
        "max_age": 100,
        "max_income": 300000,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Haryana"],
        "state_name": "Haryana",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹5,00,000 cashless health insurance cover per family per year",
        "financial_benefit_value": 500000,
        "subsidy_percentage": "100% Free Cashless Hospital Treatment",
        "description": "Haryana's expanded universal healthcare program utilizing Family ID (PPP) data to extend ₹5 Lakhs cashless health coverage to all families with annual income up to ₹3 Lakhs.",
        "eligibility_rules": {
            "domicile_haryana": True,
            "has_parivar_pehchan_patra": True,
            "max_annual_income": 300000
        },
        "key_benefits": [
            "₹5,00,000 cashless secondary and tertiary hospitalization cover per family",
            "Automatic enrollment via Parivar Pehchan Patra (PPP) verified income data",
            "Covers 1,500+ treatments across 715+ empanelled government and private hospitals"
        ],
        "required_documents": [
            "Parivar Pehchan Patra (PPP - Haryana Family ID)",
            "Aadhaar Card",
            "Active Mobile Number"
        ],
        "application_process": "Online (Chirayu / PPP Portal) / SARAL Kendra / Empanelled Hospitals",
        "apply_link": "https://chirayuayushmanharyana.in/",
        "official_source_url": "https://haryanahealth.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "mmpsy_haryana",
        "name": "Mukhyamantri Parivar Samriddhi Yojana (MMPSY Haryana)",
        "category": "Banking, Finance & Insurance",
        "domain": "Banking, Finance & Insurance",
        "ministry": "Finance Department, Government of Haryana",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Construction Worker"],
        "target_beneficiaries": ["Families in Haryana with income up to ₹1.80 Lakhs and landholding up to 5 acres"],
        "min_age": 18,
        "max_age": 60,
        "max_income": 180000,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Haryana"],
        "state_name": "Haryana",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹6,000 per year financial social security assistance & insurance premium reimbursement",
        "financial_benefit_value": 6000,
        "subsidy_percentage": "100% State Social Security & Pension Coverage",
        "description": "Provides ₹6,000 per year financial assistance to low-income Haryana families and fully pays premiums for PMJJBY life insurance, PMSBY accident insurance, and PM-SYM/KMY pension schemes.",
        "eligibility_rules": {
            "domicile_haryana": True,
            "has_parivar_pehchan_patra": True,
            "max_annual_income": 180000
        },
        "key_benefits": [
            "₹6,000 annual financial security assistance paid via DBT",
            "100% state coverage of premiums for PMJJBY (₹436), PMSBY (₹20), and PM-SYM pensions",
            "Guaranteed ₹3,000/month old age pension security after age 60"
        ],
        "required_documents": [
            "Parivar Pehchan Patra (Family ID)",
            "Aadhaar Card",
            "Bank Account linked with Family ID"
        ],
        "application_process": "Online (SARAL Haryana Portal / MMPSY Portal) / Atal Seva Kendra",
        "apply_link": "https://mmpsy.haryana.gov.in/",
        "official_source_url": "https://saralharyana.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # ==================== BIHAR ====================
    {
        "id": "kanya_utthan_bihar",
        "name": "Mukhyamantri Kanya Utthan Yojana (Bihar)",
        "category": "Women & Child Welfare",
        "domain": "Women & Child Welfare",
        "ministry": "Social Welfare Department & Education Department, Government of Bihar",
        "target_audience": ["All", "Student", "Unemployed"],
        "target_beneficiaries": ["Girl children and female students born and residing in Bihar"],
        "min_age": 0,
        "max_age": 25,
        "max_income": None,
        "gender_preference": "Female",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Bihar"],
        "state_name": "Bihar",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "Up to ₹54,100 cumulative financial assistance from birth through graduation",
        "financial_benefit_value": 54100,
        "subsidy_percentage": "100% Direct DBT Educational & Lifecycle Grant",
        "description": "Massive initiative in Bihar providing staged cash incentives from birth (₹2,000), 1-year immunization (₹1,000), 2-year Aadhaar (₹2,000), 10th pass, 12th pass (₹25,000), and graduation completion (₹50,000).",
        "eligibility_rules": {
            "domicile_bihar": True,
            "gender": "Female"
        },
        "key_benefits": [
            "₹25,000 for unmarried girls passing 12th Board Examination",
            "₹50,000 for female students graduating from recognized Bihar universities",
            "Eliminates female feticide, promotes girls' higher education and economic empowerment"
        ],
        "required_documents": [
            "Bihar Domicile / Residential Certificate",
            "Aadhaar Card of Girl Student",
            "12th / Graduation Marksheet & Registration Number",
            "Bank Passbook in Girl's Name (Bihar branch)"
        ],
        "application_process": "Online (Medhasoft Bihar Portal / e-Kalyan Portal)",
        "apply_link": "https://medhasoft.bih.nic.in/",
        "official_source_url": "https://ekalyan.bih.nic.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "udyami_yojana_bihar",
        "name": "Mukhyamantri Udyami Yojana (Bihar)",
        "category": "MSME, Business & Entrepreneurship",
        "domain": "MSME, Business & Entrepreneurship",
        "ministry": "Department of Industries, Government of Bihar",
        "target_audience": ["Entrepreneur", "Unemployed"],
        "target_beneficiaries": ["SC/ST/EBC/Women/Youth entrepreneurs setting up new manufacturing or service micro units"],
        "min_age": 18,
        "max_age": 50,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Bihar"],
        "state_name": "Bihar",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹10 Lakhs project funding (₹5 Lakhs grant/subsidy + ₹5 Lakhs interest-free / 1% loan)",
        "financial_benefit_value": 500000,
        "subsidy_percentage": "50% Direct Capital Grant (Max ₹5 Lakhs)",
        "description": "Premier entrepreneurship initiative in Bihar providing ₹10 Lakhs total capital: 50% (₹5L) as non-repayable government grant and 50% (₹5L) as interest-free loan (or 1% for General/OBC males) payable in 84 installments.",
        "eligibility_rules": {
            "domicile_bihar": True,
            "min_age": 18,
            "max_age": 50,
            "min_qualification": "12th Pass",
            "new_project_only": True
        },
        "key_benefits": [
            "₹5,00,000 non-refundable capital subsidy directly credited to project account",
            "₹5,00,000 loan with 0% interest for Women/SC/ST/EBC (1% for others)",
            "₹25,000 additional training stipend per selected entrepreneur during project incubation"
        ],
        "required_documents": [
            "Bihar Domicile Certificate",
            "10th & 12th / ITI / Diploma / Degree Marksheet",
            "Caste Certificate (if SC/ST/EBC)",
            "PAN Card & Current Bank Account Statement"
        ],
        "application_process": "Online (Udyami Portal - Industries Dept Bihar)",
        "apply_link": "https://udyami.bihar.gov.in/",
        "official_source_url": "https://udyami.bihar.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # ==================== ODISHA ====================
    {
        "id": "bsky_odisha",
        "name": "Biju Swasthya Kalyan Yojana (BSKY / Gopabandhu Jan Arogya - Odisha)",
        "category": "Health & Medical",
        "domain": "Health & Medical",
        "ministry": "Health & Family Welfare Department, Government of Odisha",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Salaried", "Construction Worker", "Fisherman"],
        "target_beneficiaries": ["All 1 Crore+ Ration Card holding families in Odisha"],
        "min_age": 0,
        "max_age": 100,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Odisha"],
        "state_name": "Odisha",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹5,00,000 per family and ₹10,00,000 for women members cashless hospital cover",
        "financial_benefit_value": 1000000,
        "subsidy_percentage": "100% Free Universal Cashless Healthcare",
        "description": "Universal health protection scheme in Odisha providing ₹5 Lakhs per family per year and an enhanced ₹10 Lakhs cashless cover for women members across 800+ empanelled hospitals in India.",
        "eligibility_rules": {
            "domicile_odisha": True,
            "has_ration_card": True
        },
        "key_benefits": [
            "₹10 Lakhs health coverage for women members; ₹5 Lakhs for family per year",
            "Over 4,000 packages covered with zero paperwork or out-of-pocket expenses",
            "Empanelled network across premier hospitals in Odisha, Hyderabad, Visakhapatnam, Kolkata, and Mumbai"
        ],
        "required_documents": [
            "BSKY Smart Card / NFSA or SFSS Ration Card",
            "Aadhaar Card",
            "Doctor Consultation / Referral"
        ],
        "application_process": "BSKY Helpdesk at Empanelled Hospitals / Mo Seva Kendra",
        "apply_link": "https://bsky.odisha.gov.in/",
        "official_source_url": "https://health.odisha.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "kalia_odisha",
        "name": "KALIA Scheme (Krushak Assistance for Livelihood and Income Augmentation - Odisha)",
        "category": "Agriculture & Allied Activities",
        "domain": "Agriculture & Allied Activities",
        "ministry": "Department of Agriculture & Farmers' Empowerment, Government of Odisha",
        "target_audience": ["Farmer", "Construction Worker", "Unemployed"],
        "target_beneficiaries": ["Small, marginal, landless agricultural workers, sharecroppers, and vulnerable farm households in Odisha"],
        "min_age": 18,
        "max_age": 100,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Odisha"],
        "state_name": "Odisha",
        "area_applicability": "Rural",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹10,000 per year for farmers & ₹12,500 livelihood unit assistance for landless laborers",
        "financial_benefit_value": 12500,
        "subsidy_percentage": "100% Direct DBT Agriculture & Livelihood Grant",
        "description": "Flagship agricultural welfare scheme of Odisha delivering direct income assistance of ₹10,000/year to small/marginal farmers and ₹12,500 for non-land agricultural livelihood activities (goat rearing, poultry, beekeeping).",
        "eligibility_rules": {
            "domicile_odisha": True,
            "is_farmer": True
        },
        "key_benefits": [
            "₹10,000/year directly into bank account (₹5,000 Kharif + ₹5,000 Rabi) for farming inputs",
            "₹12,500 for landless agricultural households for micro livelihood setups",
            "₹2,00,000 free life insurance & ₹2,00,000 accidental insurance coverage included"
        ],
        "required_documents": [
            "Aadhaar Card",
            "Ration Card",
            "Bank Passbook (Aadhaar linked)",
            "Land Record (RoR) / Self-declaration of landless laborer"
        ],
        "application_process": "Online (KALIA Portal) / Gram Panchayat Nodal Office",
        "apply_link": "https://kalia.odisha.gov.in/",
        "official_source_url": "https://agri.odisha.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # ==================== ASSAM ====================
    {
        "id": "orunodoi_assam",
        "name": "Orunodoi 2.0 / 3.0 Scheme (Assam)",
        "category": "Women & Child Welfare",
        "domain": "Women & Child Welfare",
        "ministry": "Finance Department, Government of Assam",
        "target_audience": ["All", "Unemployed", "Farmer", "Artisan"],
        "target_beneficiaries": ["Low-income resident families with priority to female heads, widows, divyangjan, and unmarried women in Assam"],
        "min_age": 18,
        "max_age": 70,
        "max_income": 200000,
        "gender_preference": "Female",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Assam"],
        "state_name": "Assam",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹1,250 per month (₹15,000 per year) unconditional cash benefit transfer",
        "financial_benefit_value": 15000,
        "subsidy_percentage": "100% Direct DBT Financial Nutrition Grant",
        "description": "Assam's largest direct benefit transfer scheme empowering over 27 lakh women with ₹1,250 on the 10th of every month for medicines, nutrition, and household financial dignity.",
        "eligibility_rules": {
            "domicile_assam": True,
            "max_annual_income": 200000
        },
        "key_benefits": [
            "₹1,250 direct cash transfer deposited every month into beneficiary's bank account",
            "Includes dedicated allocation for medicines, nutritional food, and festival expenses",
            "Covers over 27 Lakh households across rural and urban Assam"
        ],
        "required_documents": [
            "Aadhaar Card of Female Head",
            "Assam Ration Card / Income Certificate (<= ₹2 Lakhs)",
            "Aadhaar-seeded Bank Account Passbook"
        ],
        "application_process": "Gaon Panchayat / VCDC / Urban Ward Office / Orunodoi Portal",
        "apply_link": "https://orunodoi.assam.gov.in/",
        "official_source_url": "https://finance.assam.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "cmaaa_assam",
        "name": "Mukhya Mantri Atmanirbhar Asom Abhijan (CMAAA - Assam)",
        "category": "MSME, Business & Entrepreneurship",
        "domain": "MSME, Business & Entrepreneurship",
        "ministry": "Industries, Commerce and Public Enterprise Department, Assam",
        "target_audience": ["Entrepreneur", "Unemployed"],
        "target_beneficiaries": ["Educated unemployed youth of Assam setting up micro enterprises in agriculture, fabrication, packaging, and services"],
        "min_age": 28,
        "max_age": 40,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Assam"],
        "state_name": "Assam",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹2,00,000 to ₹5,00,000 seed capital (50% Government Grant + 50% Interest-free loan)",
        "financial_benefit_value": 250000,
        "subsidy_percentage": "50% Non-Repayable Government Grant (Up to ₹2.5L)",
        "description": "Massive employment generation scheme in Assam providing ₹2 Lakhs (Professional degree holders receive ₹5 Lakhs) with 50% government grant and 50% interest-free loan payable after 5 years.",
        "eligibility_rules": {
            "domicile_assam": True,
            "min_age": 28,
            "max_age": 40,
            "min_qualification": "10th Pass",
            "new_project_only": True
        },
        "key_benefits": [
            "₹1,00,000 non-repayable grant + ₹1,00,000 interest-free loan (₹2L category)",
            "₹2,50,000 non-repayable grant + ₹2,50,000 interest-free loan (₹5L category for Engineers/Doctors/Graduates)",
            "1-month free skill and managerial incubation training with ₹10,000 stipend"
        ],
        "required_documents": [
            "Assam Domicile Certificate / Voter ID",
            "Employment Exchange Registration Card",
            "Educational Qualification Certificates",
            "Detailed Project Concept / Business Plan"
        ],
        "application_process": "Online (CMAAA Portal - Government of Assam)",
        "apply_link": "https://cmaaa.assam.gov.in/",
        "official_source_url": "https://cmaaa.assam.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # ==================== JHARKHAND ====================
    {
        "id": "maiyan_samman_jharkhand",
        "name": "Mukhyamantri Maiyan Samman Yojana (Jharkhand)",
        "category": "Women & Child Welfare",
        "domain": "Women & Child Welfare",
        "ministry": "Women, Child Development and Social Security Department, Jharkhand",
        "target_audience": ["All", "Unemployed", "Farmer", "Artisan"],
        "target_beneficiaries": ["Resident women of Jharkhand aged 18 to 50 years from low-income households"],
        "min_age": 18,
        "max_age": 50,
        "max_income": 250000,
        "gender_preference": "Female",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Jharkhand"],
        "state_name": "Jharkhand",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹1,000 per month (₹12,000 per year) direct financial assistance",
        "financial_benefit_value": 12000,
        "subsidy_percentage": "100% Direct DBT Financial Grant",
        "description": "Financial dignity initiative in Jharkhand providing ₹1,000 monthly direct bank transfer to eligible women aged 18-50 to support nutrition, healthcare, and livelihood self-reliance.",
        "eligibility_rules": {
            "domicile_jharkhand": True,
            "min_age": 18,
            "max_age": 50,
            "max_annual_income": 250000
        },
        "key_benefits": [
            "₹1,000/month directly deposited into beneficiary's Aadhaar-linked bank account",
            "Covers over 48 lakh women in rural and urban Jharkhand",
            "Simple single-window verification through Pragya Kendras and Panchayat camps"
        ],
        "required_documents": [
            "Aadhaar Card",
            "Jharkhand Ration Card (Yellow / Pink / Green)",
            "Aadhaar-linked Bank Account details"
        ],
        "application_process": "Panchayat Camp / Pragya Kendra / Maiyan Samman Portal",
        "apply_link": "https://mmmsy.jharkhand.gov.in/",
        "official_source_url": "https://wcd.jharkhand.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "abua_awas_jharkhand",
        "name": "Abua Awas Yojana (Jharkhand)",
        "category": "Housing & Shelter",
        "domain": "Housing & Shelter",
        "ministry": "Rural Development Department, Government of Jharkhand",
        "target_audience": ["All", "Farmer", "Unemployed", "Construction Worker", "Artisan"],
        "target_beneficiaries": ["Homeless families and kutcha house dwellers in rural Jharkhand"],
        "min_age": 18,
        "max_age": 100,
        "max_income": 150000,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Jharkhand"],
        "state_name": "Jharkhand",
        "area_applicability": "Rural",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹2,00,000 financial grant in 4 stages + 95 days MGNREGA wages (₹26,000)",
        "financial_benefit_value": 226000,
        "subsidy_percentage": "100% Free 3-Room Pucca House Construction Grant",
        "description": "State-funded flagship housing program in Jharkhand providing ₹2,00,000 for constructing a spacious 3-room permanent pucca house with a dedicated kitchen and hygienic toilet.",
        "eligibility_rules": {
            "domicile_jharkhand": True,
            "pucca_house": False
        },
        "key_benefits": [
            "₹2,00,000 direct cash assistance disbursed in 4 construction milestones",
            "Spacious 3-room pucca layout with hygienic kitchen (larger than standard PMAY)",
            "₹26,000 additional wage assistance for 95 person-days under MGNREGA"
        ],
        "required_documents": [
            "Aadhaar Card of Family Members",
            "Ration Card",
            "Land Possession Certificate / Vested Land Proof",
            "Photograph of existing Kutcha / Dilapidated house"
        ],
        "application_process": "Aapki Yojana Aapki Sarkar Aapke Dwar Camps / Block Office",
        "apply_link": "https://aay.jharkhand.gov.in/",
        "official_source_url": "https://jharkhand.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # ==================== CHHATTISGARH ====================
    {
        "id": "mahtari_vandan_chhattisgarh",
        "name": "Mahtari Vandan Yojana (Chhattisgarh)",
        "category": "Women & Child Welfare",
        "domain": "Women & Child Welfare",
        "ministry": "Women and Child Development Department, Chhattisgarh",
        "target_audience": ["All", "Unemployed", "Farmer", "Artisan"],
        "target_beneficiaries": ["Married, widowed, and abandoned women of Chhattisgarh aged 21 and above"],
        "min_age": 21,
        "max_age": 65,
        "max_income": 250000,
        "gender_preference": "Female",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Chhattisgarh"],
        "state_name": "Chhattisgarh",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹1,000 per month (₹12,000 per year) direct bank assistance",
        "financial_benefit_value": 12000,
        "subsidy_percentage": "100% Direct DBT Financial Security Grant",
        "description": "Monthly direct benefit transfer scheme in Chhattisgarh empowering over 70 lakh married women with ₹1,000 on the 1st of every month to strengthen family nutrition, health, and economic independence.",
        "eligibility_rules": {
            "domicile_chhattisgarh": True,
            "min_age": 21,
            "max_annual_income": 250000
        },
        "key_benefits": [
            "₹1,000/month directly deposited into the woman's bank account via DBT",
            "Over 70 lakh women beneficiaries across all 33 districts of Chhattisgarh",
            "Promotes financial autonomy and maternal healthcare decision making"
        ],
        "required_documents": [
            "Aadhaar Card of Applicant & Husband",
            "Marriage Certificate or Ration Card / Panchayat Declaration",
            "Chhattisgarh Domicile Proof / Ration Card",
            "Aadhaar-linked Bank Account Details"
        ],
        "application_process": "Anganwadi Center / Gram Panchayat / Mahtari Vandan Portal",
        "apply_link": "https://mahtarivandan.cgstate.gov.in/",
        "official_source_url": "https://mahtarivandan.cgstate.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # ==================== JAMMU & KASHMIR ====================
    {
        "id": "ayushman_sehat_jk",
        "name": "Ayushman Bharat PM-JAY SEHAT (Jammu & Kashmir)",
        "category": "Health & Medical",
        "domain": "Health & Medical",
        "ministry": "Health and Medical Education Department, UT of Jammu and Kashmir",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Salaried", "Construction Worker"],
        "target_beneficiaries": ["All resident families across Jammu and Kashmir (Universal Coverage)"],
        "min_age": 0,
        "max_age": 100,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Jammu and Kashmir"],
        "state_name": "Jammu and Kashmir",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹5,00,000 universal cashless health insurance coverage per family per year",
        "financial_benefit_value": 500000,
        "subsidy_percentage": "100% Free Universal Government Cashless Coverage",
        "description": "First universal health insurance scheme in India providing ₹5 Lakhs annual cashless medical cover to 100% of all resident families in Jammu & Kashmir irrespective of income.",
        "eligibility_rules": {
            "domicile_jk": True
        },
        "key_benefits": [
            "₹5,00,000 cashless hospital cover per family per year across 28,000+ hospitals nationwide",
            "100% universal coverage with zero income ceilings or caste restrictions",
            "Covers 1,949 treatments including major oncology, bypass, and neurosurgeries"
        ],
        "required_documents": [
            "Aadhaar Card",
            "J&K Ration Card / Domicile Certificate",
            "Golden Card / Mobile verification"
        ],
        "application_process": "Common Service Center (CSC) / Empanelled Hospital Kiosk (Pradhan Mantri Arogya Mitra)",
        "apply_link": "https://sehat.jk.gov.in/",
        "official_source_url": "https://sehat.jk.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "mumkin_jk",
        "name": "Mumkin Scheme (Mission Youth J&K)",
        "category": "MSME, Business & Entrepreneurship",
        "domain": "MSME, Business & Entrepreneurship",
        "ministry": "Mission Youth, Government of Jammu and Kashmir",
        "target_audience": ["Entrepreneur", "Unemployed"],
        "target_beneficiaries": ["Unemployed youth of J&K aged 18 to 35 seeking self-employment in small commercial transport"],
        "min_age": 18,
        "max_age": 35,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Jammu and Kashmir"],
        "state_name": "Jammu and Kashmir",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹1,60,000 upfront vehicle purchase subsidy (₹80k Govt + ₹80k Vehicle Manufacturer)",
        "financial_benefit_value": 160000,
        "subsidy_percentage": "20% Upfront Capital Subsidy + 0% Down Payment",
        "description": "Customized livelihood program providing unemployed youth in J&K with small commercial vehicles (Tata Ace, Mahindra Bolero Maxi Truck, etc.) with 100% bank financing and ₹1.6 Lakhs upfront cash subsidy.",
        "eligibility_rules": {
            "domicile_jk": True,
            "min_age": 18,
            "max_age": 35,
            "has_driving_license": True
        },
        "key_benefits": [
            "Zero down payment required; 100% on-road commercial vehicle cost financed",
            "₹1,60,000 upfront capital discount/subsidy credited directly towards vehicle cost",
            "Provides immediate sustainable self-employment in local transport and logistics"
        ],
        "required_documents": [
            "J&K Domicile Certificate",
            "Commercial / LMV Driving License",
            "Aadhaar Card & Unemployed Registration proof",
            "10th Class Marksheet / Age Proof"
        ],
        "application_process": "Online (e-UNNAT Portal / Mission Youth Portal)",
        "apply_link": "https://eunnat.jk.gov.in/",
        "official_source_url": "https://missionyouth.jk.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # ==================== HIMACHAL PRADESH ====================
    {
        "id": "himcare_hp",
        "name": "HIMCARE Health Scheme (Himachal Pradesh)",
        "category": "Health & Medical",
        "domain": "Health & Medical",
        "ministry": "Department of Health & Family Welfare, Himachal Pradesh",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Salaried", "Construction Worker"],
        "target_beneficiaries": ["Resident families of Himachal Pradesh not covered under Ayushman Bharat"],
        "min_age": 0,
        "max_age": 100,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Himachal Pradesh"],
        "state_name": "Himachal Pradesh",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹5,00,000 cashless health insurance coverage per family per year",
        "financial_benefit_value": 500000,
        "subsidy_percentage": "100% Cashless Medical Hospitalization",
        "description": "Comprehensive healthcare assurance in Himachal Pradesh providing ₹5 Lakhs per family per year cashless treatment across 250+ network hospitals in HP and Chandigarh (PGIMER).",
        "eligibility_rules": {
            "domicile_hp": True
        },
        "key_benefits": [
            "₹5,00,000 cashless cover per family per year (up to 5 family members per card)",
            "Free for BPL, street vendors, and divyangjan; nominal annual fee for others",
            "Empanelled network includes AIIMS Bilaspur, IGMC Shimla, RPGMC Tanda, and PGI Chandigarh"
        ],
        "required_documents": [
            "Himachal Domicile / Bonafide Resident Certificate",
            "Aadhaar Card",
            "Ration Card / Category proof"
        ],
        "application_process": "Online (HIMCARE Portal) / LokMitra Kendra",
        "apply_link": "https://www.hpsbys.in/",
        "official_source_url": "https://www.hpsbys.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # ==================== GOA ====================
    {
        "id": "ddssy_goa",
        "name": "Deen Dayal Swasthya Seva Yojana (DDSSY - Goa)",
        "category": "Health & Medical",
        "domain": "Health & Medical",
        "ministry": "Directorate of Health Services, Government of Goa",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Salaried", "Fisherman"],
        "target_beneficiaries": ["Resident families living in Goa for 5+ years"],
        "min_age": 0,
        "max_age": 100,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Goa"],
        "state_name": "Goa",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹4,00,000 cashless health insurance cover per family per year",
        "financial_benefit_value": 400000,
        "subsidy_percentage": "100% Cashless Hospitalization Coverage",
        "description": "Universal health insurance scheme in Goa offering ₹4 Lakhs (family of 4+) or ₹2.5 Lakhs (family of up to 3) annual cashless coverage for 447 medical procedures in empanelled hospitals.",
        "eligibility_rules": {
            "domicile_goa": True
        },
        "key_benefits": [
            "₹4,00,000 annual cashless coverage for family of 4 or more; ₹2,50,000 for small families",
            "Covers 447 medical procedures, surgeries, ICU hospitalization, and prosthetics",
            "Covers all residents residing in Goa for 5 years or more"
        ],
        "required_documents": [
            "Goa Domicile / 5-Year Residence Certificate",
            "Aadhaar Card",
            "Goa Ration Card"
        ],
        "application_process": "GoaOnline Portal / DDSSY Enrollment Kiosks",
        "apply_link": "https://goaonline.gov.in/",
        "official_source_url": "https://dhsgoa.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "griha_aadhar_goa",
        "name": "Griha Aadhar Scheme (Goa)",
        "category": "Women & Child Welfare",
        "domain": "Women & Child Welfare",
        "ministry": "Directorate of Women and Child Development, Government of Goa",
        "target_audience": ["All", "Unemployed"],
        "target_beneficiaries": ["Homemakers and women from families with income under ₹3 Lakhs in Goa"],
        "min_age": 18,
        "max_age": 60,
        "max_income": 300000,
        "gender_preference": "Female",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Goa"],
        "state_name": "Goa",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹1,500 per month (₹18,000 per year) direct financial support",
        "financial_benefit_value": 18000,
        "subsidy_percentage": "100% Direct DBT Financial Grant",
        "description": "Provides ₹1,500 monthly financial assistance directly into the bank accounts of homemakers in Goa to counter inflation and maintain household nutritional security.",
        "eligibility_rules": {
            "domicile_goa": True,
            "min_age": 18,
            "max_age": 60,
            "max_annual_income": 300000
        },
        "key_benefits": [
            "₹1,500 monthly direct financial assistance to housewives and homemakers",
            "Protects low- and middle-income families from kitchen inflation",
            "Direct digital bank credit"
        ],
        "required_documents": [
            "15-Year Goa Residence Certificate",
            "Aadhaar Card",
            "Income Certificate (<= ₹3 Lakhs)",
            "Aadhaar-seeded Bank Passbook"
        ],
        "application_process": "Online (GoaOnline Portal) / Directorate of Women & Child Development Goa",
        "apply_link": "https://goaonline.gov.in/",
        "official_source_url": "https://dwcd.goa.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    }
]

db_path = os.path.join(os.path.dirname(__file__), "schemes_db.json")
with open(db_path, "r", encoding="utf-8") as f:
    schemes = json.load(f)

existing_ids = {s["id"] for s in schemes}
added = 0

for sc in ALL_NEW_STATE_SCHEMES:
    if sc["id"] not in existing_ids:
        schemes.append(sc)
        added += 1

with open(db_path, "w", encoding="utf-8") as f:
    json.dump(schemes, f, indent=2, ensure_ascii=False)

print(f"Added {added} additional state schemes! Total schemes in database: {len(schemes)}")
