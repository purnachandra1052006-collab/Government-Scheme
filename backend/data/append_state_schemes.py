import json
import os

STATE_SCHEMES = [
    # --- MAHARASHTRA ---
    {
        "id": "mjpjay_maharashtra",
        "name": "Mahatma Jyotirao Phule Jan Arogya Yojana (MJPJAY)",
        "category": "Health & Medical",
        "domain": "Health & Medical",
        "ministry": "Public Health Department, Government of Maharashtra",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Salaried", "Construction Worker", "Street Vendor"],
        "target_beneficiaries": ["All Maharashtra Domiciled Families", "Ration Card Holders (Yellow/Orange/White)"],
        "min_age": 0,
        "max_age": 100,
        "max_income": 800000,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Maharashtra"],
        "state_name": "Maharashtra",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹5,00,000 cashless health insurance coverage per family per year",
        "financial_benefit_value": 500000,
        "subsidy_percentage": "100% Free Government Cashless Hospitalization",
        "description": "Flagship health assurance scheme of Maharashtra providing ₹5 Lakhs cashless treatment for 1,356 identified medical and surgical procedures across 1,000+ empanelled hospitals.",
        "eligibility_rules": {
            "domicile_maharashtra": True,
            "max_annual_income": 800000
        },
        "key_benefits": [
            "₹5,00,000 annual cashless coverage per family across empanelled network hospitals",
            "Covers 1,356 medical and surgical therapies including oncology, cardiology, nephrology, and trauma care",
            "Universal health coverage for all ration card holders of Maharashtra",
            "Pre and post hospitalization medicine and diagnostic expenses included"
        ],
        "required_documents": [
            "Aadhaar Card",
            "Maharashtra Ration Card (Yellow / Orange / White) or Domicile Certificate",
            "Doctor's Diagnosis / Referral Slip"
        ],
        "application_process": "Empanelled Hospital Helpdesk (Arogyamitra) / Online Portal",
        "apply_link": "https://www.jeevandayee.gov.in/",
        "official_source_url": "https://www.jeevandayee.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "majhi_ladki_bahin_maharashtra",
        "name": "Mukhyamantri Majhi Ladki Bahin Yojana",
        "category": "Women & Child Welfare",
        "domain": "Women & Child Welfare",
        "ministry": "Women and Child Development Department, Government of Maharashtra",
        "target_audience": ["All", "Unemployed", "Artisan", "Farmer"],
        "target_beneficiaries": ["Women of Maharashtra aged 21 to 65 years"],
        "min_age": 21,
        "max_age": 65,
        "max_income": 250000,
        "gender_preference": "Female",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Maharashtra"],
        "state_name": "Maharashtra",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹1,500 per month (₹18,000 per year) direct bank transfer",
        "financial_benefit_value": 18000,
        "subsidy_percentage": "100% Direct DBT Financial Grant",
        "description": "Empowers underprivileged women across Maharashtra by providing ₹1,500 monthly direct financial assistance to promote health, nutrition, and financial independence.",
        "eligibility_rules": {
            "domicile_maharashtra": True,
            "max_annual_income": 250000,
            "min_age": 21,
            "max_age": 65
        },
        "key_benefits": [
            "₹1,500 monthly direct benefit transfer (DBT) directly into Aadhaar-seeded bank account",
            "Enhances financial self-reliance and nutrition security for women",
            "Simple paperless digital verification via Nari Shakti Doot App"
        ],
        "required_documents": [
            "Aadhaar Card",
            "Maharashtra Domicile Certificate / Ration Card issued before 15 years",
            "Income Certificate (Annual family income <= ₹2.5 Lakhs) or Yellow/Orange Ration Card",
            "Aadhaar-linked Bank Passbook"
        ],
        "application_process": "Online (Nari Shakti Doot App / MahaDBT Portal) / Anganwadi / Setu Suvidha Kendra",
        "apply_link": "https://ladakibahin.maharashtra.gov.in/",
        "official_source_url": "https://ladakibahin.maharashtra.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "cmyk_maharashtra",
        "name": "Mukhyamantri Yuva Karya Prashikshan Yojana",
        "category": "Employment & Skill Development",
        "domain": "Employment & Skill Development",
        "ministry": "Department of Skills, Employment, Entrepreneurship and Innovation, Maharashtra",
        "target_audience": ["Student", "Unemployed"],
        "target_beneficiaries": ["Job seekers and youth aged 18 to 35 years in Maharashtra"],
        "min_age": 18,
        "max_age": 35,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Maharashtra"],
        "state_name": "Maharashtra",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "Monthly stipend up to ₹10,000 for 6 months (Total ₹60,000)",
        "financial_benefit_value": 60000,
        "subsidy_percentage": "100% Government Funded Internship Stipend",
        "description": "Provides practical on-the-job training and paid industrial internship for educated youth in Maharashtra with monthly stipends of ₹6,000 (12th pass), ₹8,000 (Diploma/ITI), and ₹10,000 (Graduates).",
        "eligibility_rules": {
            "domicile_maharashtra": True,
            "min_age": 18,
            "max_age": 35,
            "min_qualification": "12th Pass"
        },
        "key_benefits": [
            "₹6,000/mo for 12th Pass, ₹8,000/mo for ITI/Diploma, ₹10,000/mo for Degree/PG holders",
            "6 months industry internship and work experience certificate",
            "Direct recruitment opportunities in participating industrial establishments"
        ],
        "required_documents": [
            "Aadhaar Card",
            "Maharashtra Domicile Certificate",
            "Educational Marksheets (12th / ITI / Diploma / Degree)",
            "Bank Account Details"
        ],
        "application_process": "Online (MahaSwayam Portal)",
        "apply_link": "https://rojgar.mahaswayam.gov.in/",
        "official_source_url": "https://rojgar.mahaswayam.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # --- KARNATAKA ---
    {
        "id": "gruha_lakshmi_karnataka",
        "name": "Gruha Lakshmi Scheme (Karnataka)",
        "category": "Women & Child Welfare",
        "domain": "Women & Child Welfare",
        "ministry": "Department of Women and Child Development, Government of Karnataka",
        "target_audience": ["All", "Unemployed", "Farmer", "Artisan"],
        "target_beneficiaries": ["Women head of household (Karnataka Domicile)"],
        "min_age": 18,
        "max_age": 90,
        "max_income": None,
        "gender_preference": "Female",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Karnataka"],
        "state_name": "Karnataka",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹2,000 per month (₹24,000 per year) unconditional cash transfer",
        "financial_benefit_value": 24000,
        "subsidy_percentage": "100% DBT Financial Grant",
        "description": "Karnataka's landmark welfare program granting ₹2,000 monthly cash assistance to woman head of every eligible family (Antyodaya, BPL, and APL ration card holders).",
        "eligibility_rules": {
            "domicile_karnataka": True,
            "not_income_tax_payer": True
        },
        "key_benefits": [
            "₹2,000 monthly guaranteed cash assistance deposited via DBT",
            "Covers over 1.1 crore women heads of household in Karnataka",
            "Women lead financial decisions for household well-being"
        ],
        "required_documents": [
            "Aadhaar Card of Woman Head",
            "Karnataka Ration Card (APL / BPL / Antyodaya)",
            "Aadhaar-seeded Bank Account details",
            "Husband's Aadhaar Card (if married)"
        ],
        "application_process": "Online (Seva Sindhu Portal) / Karnataka One / Grama One Centers",
        "apply_link": "https://sevasindhugs.karnataka.gov.in/",
        "official_source_url": "https://sevasindhu.karnataka.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "yuva_nidhi_karnataka",
        "name": "Yuva Nidhi Scheme (Karnataka)",
        "category": "Employment & Skill Development",
        "domain": "Employment & Skill Development",
        "ministry": "Department of Skill Development, Entrepreneurship and Livelihood, Karnataka",
        "target_audience": ["Student", "Unemployed"],
        "target_beneficiaries": ["Unemployed Degree and Diploma graduates in Karnataka"],
        "min_age": 18,
        "max_age": 30,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Karnataka"],
        "state_name": "Karnataka",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹3,000/mo for Graduates, ₹1,500/mo for Diploma holders for 2 years (Up to ₹72,000)",
        "financial_benefit_value": 72000,
        "subsidy_percentage": "100% Government Unemployment Allowance & Skill Support",
        "description": "Provides financial security and skill development for unemployed youth in Karnataka who graduated and have remained unemployed for at least 6 months.",
        "eligibility_rules": {
            "domicile_karnataka": True,
            "min_age": 18,
            "max_age": 30,
            "min_qualification": "Diploma",
            "unemployed_graduate": True
        },
        "key_benefits": [
            "₹3,000 per month for degree holders for up to 2 years or until employed",
            "₹1,500 per month for diploma holders for up to 2 years",
            "Free access to government skill development and job matching programs"
        ],
        "required_documents": [
            "Aadhaar Card",
            "Karnataka Domicile / Study Certificate (minimum 6 years in Karnataka)",
            "Degree / Diploma Certificate & Marks Cards",
            "Self-declaration of Unemployment"
        ],
        "application_process": "Online (Seva Sindhu Portal)",
        "apply_link": "https://sevasindhugs.karnataka.gov.in/",
        "official_source_url": "https://skilldevelopment.karnataka.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # --- TAMIL NADU ---
    {
        "id": "cmchis_tamil_nadu",
        "name": "Chief Minister's Comprehensive Health Insurance Scheme (CMCHIS)",
        "category": "Health & Medical",
        "domain": "Health & Medical",
        "ministry": "Health and Family Welfare Department, Government of Tamil Nadu",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Salaried", "Construction Worker", "Fisherman"],
        "target_beneficiaries": ["Low-income resident families of Tamil Nadu"],
        "min_age": 0,
        "max_age": 100,
        "max_income": 120000,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Tamil Nadu"],
        "state_name": "Tamil Nadu",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹5,00,000 cashless health insurance cover per family per year",
        "financial_benefit_value": 500000,
        "subsidy_percentage": "100% Cashless Treatment Guarantee",
        "description": "Comprehensive health protection scheme by Tamil Nadu government offering ₹5 Lakhs cashless medical and surgical treatment across 1,500+ procedures in empanelled hospitals.",
        "eligibility_rules": {
            "domicile_tamil_nadu": True,
            "max_annual_income": 120000
        },
        "key_benefits": [
            "₹5,00,000 cashless cover per family per year for secondary and tertiary care",
            "Covers 1,513 procedures, 52 diagnostic procedures, and 8 follow-up packages",
            "Includes dedicated corpus fund for specialized high-cost surgeries (organ transplants, cochlear implants)"
        ],
        "required_documents": [
            "Smart Ration Card (Tamil Nadu)",
            "Aadhaar Card",
            "Income Certificate (<= ₹1.20 Lakhs per annum from VAO / Revenue Inspector)"
        ],
        "application_process": "District Kiosk (Collectorate) / Empanelled Hospital Helpdesk",
        "apply_link": "https://www.cmchistn.com/",
        "official_source_url": "https://www.cmchistn.com/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "pudhumai_penn_tamil_nadu",
        "name": "Moovalur Ramamirtham Ammaiyar Higher Education Scheme (Pudhumai Penn)",
        "category": "Education & Scholarships",
        "domain": "Education & Scholarships",
        "ministry": "Social Welfare and Women Empowerment Department, Tamil Nadu",
        "target_audience": ["Student"],
        "target_beneficiaries": ["Female students who studied 6th to 12th in Tamil Nadu Government Schools"],
        "min_age": 17,
        "max_age": 25,
        "max_income": None,
        "gender_preference": "Female",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Tamil Nadu"],
        "state_name": "Tamil Nadu",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹1,000 per month financial aid throughout undergraduate degree / diploma",
        "financial_benefit_value": 36000,
        "subsidy_percentage": "100% Monthly DBT Educational Incentive",
        "description": "Incentivizes girl students from government schools to pursue higher education (Undergraduate degrees, Engineering, Medicine, Diploma, ITI) with ₹1,000 monthly bank transfer.",
        "eligibility_rules": {
            "domicile_tamil_nadu": True,
            "gender": "Female",
            "govt_school_student": True,
            "higher_education_pursuing": True
        },
        "key_benefits": [
            "₹1,000 deposited every month into beneficiary's bank account till graduation",
            "Prevents female student dropouts after 12th standard",
            "Applicable for Arts, Science, Engineering, Medicine, Agriculture, and Polytechnic courses"
        ],
        "required_documents": [
            "Aadhaar Card",
            "10th & 12th Marksheets / School Study Certificate (Classes 6-12 in Govt School)",
            "College / University Bonafide & Admission Fee Receipt",
            "Student Bank Account Details"
        ],
        "application_process": "Online (Penumai Penn Portal via College Nodal Officer)",
        "apply_link": "https://www.pudhumaipenn.tn.gov.in/",
        "official_source_url": "https://www.pudhumaipenn.tn.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # --- UTTAR PRADESH ---
    {
        "id": "kanya_sumangala_up",
        "name": "Mukhyamantri Kanya Sumangala Yojana (Uttar Pradesh)",
        "category": "Women & Child Welfare",
        "domain": "Women & Child Welfare",
        "ministry": "Women and Child Development Department, Government of Uttar Pradesh",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Salaried"],
        "target_beneficiaries": ["Girl child of permanent residents of Uttar Pradesh"],
        "min_age": 0,
        "max_age": 22,
        "max_income": 300000,
        "gender_preference": "Female",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Uttar Pradesh"],
        "state_name": "Uttar Pradesh",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹25,000 conditional cash grant across 6 developmental milestones",
        "financial_benefit_value": 25000,
        "subsidy_percentage": "100% DBT Milestone Grant",
        "description": "Comprehensive conditional cash transfer scheme in Uttar Pradesh providing ₹25,000 across birth, complete vaccination, Class 1, Class 6, Class 9 admission, and graduation enrolment.",
        "eligibility_rules": {
            "domicile_up": True,
            "has_girl_child": True,
            "max_annual_income": 300000
        },
        "key_benefits": [
            "₹25,000 cumulative grant transferred in 6 stages from birth through degree admission",
            "Encourages female literacy, immunization, and prevents female feticide",
            "Covers up to two daughters per family"
        ],
        "required_documents": [
            "Aadhaar Card of Parent and Daughter",
            "UP Domicile / Resident Certificate",
            "Income Certificate (<= ₹3.00 Lakhs per annum)",
            "Birth Certificate / School Enrolment Certificate"
        ],
        "application_process": "Online (MKSY Portal) / Common Service Centers (CSC)",
        "apply_link": "https://mksy.up.gov.in/",
        "official_source_url": "https://mksy.up.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "mmysy_up",
        "name": "Mukhyamantri Yuva Swarojgar Yojana (UP-MMYSY)",
        "category": "MSME, Business & Entrepreneurship",
        "domain": "MSME, Business & Entrepreneurship",
        "ministry": "Department of MSME and Export Promotion, Uttar Pradesh",
        "target_audience": ["Entrepreneur", "Unemployed"],
        "target_beneficiaries": ["Educated unemployed youth of Uttar Pradesh establishing micro ventures"],
        "min_age": 18,
        "max_age": 40,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Uttar Pradesh"],
        "state_name": "Uttar Pradesh",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "Loan up to ₹25 Lakhs (Industry) or ₹10 Lakhs (Service) with 25% capital subsidy",
        "financial_benefit_value": 625000,
        "subsidy_percentage": "25% Government Margin Money Subsidy (Max ₹6.25L)",
        "description": "Fosters self-employment in Uttar Pradesh by providing collateral-free bank loans up to ₹25 Lakhs for manufacturing units and ₹10 Lakhs for service businesses with 25% state margin subsidy.",
        "eligibility_rules": {
            "domicile_up": True,
            "min_age": 18,
            "max_age": 40,
            "min_qualification": "10th Pass",
            "new_project_only": True
        },
        "key_benefits": [
            "25% capital margin money subsidy credited directly into loan account",
            "Up to ₹25 Lakhs loan for industrial enterprises, ₹10 Lakhs for service enterprises",
            "Converts loan subsidy into grant after 2 years of successful business operation"
        ],
        "required_documents": [
            "Aadhaar Card & UP Domicile Certificate",
            "Educational Qualification Certificate (Minimum 10th Pass)",
            "Detailed Project Report (DPR)",
            "PAN Card & Caste Certificate (if applicable)"
        ],
        "application_process": "Online (DIUPMS Portal - MSME UP)",
        "apply_link": "http://diupmsme.upsdc.gov.in/",
        "official_source_url": "http://diupmsme.upsdc.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # --- ANDHRA PRADESH ---
    {
        "id": "ysr_aarogyasri_ap",
        "name": "Dr. YSR Aarogyasri Health Scheme (Andhra Pradesh)",
        "category": "Health & Medical",
        "domain": "Health & Medical",
        "ministry": "Health, Medical and Family Welfare Department, Government of Andhra Pradesh",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Salaried", "Construction Worker", "Fisherman"],
        "target_beneficiaries": ["All resident families of Andhra Pradesh with income under ₹5 Lakhs"],
        "min_age": 0,
        "max_age": 100,
        "max_income": 500000,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Andhra Pradesh"],
        "state_name": "Andhra Pradesh",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹10,00,000 cashless medical coverage per family per year",
        "financial_benefit_value": 1000000,
        "subsidy_percentage": "100% Free Cashless Treatment Guarantee",
        "description": "Comprehensive universal health coverage scheme of Andhra Pradesh covering cashless treatment up to ₹10 Lakhs for 3,257 medical procedures across 2,000+ empanelled hospitals.",
        "eligibility_rules": {
            "domicile_andhra_pradesh": True,
            "max_annual_income": 500000
        },
        "key_benefits": [
            "Cashless health cover up to ₹10,00,000 per family per year",
            "Covers 3,257 surgical and medical treatments including major surgeries & cancer therapy",
            "Aarogya Aasara post-operative allowance of ₹225/day (up to ₹5,000/mo) during recovery"
        ],
        "required_documents": [
            "Dr. YSR Aarogyasri Smart Card / Rice Card (Ration Card)",
            "Aadhaar Card",
            "Income Certificate or Land Holding documents"
        ],
        "application_process": "Empanelled Network Hospital Helpdesk (Arogyamitra) / Grama Sachivalayam",
        "apply_link": "https://aarogyasri.ap.gov.in/",
        "official_source_url": "https://aarogyasri.ap.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "jagananna_vidya_deevena_ap",
        "name": "Jagananna Vidya Deevena (Full Fee Reimbursement)",
        "category": "Education & Scholarships",
        "domain": "Education & Scholarships",
        "ministry": "Higher Education Department, Government of Andhra Pradesh",
        "target_audience": ["Student"],
        "target_beneficiaries": ["College students pursuing Polytechnic, ITI, Degree, Engineering, Medicine, PG"],
        "min_age": 16,
        "max_age": 30,
        "max_income": 250000,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Andhra Pradesh"],
        "state_name": "Andhra Pradesh",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "100% Complete tuition fee reimbursement directly into mother's account",
        "financial_benefit_value": 75000,
        "subsidy_percentage": "100% Full College Tuition Fee Waiver",
        "description": "Ensures no meritorious student in Andhra Pradesh is denied higher education due to poverty by providing 100% full fee reimbursement paid quarterly to mothers' bank accounts.",
        "eligibility_rules": {
            "domicile_andhra_pradesh": True,
            "max_annual_income": 250000,
            "student_attendance_min": 75
        },
        "key_benefits": [
            "100% full tuition fee deposited directly into student mother's bank account",
            "Covers ITI, Polytechnic, B.Tech, B.Pharmacy, MBBS, B.Sc, MBA, MCA, and Post Graduation",
            "Quarterly transparent disbursements linked with 75% biometric attendance"
        ],
        "required_documents": [
            "Rice Card / BPL Card / Income Certificate (<= ₹2.5L)",
            "Aadhaar Card of Student and Mother",
            "College Admission Allotment Letter & Fee Structure",
            "Mother's Aadhaar-linked Bank Passbook"
        ],
        "application_process": "Online (JnanaBhumi Portal) / Village/Ward Secretariats",
        "apply_link": "https://jnanabhumi.ap.gov.in/",
        "official_source_url": "https://jnanabhumi.ap.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # --- TELANGANA ---
    {
        "id": "aarogyasri_telangana",
        "name": "Rajiv Aarogyasri Scheme (Telangana)",
        "category": "Health & Medical",
        "domain": "Health & Medical",
        "ministry": "Medical, Health & Family Welfare Department, Telangana",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Salaried", "Construction Worker"],
        "target_beneficiaries": ["BPL Food Security Card holding families in Telangana"],
        "min_age": 0,
        "max_age": 100,
        "max_income": 200000,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Telangana"],
        "state_name": "Telangana",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹10,00,000 cashless medical coverage per family per year",
        "financial_benefit_value": 1000000,
        "subsidy_percentage": "100% Free Treatment in Empanelled Hospitals",
        "description": "Telangana's enhanced healthcare program offering cashless financial cover up to ₹10 Lakhs for catastrophic illnesses and surgeries in network hospitals.",
        "eligibility_rules": {
            "domicile_telangana": True,
            "max_annual_income": 200000
        },
        "key_benefits": [
            "Cashless treatment up to ₹10 Lakhs covering 1,672 treatments & procedures",
            "Complete cashless inpatient care, diagnostics, and 10 days post-discharge medicines",
            "Dedicated Aarogya Mithra help desks across government and private network hospitals"
        ],
        "required_documents": [
            "Telangana Food Security Card (White Ration Card)",
            "Aadhaar Card",
            "Patient Diagnostic Referral"
        ],
        "application_process": "Aarogyasri Kiosk at Network Hospital / Online Portal",
        "apply_link": "https://aarogyasri.telangana.gov.in/",
        "official_source_url": "https://aarogyasri.telangana.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "rythu_bandhu_telangana",
        "name": "Rythu Bharosa / Rythu Bandhu Scheme (Telangana)",
        "category": "Agriculture & Allied Activities",
        "domain": "Agriculture & Allied Activities",
        "ministry": "Agriculture & Co-operation Department, Government of Telangana",
        "target_audience": ["Farmer"],
        "target_beneficiaries": ["Pattadar landowning farmers and agriculturalists in Telangana"],
        "min_age": 18,
        "max_age": 100,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Telangana"],
        "state_name": "Telangana",
        "area_applicability": "Rural",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹15,000 per acre per year direct farmer investment support",
        "financial_benefit_value": 30000,
        "subsidy_percentage": "100% Crop Investment DBT Assistance",
        "description": "Provides financial investment support of ₹15,000 per acre per year (₹7,500/acre per crop season) directly to farmers for buying seeds, fertilizers, pesticides, and farming inputs.",
        "eligibility_rules": {
            "domicile_telangana": True,
            "is_farmer": True,
            "owns_agricultural_land": True
        },
        "key_benefits": [
            "₹15,000 per acre per year direct benefit transfer for Kharif & Rabi seasons",
            "Eliminates debt trap from informal private moneylenders",
            "Direct electronic transfer straight into farmer bank accounts"
        ],
        "required_documents": [
            "Pattadar Passbook (Dharani Portal record)",
            "Aadhaar Card",
            "Bank Account Passbook"
        ],
        "application_process": "Online (Rythu Bandhu Portal / Agriculture Extension Officer)",
        "apply_link": "https://rythubandhu.telangana.gov.in/",
        "official_source_url": "https://rythubandhu.telangana.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # --- WEST BENGAL ---
    {
        "id": "swasthya_sathi_wb",
        "name": "Swasthya Sathi Scheme (West Bengal)",
        "category": "Health & Medical",
        "domain": "Health & Medical",
        "ministry": "Department of Health & Family Welfare, Government of West Bengal",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Salaried", "Construction Worker"],
        "target_beneficiaries": ["All resident families of West Bengal (Smart card issued to Woman Head)"],
        "min_age": 0,
        "max_age": 100,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["West Bengal"],
        "state_name": "West Bengal",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹5,00,000 cashless basic health cover per family per year",
        "financial_benefit_value": 500000,
        "subsidy_percentage": "100% Free Paperless Cashless Treatment",
        "description": "Universal health protection scheme by West Bengal government providing ₹5 Lakhs annual cashless cover per family on a smart card registered in the name of the woman head of household.",
        "eligibility_rules": {
            "domicile_west_bengal": True
        },
        "key_benefits": [
            "₹5,00,000 cashless cover per family per year across 2,200+ empanelled hospitals",
            "Pre-existing illnesses covered; no limit on family size",
            "Issued in the name of the oldest female member to empower women"
        ],
        "required_documents": [
            "Aadhaar Card",
            "West Bengal Khadya Sathi (Ration Card)",
            "Family Member Details"
        ],
        "application_process": "Duare Sarkar Camps / Municipality Office / Swasthya Sathi Portal",
        "apply_link": "https://swasthyasathi.gov.in/",
        "official_source_url": "https://swasthyasathi.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "kanyashree_wb",
        "name": "Kanyashree Prakalpa (West Bengal)",
        "category": "Education & Scholarships",
        "domain": "Education & Scholarships",
        "ministry": "Department of Women & Child Development and Social Welfare, West Bengal",
        "target_audience": ["Student"],
        "target_beneficiaries": ["Unmarried adolescent girls aged 13-19 years studying in recognized institutions"],
        "min_age": 13,
        "max_age": 19,
        "max_income": 120000,
        "gender_preference": "Female",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["West Bengal"],
        "state_name": "West Bengal",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹1,000 annual scholarship (K1) + ₹25,000 one-time grant at age 18 (K2)",
        "financial_benefit_value": 30000,
        "subsidy_percentage": "100% UN Award-Winning Educational Grant",
        "description": "United Nations award-winning initiative of West Bengal to improve the status and well-being of the girl child by incentivizing schooling and preventing early child marriage.",
        "eligibility_rules": {
            "domicile_west_bengal": True,
            "min_age": 13,
            "max_age": 19,
            "is_unmarried": True,
            "max_annual_income": 120000
        },
        "key_benefits": [
            "Annual Scholarship (K1): ₹1,000/year for girls in classes VIII to XII",
            "One-time Grant (K2): ₹25,000 on turning 18 if unmarried and continuing education",
            "Direct digital disbursement into the girl's dedicated bank account"
        ],
        "required_documents": [
            "Aadhaar Card",
            "School / College Enrolment Certificate",
            "Unmarried Certificate signed by Parent/Guardian",
            "Bank Passbook in Girl's Name"
        ],
        "application_process": "Through respective School / College Head / Kanyashree Portal",
        "apply_link": "https://www.wbkanyashree.gov.in/",
        "official_source_url": "https://www.wbkanyashree.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # --- RAJASTHAN ---
    {
        "id": "chiranjeevi_rajasthan",
        "name": "Mukhyamantri Ayushman Arogya (Chiranjeevi) Yojana",
        "category": "Health & Medical",
        "domain": "Health & Medical",
        "ministry": "Medical, Health and Family Welfare Department, Rajasthan",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Salaried", "Construction Worker"],
        "target_beneficiaries": ["All resident families of Rajasthan"],
        "min_age": 0,
        "max_age": 100,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Rajasthan"],
        "state_name": "Rajasthan",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹25,00,000 cashless medical hospitalization coverage per family per year",
        "financial_benefit_value": 2500000,
        "subsidy_percentage": "100% Free Cashless Hospital Treatment",
        "description": "India's highest coverage health assurance scheme offering ₹25 Lakhs per family per year cashless treatment for complex illnesses, surgeries, and organ transplants.",
        "eligibility_rules": {
            "domicile_rajasthan": True,
            "has_jan_aadhaar": True
        },
        "key_benefits": [
            "₹25 Lakhs annual cashless health cover per family across empanelled hospitals",
            "Covers 1,800+ treatments, kidney/liver/heart transplants, and oncology packages",
            "Free for NFSA, SECC, small farmers, and contractual workers; modest ₹850 premium for others"
        ],
        "required_documents": [
            "Jan Aadhaar Card (Rajasthan)",
            "Aadhaar Card",
            "Ration Card / NFSA Proof (if applicable)"
        ],
        "application_process": "Online (Jan Soochna / SSO Rajasthan) / E-Mitra Kiosks",
        "apply_link": "https://chiranjeevi.rajasthan.gov.in/",
        "official_source_url": "https://chiranjeevi.rajasthan.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "anupriti_rajasthan",
        "name": "Mukhyamantri Anupriti Coaching Scheme (Rajasthan)",
        "category": "Education & Scholarships",
        "domain": "Education & Scholarships",
        "ministry": "Social Justice and Empowerment Department, Government of Rajasthan",
        "target_audience": ["Student"],
        "target_beneficiaries": ["Meritorious students preparing for UPSC, RPSC, JEE, NEET, CA, CLAT, Banking"],
        "min_age": 16,
        "max_age": 28,
        "max_income": 800000,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Rajasthan"],
        "state_name": "Rajasthan",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "100% Free premier coaching + ₹40,000 annual boarding/lodging allowance",
        "financial_benefit_value": 150000,
        "subsidy_percentage": "100% Government Funded Professional Coaching",
        "description": "Provides 100% free coaching in top reputed coaching institutes plus ₹40,000 annual living allowance for meritorious candidates from economically backward families.",
        "eligibility_rules": {
            "domicile_rajasthan": True,
            "max_annual_income": 800000,
            "merit_qualification": True
        },
        "key_benefits": [
            "Free coaching in premier institutes for IAS, RAS, IIT-JEE, NEET, CLAT, CA, and Constable exams",
            "₹40,000 annual stipend for hostel and lodging if studying in a different city",
            "Over 30,000 meritorious students sponsored each academic year"
        ],
        "required_documents": [
            "Jan Aadhaar Card / Domicile Certificate",
            "10th & 12th / Graduation Marksheets",
            "Caste Certificate & Income Certificate (<= ₹8 Lakhs)",
            "Bank Account Details"
        ],
        "application_process": "Online (SJMS Portal - SSO Rajasthan)",
        "apply_link": "https://sje.rajasthan.gov.in/",
        "official_source_url": "https://sje.rajasthan.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # --- DELHI ---
    {
        "id": "delhi_arogya_kosh",
        "name": "Delhi Arogya Kosh (DAK) & Free High-End Diagnostics Scheme",
        "category": "Health & Medical",
        "domain": "Health & Medical",
        "ministry": "Directorate General of Health Services, Government of NCT of Delhi",
        "target_audience": ["All", "Farmer", "Unemployed", "Artisan", "Salaried", "Construction Worker"],
        "target_beneficiaries": ["All permanent residents of Delhi with Voter ID Card"],
        "min_age": 0,
        "max_age": 100,
        "max_income": None,
        "gender_preference": "All",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Delhi"],
        "state_name": "Delhi",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "100% Free cashless surgeries (up to ₹5L) and high-end MRI/CT/PET scans",
        "financial_benefit_value": 500000,
        "subsidy_percentage": "100% Free Cashless Diagnostics & Surgery Guarantee",
        "description": "Ensures every Delhi resident receives free specialized surgeries in private hospitals when wait times exceed 30 days in govt hospitals, plus free MRI, CT scans, and ultrasound at private labs.",
        "eligibility_rules": {
            "domicile_delhi": True,
            "has_delhi_voter_id": True
        },
        "key_benefits": [
            "Free cashless surgeries for 450+ designated procedures in top private empanelled hospitals",
            "Free high-end diagnostic tests (MRI, CT Scan, PET Scan, Echo, Nuclear scans) in private labs",
            "Financial assistance up to ₹5 Lakhs for critical life-saving implants and treatments"
        ],
        "required_documents": [
            "Delhi Voter ID Card / Domicile Proof (mandatory for adult)",
            "Aadhaar Card",
            "Prescription / Referral from Delhi Government Hospital Doctor"
        ],
        "application_process": "Referral through Delhi Govt Hospital / DAK Online Counter",
        "apply_link": "https://dshm.delhi.gov.in/",
        "official_source_url": "https://dshm.delhi.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },
    {
        "id": "jai_bhim_delhi",
        "name": "Jai Bhim Mukhyamantri Pratibha Vikas Yojana (Delhi)",
        "category": "Education & Scholarships",
        "domain": "Education & Scholarships",
        "ministry": "Department for the Welfare of SC/ST/OBC, Government of NCT of Delhi",
        "target_audience": ["Student"],
        "target_beneficiaries": ["SC/ST/OBC/EWS students residing in Delhi preparing for competitive exams"],
        "min_age": 16,
        "max_age": 30,
        "max_income": 800000,
        "gender_preference": "All",
        "caste_category": ["OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Delhi"],
        "state_name": "Delhi",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "100% Free premier coaching + ₹2,500/month stipend",
        "financial_benefit_value": 120000,
        "subsidy_percentage": "100% Government Funded Coaching & Monthly Stipend",
        "description": "Sponsors complete coaching fees for competitive exams (UPSC, SSC, IIT-JEE, NEET, CLAT, Bank PO) in leading private institutes and provides ₹2,500 monthly stipend.",
        "eligibility_rules": {
            "domicile_delhi": True,
            "max_annual_income": 800000,
            "caste_restriction": ["SC", "ST", "OBC", "EWS"]
        },
        "key_benefits": [
            "100% coaching fee paid directly to top empanelled coaching institutes",
            "₹2,500 monthly stipend credited directly to student's bank account for study materials & transport",
            "Covers Civil Services, Engineering, Medical, Judicial Services, and Defence examinations"
        ],
        "required_documents": [
            "Delhi Domicile / Voter ID / Ration Card",
            "Aadhaar Card",
            "Caste Certificate (SC/ST/OBC) or EWS Certificate",
            "Income Certificate (Annual family income <= ₹8.00 Lakhs)"
        ],
        "application_process": "Online (e-District Delhi Portal) / Empanelled Coaching Institute",
        "apply_link": "https://edistrict.delhigovt.nic.in/",
        "official_source_url": "https://scstwelfare.delhi.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    },

    # --- MADHYA PRADESH ---
    {
        "id": "ladli_behna_mp",
        "name": "Mukhyamantri Ladli Behna Yojana (Madhya Pradesh)",
        "category": "Women & Child Welfare",
        "domain": "Women & Child Welfare",
        "ministry": "Women and Child Development Department, Madhya Pradesh",
        "target_audience": ["All", "Unemployed", "Farmer", "Artisan"],
        "target_beneficiaries": ["Resident married/widowed/divorced women of Madhya Pradesh aged 21 to 60"],
        "min_age": 21,
        "max_age": 60,
        "max_income": 250000,
        "gender_preference": "Female",
        "caste_category": ["General", "OBC", "SC", "ST", "EWS"],
        "states_applicable": ["Madhya Pradesh"],
        "state_name": "Madhya Pradesh",
        "area_applicability": "All",
        "central_or_state": "State Government",
        "max_subsidy_or_loan": "₹1,250 per month (₹15,000 per year) direct bank assistance",
        "financial_benefit_value": 15000,
        "subsidy_percentage": "100% Direct DBT Financial Grant",
        "description": "Financial empowerment scheme providing ₹1,250 monthly direct assistance to women in Madhya Pradesh to foster economic self-reliance and nutritional health.",
        "eligibility_rules": {
            "domicile_mp": True,
            "min_age": 21,
            "max_age": 60,
            "max_annual_income": 250000
        },
        "key_benefits": [
            "₹1,250 transferred monthly on the 10th directly into Aadhaar-linked bank accounts",
            "Over 1.29 crore women beneficiaries across rural and urban Madhya Pradesh",
            "Paperless, decentralized registration through Samagra ID and e-KYC"
        ],
        "required_documents": [
            "Samagra Family ID and Member ID",
            "Aadhaar Card",
            "Aadhaar-linked & DBT enabled Bank Account"
        ],
        "application_process": "Gram Panchayat / Ward Office Camps / Ladli Behna Portal",
        "apply_link": "https://cmladlibahna.mp.gov.in/",
        "official_source_url": "https://cmladlibahna.mp.gov.in/",
        "last_verified_date": "2026-09",
        "scheme_status": "Active"
    }
]

db_path = os.path.join(os.path.dirname(__file__), "schemes_db.json")
with open(db_path, "r", encoding="utf-8") as f:
    current_schemes = json.load(f)

current_ids = {s["id"] for s in current_schemes}
added_count = 0

for state_scheme in STATE_SCHEMES:
    if state_scheme["id"] not in current_ids:
        current_schemes.append(state_scheme)
        added_count += 1

with open(db_path, "w", encoding="utf-8") as f:
    json.dump(current_schemes, f, indent=2, ensure_ascii=False)

print(f"Successfully added {added_count} state government schemes! Total schemes: {len(current_schemes)}")
