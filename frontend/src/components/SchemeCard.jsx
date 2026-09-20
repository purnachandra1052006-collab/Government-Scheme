import React, { useState } from "react";
import { 
  CheckCircle2, 
  AlertTriangle, 
  ExternalLink, 
  ChevronDown, 
  ChevronUp, 
  FileText, 
  Sparkles, 
  Award, 
  ShieldCheck,
  Building,
  Coins,
  ArrowRight
} from "lucide-react";

export default function SchemeCard({ match, onSelectScheme, onViewDocuments }) {
  const [isExpanded, setIsExpanded] = useState(false);
  const { scheme, match_type, match_score, reasoning, near_miss_info } = match;
  const isDirect = match_type === "direct";

  return (
    <div
      className={`rounded-2xl border transition-all duration-200 overflow-hidden bg-white shadow-sm hover:shadow-md ${
        isDirect
          ? "border-emerald-200 ring-1 ring-emerald-100"
          : "border-amber-200 ring-1 ring-amber-100 bg-amber-50/20"
      }`}
    >
      {/* Top Banner Stripe */}
      <div
        className={`px-5 py-3 flex items-center justify-between border-b ${
          isDirect
            ? "bg-gradient-to-r from-emerald-50 via-teal-50 to-white border-emerald-100"
            : "bg-gradient-to-r from-amber-50 via-yellow-50 to-white border-amber-100"
        }`}
      >
        <div className="flex items-center gap-2">
          {isDirect ? (
            <span className="inline-flex items-center gap-1.5 text-xs font-extrabold uppercase tracking-wider text-emerald-800 bg-emerald-100/90 border border-emerald-300/80 px-2.5 py-0.5 rounded-full shadow-xs">
              <CheckCircle2 className="w-3.5 h-3.5 text-emerald-700" />
              Direct Eligible
            </span>
          ) : (
            <span className="inline-flex items-center gap-1.5 text-xs font-extrabold uppercase tracking-wider text-amber-800 bg-amber-100 border border-amber-300 px-2.5 py-0.5 rounded-full shadow-xs">
              <AlertTriangle className="w-3.5 h-3.5 text-amber-700" />
              Near-Miss (Action Required)
            </span>
          )}

          <span className="text-xs text-slate-500 font-medium hidden sm:inline">
            {scheme.category}
          </span>
        </div>

        {/* Match Score Badge */}
        <div className="flex items-center gap-1.5">
          <span className="text-[11px] font-semibold text-slate-500">Match Score:</span>
          <span
            className={`text-xs font-black px-2 py-0.5 rounded-md ${
              isDirect
                ? "bg-emerald-600 text-white"
                : "bg-amber-600 text-white"
            }`}
          >
            {Math.round(match_score)}%
          </span>
        </div>
      </div>

      {/* Main Body */}
      <div className="p-5">
        
        {/* Scheme Name & Ministry */}
        <div className="mb-3">
          <h3 className="font-extrabold text-base sm:text-lg text-slate-900 leading-snug">
            {scheme.name}
          </h3>
          <div className="flex items-center gap-1.5 text-xs text-slate-500 mt-1">
            <Building className="w-3.5 h-3.5 text-slate-400" />
            <span>{scheme.ministry}</span>
          </div>
        </div>

        {/* Description */}
        <p className="text-xs sm:text-sm text-slate-600 line-clamp-2 mb-4 leading-relaxed">
          {scheme.description}
        </p>

        {/* Financial Benefit Callout */}
        <div className="bg-slate-50 border border-slate-200/80 rounded-xl p-3.5 mb-4 flex items-start gap-3">
          <div className="w-9 h-9 rounded-lg bg-emerald-100 text-emerald-800 flex items-center justify-center shrink-0 mt-0.5 font-bold">
            <Coins className="w-5 h-5 text-emerald-700" />
          </div>
          <div>
            <span className="text-[11px] font-bold text-slate-500 uppercase tracking-wider">
              Maximum Financial Benefit & Subsidies
            </span>
            <p className="font-extrabold text-sm sm:text-base text-emerald-900 leading-tight mt-0.5">
              {scheme.max_subsidy_or_loan}
            </p>
            {scheme.subsidy_percentage && (
              <span className="inline-block text-[11px] font-semibold text-emerald-700 mt-1">
                ⚡ {scheme.subsidy_percentage}
              </span>
            )}
          </div>
        </div>

        {/* Near-Miss Remediation Notice (If Near Miss) */}
        {!isDirect && near_miss_info && (
          <div className="bg-amber-50 border border-amber-200 rounded-xl p-3.5 mb-4 space-y-2">
            <div className="flex items-center gap-1.5 text-xs font-bold text-amber-900">
              <AlertTriangle className="w-4 h-4 text-amber-600 shrink-0" />
              <span>Eligibility Gap Analysis:</span>
            </div>
            <p className="text-xs text-amber-800 leading-relaxed font-medium">
              {near_miss_info.gap_explanation}
            </p>
            <div className="bg-white/80 rounded-lg p-2.5 border border-amber-200/60 mt-2">
              <span className="text-[11px] font-bold text-slate-700 block uppercase tracking-wider">
                💡 How You Can Qualify:
              </span>
              <p className="text-xs text-slate-800 font-semibold mt-0.5">
                {near_miss_info.how_to_qualify}
              </p>
            </div>
          </div>
        )}

        {/* 'Why You Qualify' Breakdown (Accordion) */}
        <div className="border border-slate-100 rounded-xl overflow-hidden mb-4">
          <button
            onClick={() => setIsExpanded(!isExpanded)}
            className="w-full flex items-center justify-between px-4 py-2.5 bg-slate-50/80 hover:bg-slate-100 text-left transition-colors"
          >
            <div className="flex items-center gap-2">
              <ShieldCheck className="w-4 h-4 text-blue-600" />
              <span className="text-xs font-bold text-slate-800">
                {isDirect ? "Why You Qualify (Reasoning Breakdown)" : "Matched Criteria Breakdown"}
              </span>
            </div>
            {isExpanded ? (
              <ChevronUp className="w-4 h-4 text-slate-500" />
            ) : (
              <ChevronDown className="w-4 h-4 text-slate-500" />
            )}
          </button>

          {isExpanded && (
            <div className="p-4 bg-white border-t border-slate-100 space-y-3 animate-fade-in">
              {/* Point-by-point reasons */}
              <div>
                <span className="text-[11px] font-bold text-slate-500 uppercase tracking-wider block mb-2">
                  Matching Attributes:
                </span>
                <ul className="space-y-1.5">
                  {reasoning.why_you_qualify.map((reason, idx) => (
                    <li key={idx} className="flex items-start gap-2 text-xs text-slate-700">
                      <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 shrink-0 mt-0.5" />
                      <span>{reason}</span>
                    </li>
                  ))}
                </ul>
              </div>

              {/* Key Benefits */}
              {scheme.key_benefits && scheme.key_benefits.length > 0 && (
                <div className="pt-2 border-t border-slate-100">
                  <span className="text-[11px] font-bold text-slate-500 uppercase tracking-wider block mb-1.5">
                    Key Scheme Features:
                  </span>
                  <ul className="space-y-1">
                    {scheme.key_benefits.map((b, idx) => (
                      <li key={idx} className="text-xs text-slate-600 flex items-start gap-1.5">
                        <span className="text-blue-500 font-bold">•</span>
                        <span>{b}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          )}
        </div>

        {/* Footer Actions */}
        <div className="flex flex-wrap items-center justify-between gap-2 pt-2 border-t border-slate-100">
          
          <button
            onClick={() => onViewDocuments(scheme)}
            className="flex items-center gap-1.5 text-xs font-semibold text-slate-700 hover:text-blue-700 bg-slate-100 hover:bg-blue-50 px-3 py-2 rounded-lg transition-colors"
          >
            <FileText className="w-3.5 h-3.5 text-slate-500" />
            <span>Required Documents ({scheme.required_documents?.length || 0})</span>
          </button>

          <a
            href={scheme.apply_link}
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center gap-1.5 text-xs font-bold text-white bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-lg shadow-sm shadow-blue-500/20 transition-all hover:translate-x-0.5"
          >
            <span>Official Portal</span>
            <ExternalLink className="w-3.5 h-3.5" />
          </a>

        </div>

      </div>
    </div>
  );
}
