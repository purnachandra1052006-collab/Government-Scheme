# 🏛️ System Architecture: GovScheme.AI

**GovScheme.AI** is an enterprise-grade, hybrid **RAG & Rule-Powered National Scheme Eligibility & Benefit Matching Engine** designed to help Indian citizens discover, evaluate, and apply for central and state government welfare schemes, subsidies, grants, loans, and scholarships across **24 National Domains**.

---

## 📐 1. End-to-End System Architecture

```mermaid
flowchart TD
    %% Clients Layer
    subgraph ClientLayer["🖥️ Presentation Layer (React + Vite + Tailwind CSS)"]
        UI_Chat["💬 Conversational AI Intake\n(Natural Language + Adaptive Chips)"]
        UI_Wizard["📋 Quick Assessment Wizard\n(Categorized Multi-Step Form)"]
        UI_Directory["📚 24-Domain Scheme Directory\n(Multi-Filter & Instant Search)"]
        UI_Dashboard["📊 Results Dashboard\n(Cards, Near-Miss, Matrix, PDF Export)"]
    end

    %% API Gateway Layer
    subgraph APILayer["⚡ API Gateway & Server (Python FastAPI)"]
        API_Routes["FastAPI REST Endpoints\n(/api/chat, /api/evaluate, /api/schemes)"]
        CORS["CORS & Session Middleware"]
    end

    %% Orchestration & Reasoning
    subgraph EngineLayer["🧠 Hybrid Reasoning & Matching Core"]
        %% LLM Layer
        subgraph LLMModule["🤖 Conversational LLM & NLP Layer (Groq / Llama-3.3 70B)"]
            NLP_Extractor["Entity & Slot Extractor\n(Age, Gender, Caste, Income, Goals, Special Status)"]
            Chat_Reasoner["Conversational QA & Guidance\n(Scheme Inquiries & Dialog Management)"]
            Explain_Gen["'Why You Qualify' & Benefit Explainer\n(Plain-Language Synthesis)"]
        end

        %% Deterministic Logic Core
        subgraph RuleModule["⚖️ Deterministic Evaluation Core (Python Engine)"]
            Rule_Engine["Deterministic Rule Engine\n(Age, Income Ceiling, Gender, Caste, State, Area, Rules)"]
            NearMiss_Engine["Near-Miss Criteria Evaluator\n(Boundary Gap Analysis: Income +15%, Age +1yr, Disability %)"]
            Ranking_Engine["Multi-Attribute Ranking Engine\n(Demographic Fit 60% + Financial Benefit 40%)"]
            Doc_Manager["Document Checklist Manager\n(Deduplication & Universal/Specific Grouping)"]
        end
    end

    %% Data Store
    subgraph DataLayer["🗄️ National Scheme Knowledge Base"]
        SchemesDB[("schemes_db.json\n30+ Curated Official Schemes\nacross 24 National Domains")]
    end

    %% Connectors
    ClientLayer <==>|HTTP / REST JSON| APILayer
    APILayer --> API_Routes
    API_Routes <--> NLP_Extractor
    API_Routes <--> Rule_Engine
    
    NLP_Extractor -->|Extracted Profile| Rule_Engine
    Rule_Engine <-->|Queries & Rules| SchemesDB
    
    Rule_Engine -->|Hard Matches| Ranking_Engine
    Rule_Engine -->|Borderline Gaps| NearMiss_Engine
    NearMiss_Engine -->|Near-Miss Recommendations| Ranking_Engine

    Ranking_Engine --> Explain_Gen
    Explain_Gen --> Doc_Manager
    Doc_Manager -->|EvaluationResponse JSON| API_Routes
    API_Routes --> UI_Dashboard
```

---

## 🔄 2. Data Flow & Execution Sequence

```mermaid
sequenceDiagram
    autonumber
    actor Citizen as Citizen / User
    participant Frontend as React Frontend
    participant API as FastAPI Backend
    participant LLM as Groq Llama-3.3 LLM
    participant Rules as Python Rule Engine
    participant DB as Schemes Database (24 Domains)

    Citizen->>Frontend: Sends Natural Message (e.g. "I'm a 28yo woman in Karnataka with a 4yo daughter...")
    Frontend->>API: POST /api/chat/message (user_message, current_profile)
    
    API->>LLM: process_conversational_turn()
    Note over LLM: Extracts slots: age=28, gender=Female, state=KA,<br/>has_girl_child=True, girl_child_age=4
    LLM-->>API: (updated_profile, conversational_reply, suggested_chips, is_ready)
    API-->>Frontend: Returns ChatIntakeSession JSON
    Frontend-->>Citizen: Displays AI reply, live updated profile drawer, and quick chips

    Citizen->>Frontend: Clicks "Run Scheme Eligibility Match"
    Frontend->>API: POST /api/evaluate (user_profile)
    
    API->>Rules: evaluate_scheme() across all schemes
    Rules->>DB: Load scheme criteria & eligibility rules
    
    alt Satisfies all mandatory criteria
        Rules-->>API: MatchType = Direct Eligible
    else Fails 1 or 2 soft criteria (e.g., income within 15%, age within 1yr)
        Rules->>Rules: NearMissEvaluator.evaluate_near_miss()
        Rules-->>API: MatchType = Near-Miss (with gap explanation & advice)
    else Hard mismatch
        Rules-->>API: MatchType = Ineligible
    end

    API->>Rules: RankingEngine.rank_matches() [Demographic Fit + Normalized Benefit]
    API->>LLM: generate_scheme_reasoning() [Generates "Why You Qualify" breakdown]
    API->>Rules: DocumentChecklistManager [Deduplicates required documents]
    
    API-->>Frontend: EvaluationResponse (Direct Matches, Near Misses, Checklist, Summary)
    Frontend-->>Citizen: Renders interactive Dashboard, Scheme Cards, Comparison Table, and PDF Export
```

