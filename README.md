# 🏛️ Government Scheme-Matching Assistant (GovScheme.AI)

A full-stack, RAG & Rule-Powered web application titled **"Government Scheme-Matching Assistant"** designed to guide Indian citizens through an adaptive conversational profile intake, verify deterministic eligibility constraints across Central & State schemes, detect near-miss opportunities with actionable advice, rank recommendations by financial benefit & eligibility score, generate transparent reasoning ("Why You Qualify"), and deliver an interactive required documents checklist with PDF export.

---

## 🌟 Key Features

1. **Conversational Profile Intake (5–8 Adaptive Questions)**
   - Dynamic questioning that adapts based on user demographics (Students, Entrepreneurs, Farmers, Artisans, Street Vendors, Jobseekers, Salaried).
   - Real-time profile state tracking and live summary sidebar.

2. **Hybrid Reasoning Engine**
   - **Deterministic Python Rule Engine**: Strict boundary evaluation for age brackets, income caps, gender preference, social categories (General, OBC, SC, ST, EWS), state applicability, and educational prerequisites.
   - **Near-Miss Engine**: Evaluates edge cases failing 1–2 soft criteria (e.g., income threshold within 10–15%, age within 1–2 years) and generates concrete steps to qualify.
   - **Ranking Engine**: Computes weighted scores based on exact demographic fit and normalized financial benefit magnitude.

3. **LLM Explanations & "Why You Qualify" Reasoning (Groq Llama-3.3 70B)**
   - Generates transparent point-by-point breakdown for matching attributes, key financial benefits/subsidies, and next action items.
   - Built-in fallback rule-based reasoning engine ensuring 100% offline uptime and zero failure risk.

4. **Interactive Required Documents Checklist & PDF Export**
   - Deduplicated across all eligible schemes into Universal Proofs (Aadhaar, PAN, Bank Passbook, Photos) and Scheme-Specific Proofs (DPR, Caste Certificates, RoR Land Records, Artisan ID, DPIIT Letters).
   - Real-time checkbox completion progress tracker.
   - 1-Click PDF Download, Markdown Copy, and Print Support.

5. **Scheme Comparison Matrix & Catalog Directory**
   - Side-by-side comparison of loan caps, subsidies, and prerequisite rules.
   - Searchable and filterable directory of 12+ curated realistic Indian government schemes.

---

## 🗄️ Curated Schemes Database

Includes realistic Central & State schemes conforming to the required schema:
- **PMEGP**: Prime Minister’s Employment Generation Programme (Up to ₹50L + 35% subsidy)
- **PM MUDRA Yojana**: Shishu, Kishore, Tarun & Tarun Plus (Up to ₹20L collateral-free)
- **Stand-Up India Scheme**: SC/ST and Women Entrepreneurs (₹10L to ₹1 Crore)
- **Post-Matric Scholarship**: SC/ST/OBC/EWS Students (100% tuition + maintenance allowance)
- **PM-KISAN**: PM Kisan Samman Nidhi (₹6,000/year direct DBT)
- **PM SVANidhi**: Micro-credit for Urban Street Vendors (Up to ₹50k + 7% interest subsidy)
- **PM Vishwakarma Scheme**: 18 Traditional Crafts & Trades (₹15,000 Toolkit grant + 5% loan)
- **Startup India Seed Fund (SISFS)**: Up to ₹20L Grant + ₹50L Debt
- **Pradhan Mantri Awas Yojana (PMAY)**: Up to ₹2.67L CLSS interest subsidy
- **CSSS**: Central Sector Scholarship for College & University Students
- **PMKVY 4.0**: Pradhan Mantri Kaushal Vikas Yojana
- **NAPS-2**: National Apprenticeship Promotion Scheme

---

## 🚀 Quick Start Guide

### 1. Backend Setup (FastAPI)
```bash
cd backend
pip install -r requirements.txt

# Run backend server
python app.py
# Server runs on http://localhost:8000 (Swagger docs at http://localhost:8000/docs)
```

### 2. Frontend Setup (React + Vite)
```bash
cd frontend
npm install
npm run dev
# App runs on http://localhost:5173
```

### 3. Run Backend Unit Tests
```bash
python backend/tests/run_tests.py
```

### 4. Optional: Configure Groq API Key
Set your `GROQ_API_KEY` in `backend/.env` or click the **Groq LLM** button directly in the web UI navbar to enter your key.

---

## 🧪 Architecture & Testing

- Unit tests verify rule engine accuracy across student scholarships, entrepreneur subsidies, near-miss income gaps, farmer DBT schemes, and document deduplication.
- Frontend built with Tailwind CSS, Lucide Icons, and jsPDF.
