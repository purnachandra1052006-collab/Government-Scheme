import React, { useState, useEffect } from "react";
import confetti from "canvas-confetti";
import { 
  Building2, 
  Sparkles, 
  CheckCircle2, 
  AlertTriangle, 
  Layers, 
  Coins, 
  FileText, 
  ArrowLeft, 
  RotateCcw,
  SlidersHorizontal,
  FolderCheck,
  TrendingUp
} from "lucide-react";

import Navbar from "./components/Navbar";
import ChatIntake from "./components/ChatIntake";
import QuickFormIntake from "./components/QuickFormIntake";
import ProfileSummaryDrawer from "./components/ProfileSummaryDrawer";
import SchemeCard from "./components/SchemeCard";
import DocumentChecklist from "./components/DocumentChecklist";
import SchemeComparison from "./components/SchemeComparison";
import SchemeCatalog from "./components/SchemeCatalog";
import SchemeDetailModal from "./components/SchemeDetailModal";
import GroqKeyModal from "./components/GroqKeyModal";

import { evaluateProfile, checkHealth } from "./services/api";

export default function App() {
  const [activeTab, setActiveTab] = useState("chat"); // 'chat' | 'wizard' | 'catalog'
  const [profile, setProfile] = useState({});
  const [evaluation, setEvaluation] = useState(null);
  const [isEvaluating, setIsEvaluating] = useState(false);
  const [selectedSchemeForModal, setSelectedSchemeForModal] = useState(null);
  const [showGroqModal, setShowGroqModal] = useState(false);
  const [groqConfigured, setGroqConfigured] = useState(false);
  const [resultsFilter, setResultsFilter] = useState("all"); // 'all' | 'direct' | 'near_miss'

  useEffect(() => {
    checkHealth().then((res) => {
      setGroqConfigured(res.groq_configured);
    });
  }, []);

  const triggerConfetti = () => {
    try {
      confetti({
        particleCount: 80,
        spread: 70,
        origin: { y: 0.6 },
        colors: ["#FF9933", "#138808", "#000080", "#2563eb"],
      });
    } catch (e) {
      // ignore
    }
  };

  const handleRunEvaluation = async (profileToEval) => {
    setIsEvaluating(true);
    try {
      const res = await evaluateProfile(profileToEval || profile);
      setEvaluation(res);
      if (res.total_direct_count > 0) {
        triggerConfetti();
      }
    } catch (err) {
      console.error("Evaluation error:", err);
      alert(`Evaluation failed: ${err.message || "Please check backend server"}`);
    } finally {
      setIsEvaluating(false);
    }
  };

  const handleSelectSampleProfile = (sample) => {
    setProfile(sample);
    handleRunEvaluation(sample);
  };

  const handleResetProfile = () => {
    setProfile({});
    setEvaluation(null);
  };

  const filteredDirect = evaluation?.direct_matches || [];
  const filteredNearMiss = evaluation?.near_miss_matches || [];

  return (
    <div className="min-h-screen flex flex-col bg-slate-50 text-slate-900 selection:bg-blue-600 selection:text-white">
      
      {/* Top Navbar */}
      <Navbar
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        onSelectSampleProfile={handleSelectSampleProfile}
        onOpenGroqModal={() => setShowGroqModal(true)}
        groqConfigured={groqConfigured}
      />

      {/* Main Content Container */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8">
        
        {/* TAB 1: Scheme Catalog Directory */}
        {activeTab === "catalog" && (
          <SchemeCatalog
            onViewScheme={(scheme) => setSelectedSchemeForModal(scheme)}
            onViewDocuments={(scheme) => setSelectedSchemeForModal(scheme)}
          />
        )}

        {/* TAB 2: Conversational Intake or Form Wizard */}
        {(activeTab === "chat" || activeTab === "wizard") && (
          <div className="space-y-8">
            
            {/* Top Banner & Mode Switcher */}
            <div className="bg-gradient-to-r from-blue-900 via-indigo-900 to-slate-900 text-white rounded-3xl p-6 sm:p-8 shadow-xl relative overflow-hidden">
              <div className="absolute -right-12 -top-12 w-64 h-64 rounded-full bg-blue-500/10 blur-3xl" />
              <div className="absolute -left-12 -bottom-12 w-64 h-64 rounded-full bg-amber-500/10 blur-3xl" />
              
              <div className="relative z-10 max-w-3xl">
                <h1 className="text-2xl sm:text-4xl font-extrabold tracking-tight leading-tight">
                  Discover Government Schemes, Grants & Subsidies Tailored for You
                </h1>
                <p className="text-sm sm:text-base text-slate-300 mt-2 font-medium leading-relaxed">
                  Our hybrid reasoning engine verifies eligibility rules, finds near-miss opportunities, computes match scores, and provides a consolidated required documents checklist.
                </p>
              </div>
            </div>

            {/* If Results are Generated: Show Results Dashboard */}
            {evaluation ? (
              <div className="space-y-8 animate-fade-in">
                
                {/* Results Summary Header */}
                <div className="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
                  <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 border-b border-slate-100 pb-5 mb-5">
                    <div>
                      <div className="flex items-center gap-2">
                        <span className="text-xs font-bold text-blue-600 uppercase tracking-wider bg-blue-50 px-2.5 py-0.5 rounded-full border border-blue-200">
                          Assessment Complete
                        </span>
                      </div>
                      <h2 className="text-xl sm:text-2xl font-extrabold text-slate-900 mt-1">
                        Your Scheme Eligibility Results
                      </h2>
                      <p className="text-xs sm:text-sm text-slate-600 mt-1 max-w-3xl leading-relaxed">
                        {evaluation.summary_insight}
                      </p>
                    </div>

                    <div className="flex items-center gap-2 shrink-0">
                      <button
                        onClick={handleResetProfile}
                        className="flex items-center gap-1.5 px-4 py-2 text-xs font-bold text-slate-700 bg-slate-100 hover:bg-slate-200 rounded-xl transition-colors"
                      >
                        <RotateCcw className="w-3.5 h-3.5" />
                        <span>Start New Assessment</span>
                      </button>
                    </div>
                  </div>

                  {/* Summary Metric Counters */}
                  <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
                    
                    <div className="bg-emerald-50/70 border border-emerald-200 rounded-xl p-4 flex items-center gap-3.5">
                      <div className="w-10 h-10 rounded-xl bg-emerald-600 text-white flex items-center justify-center font-black text-lg shadow-sm">
                        {evaluation.total_direct_count}
                      </div>
                      <div>
                        <span className="text-[11px] font-bold text-emerald-800 uppercase tracking-wider block">
                          Direct Matches
                        </span>
                        <p className="text-xs text-emerald-950 font-semibold mt-0.5">
                          100% hard criteria satisfied
                        </p>
                      </div>
                    </div>

                    <div className="bg-amber-50/70 border border-amber-200 rounded-xl p-4 flex items-center gap-3.5">
                      <div className="w-10 h-10 rounded-xl bg-amber-600 text-white flex items-center justify-center font-black text-lg shadow-sm">
                        {evaluation.total_near_miss_count}
                      </div>
                      <div>
                        <span className="text-[11px] font-bold text-amber-800 uppercase tracking-wider block">
                          Near-Miss Schemes
                        </span>
                        <p className="text-xs text-amber-950 font-semibold mt-0.5">
                          Actionable criteria gap detected
                        </p>
                      </div>
                    </div>

                    <div className="bg-blue-50/70 border border-blue-200 rounded-xl p-4 flex items-center gap-3.5">
                      <div className="w-10 h-10 rounded-xl bg-blue-600 text-white flex items-center justify-center font-black text-lg shadow-sm">
                        {evaluation.consolidated_documents.total_unique_documents}
                      </div>
                      <div>
                        <span className="text-[11px] font-bold text-blue-800 uppercase tracking-wider block">
                          Total Unique Documents
                        </span>
                        <p className="text-xs text-blue-950 font-semibold mt-0.5">
                          Deduplicated checklist generated
                        </p>
                      </div>
                    </div>

                  </div>
                </div>

                {/* Filter Pills */}
                <div className="flex items-center gap-2">
                  <button
                    onClick={() => setResultsFilter("all")}
                    className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all ${
                      resultsFilter === "all"
                        ? "bg-slate-900 text-white shadow-xs"
                        : "bg-white text-slate-600 border border-slate-200 hover:bg-slate-100"
                    }`}
                  >
                    All Schemes ({evaluation.total_direct_count + evaluation.total_near_miss_count})
                  </button>

                  <button
                    onClick={() => setResultsFilter("direct")}
                    className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all ${
                      resultsFilter === "direct"
                        ? "bg-emerald-700 text-white shadow-xs"
                        : "bg-white text-emerald-800 border border-emerald-200 hover:bg-emerald-50"
                    }`}
                  >
                    Direct Eligible ({evaluation.total_direct_count})
                  </button>

                  <button
                    onClick={() => setResultsFilter("near_miss")}
                    className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all ${
                      resultsFilter === "near_miss"
                        ? "bg-amber-600 text-white shadow-xs"
                        : "bg-white text-amber-800 border border-amber-200 hover:bg-amber-50"
                    }`}
                  >
                    Near-Miss Opportunities ({evaluation.total_near_miss_count})
                  </button>
                </div>

                {/* Scheme Cards Grid */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  {(resultsFilter === "all" || resultsFilter === "direct") &&
                    filteredDirect.map((match) => (
                      <SchemeCard
                        key={match.scheme.id}
                        match={match}
                        onSelectScheme={(s) => setSelectedSchemeForModal(s)}
                        onViewDocuments={(s) => setSelectedSchemeForModal(s)}
                      />
                    ))}

                  {(resultsFilter === "all" || resultsFilter === "near_miss") &&
                    filteredNearMiss.map((match) => (
                      <SchemeCard
                        key={match.scheme.id}
                        match={match}
                        onSelectScheme={(s) => setSelectedSchemeForModal(s)}
                        onViewDocuments={(s) => setSelectedSchemeForModal(s)}
                      />
                    ))}
                </div>

                {/* Interactive Document Checklist Component */}
                <DocumentChecklist
                  consolidatedDocs={evaluation.consolidated_documents}
                  directMatches={evaluation.direct_matches}
                  nearMissMatches={evaluation.near_miss_matches}
                />

                {/* Scheme Comparison Table */}
                <SchemeComparison
                  directMatches={evaluation.direct_matches}
                  nearMissMatches={evaluation.near_miss_matches}
                  onViewDocuments={(s) => setSelectedSchemeForModal(s)}
                />

              </div>
            ) : (
              /* Intake Modes: Conversational Chat or Wizard Form */
              <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 items-start">
                
                {/* Main Intake Area (2 cols) */}
                <div className="lg:col-span-2">
                  {activeTab === "chat" ? (
                    <ChatIntake
                      profile={profile}
                      setProfile={setProfile}
                      onCompleteEvaluation={handleRunEvaluation}
                      isEvaluating={isEvaluating}
                    />
                  ) : (
                    <QuickFormIntake
                      profile={profile}
                      setProfile={setProfile}
                      onEvaluate={handleRunEvaluation}
                      isEvaluating={isEvaluating}
                    />
                  )}
                </div>

                {/* Live Profile Sidebar (1 col) */}
                <div className="lg:col-span-1 space-y-5">
                  <ProfileSummaryDrawer
                    profile={profile}
                    onReset={handleResetProfile}
                    isEvaluating={isEvaluating}
                  />

                  {/* Quick Evaluate Button if partial data exists */}
                  {Object.keys(profile).length >= 3 && (
                    <button
                      onClick={() => handleRunEvaluation(profile)}
                      disabled={isEvaluating}
                      className="w-full py-3 px-4 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white rounded-2xl font-extrabold text-xs shadow-md shadow-blue-500/20 transition-all flex items-center justify-center gap-2"
                    >
                      <Sparkles className="w-4 h-4 text-amber-300" />
                      <span>{isEvaluating ? "Evaluating Rules..." : "Evaluate Current Profile Now"}</span>
                    </button>
                  )}
                </div>

              </div>
            )}

          </div>
        )}

      </main>

      {/* Modals */}
      <SchemeDetailModal
        scheme={selectedSchemeForModal}
        onClose={() => setSelectedSchemeForModal(null)}
      />

      <GroqKeyModal
        isOpen={showGroqModal}
        onClose={() => setShowGroqModal(false)}
        onKeySaved={() => setGroqConfigured(true)}
        currentConfigured={groqConfigured}
      />

      {/* Footer */}
      <footer className="bg-white border-t border-slate-200 py-6 mt-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-slate-500">
          <div className="flex items-center gap-2">
            <Building2 className="w-4 h-4 text-blue-600" />
            <span className="font-bold text-slate-800">GovScheme.AI</span>
            <span>• National Scheme Eligibility & Benefit Matching Engine</span>
          </div>
          <p>Official Indian Schemes</p>
        </div>
      </footer>

    </div>
  );
}