---

## 🧩 3. Architectural Component Breakdown

### A. Presentation Layer (Frontend)
- **Framework:** React 19 + Vite + Tailwind CSS + Lucide Icons + jsPDF
- **Core Components:**
  1. `ChatIntake.jsx`: Natural language conversational intake with dynamic suggested chip replies.
  2. `QuickFormIntake.jsx`: Multi-step categorized assessment wizard (Demographics, Economics, Specialized Criteria).
  3. `ProfileSummaryDrawer.jsx`: Live reactive profile viewer displaying extracted attributes.
  4. `SchemeCard.jsx`: Displays match score, domain badges, "Why You Qualify" accordion, Near-Miss alert notices, and official portal links.
  5. `DocumentChecklist.jsx`: Deduplicated document checklist with real-time checkbox tracking and 1-click PDF download.
  6. `SchemeComparison.jsx`: Side-by-side comparison table of benefits, subsidies, and requirements.
  7. `SchemeCatalog.jsx`: 24-domain chips filter with instant search.

### B. API Gateway & Controllers (Backend)
- **Framework:** Python 3.9+ with FastAPI & Uvicorn
- **Endpoints:**
  - `POST /api/chat/start`: Initializes intake session and profile state.
  - `POST /api/chat/message`: Handles natural language input, slot extraction, and dynamic quick replies.
  - `POST /api/evaluate`: Executes deterministic rule matching, ranking, and document aggregation.
  - `GET /api/schemes`: Returns all schemes across the 24 domains.
  - `POST /api/config/groq-key`: Runtime API key management.

### C. Hybrid Reasoning Core
- **1. Natural Language Slot Extractor & Conversational Agent (`llm_explainer.py`):**
  - Uses **Groq API (`llama-3.3-70b-versatile`)** to extract unstructured demographic details into structured attributes.
  - Includes a regex/pattern-based NLP fallback engine for 100% uptime and offline reliability.
- **2. Deterministic Rule Engine (`rule_engine.py`):**
  - Strictly checks legal criteria (Age limits, Income ceilings, Gender prerequisites, Caste categories, State/Region, Rural/Urban area, Benchmark disability %, Maternity, Girl child age, Greenfield project status, Non-taxpayer condition).
- **3. Near-Miss Engine (`near_miss.py`):**
  - Identifies boundary candidates failing 1 or 2 soft criteria and computes exact quantitative gaps with actionable advice.
- **4. Ranking Engine (`ranking.py`):**
  - Scores recommendations: $\text{Rank Score} = (\text{Match Score} \times 0.6) + (\text{Log-Scaled Financial Benefit} \times 0.4)$.
- **5. Document Checklist Aggregator (`document_checklist.py`):**
  - Separates universal identity proofs (Aadhaar, PAN, Bank Passbook, Photos) from scheme-specific proofs (DPR, RoR Land extract, Caste/UDID certificates).

---

## 🏛️ 4. Decoupled 24-Domain Schema Matrix

```
Citizen Profile Attributes             Standardized Scheme Domains (24)
──────────────────────────             ────────────────────────────────
• Age, Gender, Social Category   ───►  1. Education & Scholarships
• Annual Household Income        ───►  2. Health & Medical (PM-JAY, PMMVY)
• State / District / Rural-Urban ───►  3. Housing & Shelter (PMAY)
• Primary Occupation             ───►  4. Banking & Insurance (PMSBY, PMJJBY, APY)
• Benchmark Disability (UDID %)  ───►  5. Women & Child Welfare (Sukanya Samriddhi)
• Maternity / Pregnancy Status   ───►  6. Agriculture & Allied (PM-KISAN, PMFBY)
• Girl Child (& Age)             ───►  7. MSME & Entrepreneurship (PMEGP, MUDRA)
• Available Rooftop Solar Space  ───►  8. Employment & Skill Development (PMKVY)
• BPL / Antyodaya Ration Card    ───►  9. Disability & Accessibility (ADIP Scheme)
• e-Shram / Unorganised Worker   ───►  10. Senior Citizens & Pensions (IGNOAPS)
• Greenfield / New Venture       ───►  11. Social Justice & Empowerment
• Landholding Size (Acres)       ───►  12-24. Environment, Rural/Urban, Handloom, etc.
```

---

## 🛡️ 5. Non-Functional & Quality Attributes

| Attribute | Implementation Strategy |
| :--- | :--- |
| **Determinism & Trust** | Financial eligibility and legal caps are computed by mathematical Python rules, avoiding LLM hallucinations. |
| **Explainability** | Every matched scheme displays a transparent point-by-point breakdown of which citizen attributes matched the scheme rules. |
| **Resilience & Fallback** | The platform functions completely even if offline or if no LLM API key is present via deterministic fallback reasoning. |
| **Extensibility** | Adding new government schemes requires simply adding a JSON entry to `schemes_db.json` without frontend code changes. |
| **Exportability** | 1-Click client-side PDF document checklist generation and Markdown export for offline use. |
