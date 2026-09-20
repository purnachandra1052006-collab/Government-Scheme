import React, { useState } from "react";
import { 
  Building2, 
  Sparkles, 
  Key, 
  CheckCircle2, 
  MessageSquare, 
  FileSpreadsheet, 
  BookOpen, 
  HelpCircle,
  ShieldAlert
} from "lucide-react";
import { SAMPLE_PROFILES } from "../data/sampleProfiles";

export default function Navbar({ 
  activeTab, 
  setActiveTab, 
  onSelectSampleProfile, 
  onOpenGroqModal, 
  groqConfigured 
}) {
  const [showSampleDropdown, setShowSampleDropdown] = useState(false);

  return (
    <header className="sticky top-0 z-40 bg-white/90 backdrop-blur-md border-b border-slate-200 shadow-sm">
      {/* Tricolor top indicator stripe */}
      <div className="h-1.5 w-full bg-gradient-to-r from-[#FF9933] via-white via-slate-300 to-[#138808]" />
      
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          
          {/* Logo and Brand */}
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-700 via-indigo-600 to-amber-500 flex items-center justify-center text-white shadow-md shadow-blue-500/20">
              <Building2 className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-extrabold text-lg sm:text-xl tracking-tight text-slate-900">
                  GovScheme<span className="text-blue-600">.AI</span>
                </span>
              </div>
              <p className="text-xs text-slate-500 font-medium hidden sm:block">
                National Scheme Eligibility & Benefit Matching Engine
              </p>
            </div>
          </div>

          {/* Navigation Mode Tabs */}
          <nav className="flex items-center gap-1 sm:gap-2">
            <button
              onClick={() => setActiveTab("chat")}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs sm:text-sm font-semibold transition-all ${
                activeTab === "chat"
                  ? "bg-blue-600 text-white shadow-sm shadow-blue-500/30"
                  : "text-slate-600 hover:text-slate-900 hover:bg-slate-100"
              }`}
            >
              <MessageSquare className="w-4 h-4" />
              <span className="hidden md:inline">Conversational Intake</span>
              <span className="md:hidden">AI Intake</span>
            </button>

            <button
              onClick={() => setActiveTab("wizard")}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs sm:text-sm font-semibold transition-all ${
                activeTab === "wizard"
                  ? "bg-blue-600 text-white shadow-sm shadow-blue-500/30"
                  : "text-slate-600 hover:text-slate-900 hover:bg-slate-100"
              }`}
            >
              <FileSpreadsheet className="w-4 h-4" />
              <span className="hidden md:inline">Quick Assessment</span>
              <span className="md:hidden">Form</span>
            </button>

            <button
              onClick={() => setActiveTab("catalog")}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs sm:text-sm font-semibold transition-all ${
                activeTab === "catalog"
                  ? "bg-blue-600 text-white shadow-sm shadow-blue-500/30"
                  : "text-slate-600 hover:text-slate-900 hover:bg-slate-100"
              }`}
            >
              <BookOpen className="w-4 h-4" />
              <span className="hidden md:inline">Scheme Directory</span>
              <span className="md:hidden">Schemes</span>
            </button>
          </nav>

          {/* Action Buttons: Sample Profiles & Groq Key */}
          <div className="flex items-center gap-2">
            
            {/* Sample Profile Selector Dropdown */}
            <div className="relative">
              <button
                onClick={() => setShowSampleDropdown(!showSampleDropdown)}
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-amber-50 text-amber-900 border border-amber-200 hover:bg-amber-100 transition-colors shadow-xs"
              >
                <Sparkles className="w-3.5 h-3.5 text-amber-600" />
                <span className="hidden lg:inline">Test Profiles</span>
                <span className="lg:hidden">Presets</span>
              </button>

              {showSampleDropdown && (
                <div className="absolute right-0 mt-2 w-80 bg-white border border-slate-200 rounded-xl shadow-xl py-2 z-50 animate-slide-up">
                  <div className="px-3 py-1.5 border-b border-slate-100 text-xs font-bold text-slate-500 uppercase tracking-wider">
                    Select a Preset Citizen Profile
                  </div>
                  <div className="max-h-80 overflow-y-auto divide-y divide-slate-50">
                    {SAMPLE_PROFILES.map((sample) => (
                      <button
                        key={sample.id}
                        onClick={() => {
                          onSelectSampleProfile(sample.profile);
                          setShowSampleDropdown(false);
                        }}
                        className="w-full text-left px-3 py-2.5 hover:bg-blue-50/70 transition-colors group"
                      >
                        <div className="text-xs font-bold text-slate-800 group-hover:text-blue-700">
                          {sample.title}
                        </div>
                        <div className="text-[11px] text-slate-500 line-clamp-1 mt-0.5">
                          {sample.description}
                        </div>
                        <div className="inline-block mt-1 text-[10px] font-semibold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200/60">
                          {sample.badge}
                        </div>
                      </button>
                    ))}
                  </div>
                </div>
              )}
            </div>

            {/* Groq LLM Key Button */}
            <button
              onClick={onOpenGroqModal}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold border transition-all ${
                groqConfigured
                  ? "bg-emerald-50 text-emerald-800 border-emerald-200 hover:bg-emerald-100"
                  : "bg-slate-100 text-slate-700 border-slate-300 hover:bg-slate-200"
              }`}
              title="Configure Groq API Key for Llama-3.3 Reasoning"
            >
              <Key className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">Groq LLM</span>
              {groqConfigured ? (
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
              ) : (
                <span className="w-2 h-2 rounded-full bg-amber-500" />
              )}
            </button>

          </div>

        </div>
      </div>
    </header>
  );
}
