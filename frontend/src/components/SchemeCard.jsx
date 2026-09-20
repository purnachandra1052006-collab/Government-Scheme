import React, { useState } from "react";
import { 
  CheckCircle2, 
  AlertTriangle, 
  ExternalLink, 
  ChevronDown, 
  ChevronUp, 
  FileText, 
  Building,
  Coins,
  ShieldCheck,
  Tag
} from "lucide-react";

export default function SchemeCard({ match, onSelectScheme, onViewDocuments }) {
  const [isExpanded, setIsExpanded] = useState(false);
  const { scheme, match_type, match_score, reasoning, near_miss_info } = match;
  const isDirect = match_type === "direct";

  return (
    <div
      className={`rounded-3xl border transition-all duration-200 overflow-hidden bg-white shadow-sm hover:shadow-md ${
        isDirect
          ? "border-emerald-200 ring-1 ring-emerald-100"
          : "border-amber-200 ring-1 ring-amber-100 bg-amber-50/20"
      }`}
    >
      {/* Top Banner Stripe */}
      <div
        className={`px-6 py-3.5 flex items-center justify-between border-b ${
          isDirect
            ? "bg-gradient-to-r from-emerald-50 via-teal-50 to-white border-emerald-100"
            : "bg-gradient-to-r from-amber-50 via-yellow-50 to-white border-amber-100"
        }`}
      >
        <div className="flex items-center gap-2 flex-wrap">
          {isDirect ? (
            <span className="inline-flex items-center gap-1.5 text-[11px] font-extrabold uppercase tracking-wider text-emerald-800 bg-emerald-100/90 border border-emerald-300/80 px-2.5 py-0.5 rounded-full shadow-xs">
              <CheckCircle2 className="w-3.5 h-3.5 text-emerald-700" />
              Direct Eligible
            </span>
          ) : (
            <span className="inline-flex items-center gap-1.5 text-[11px] font-extrabold uppercase tracking-wider text-amber-800 bg-amber-100 border border-amber-300 px-2.5 py-0.5 rounded-full shadow-xs">
              <AlertTriangle className="w-3.5 h-3.5 text-amber-700" />
              Near-Miss (Action Needed)
            </span>
          )}

          <span className="text-[11px] font-bold text-blue-700 bg-blue-50 border border-blue-200 px-2 py-0.5 rounded-md">
            {scheme.category || scheme.domain}
          </span>

          {scheme.central_or_state === "State Government" || scheme.state_name ? (
            <span className="inline-flex items-center gap-1 text-[11px] font-bold text-purple-700 bg-purple-50 border border-purple-200 px-2 py-0.5 rounded-md">
              🏛️ {scheme.state_name || scheme.states_applicable?.[0] || "State"} Govt
            </span>
          ) : (
            <span className="inline-flex items-center gap-1 text-[11px] font-bold text-slate-700 bg-slate-100 border border-slate-200 px-2 py-0.5 rounded-md">
              🇮🇳 Central Govt
            </span>
          )}

          {scheme.beneficiary_level === "Family / Household" ? (
            <span className="inline-flex items-center gap-1 text-[11px] font-bold text-amber-800 bg-amber-50 border border-amber-200 px-2 py-0.5 rounded-md">
              👨‍👩‍👧 Family Welfare
            </span>
          ) : (
            <span className="inline-flex items-center gap-1 text-[11px] font-bold text-emerald-800 bg-emerald-50 border border-emerald-200 px-2 py-0.5 rounded-md">
              👤 Individual Benefit
            </span>
          )}
        </div>

        {/* Match Score Badge */}
        <div className="flex items-center gap-1.5">
          <span className="text-[11px] font-semibold text-slate-500">Score:</span>
          <span
            className={`text-xs font-black px-2.5 py-0.5 rounded-md ${
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
      <div className="p-6">
        
        {/* Scheme Name & Ministry */}
        <div className="mb-3">
          <div className="flex items-center justify-between gap-2">
            <h3 className="font-black text-base sm:text-lg text-slate-900 leading-snug">
              {scheme.name}
            </h3>
          </div>
          <div className="flex items-center gap-1.5 text-xs text-slate-500 mt-1">
            <Building className="w-3.5 h-3.5 text-slate-400 shrink-0" />
            <span className="line-clamp-1">{scheme.ministry}</span>
            <span className="text-slate-300">•</span>
            <span className="text-slate-600 font-semibold">{scheme.central_or_state || "Central"}</span>
          </div>
        </div>

        {/* Description */}
        <p className="text-xs sm:text-sm text-slate-600 line-clamp-2 mb-4 leading-relaxed">
          {scheme.description}
        </p>

        {/* Financial Benefit Callout */}
        <div className="bg-slate-50 border border-slate-200/80 rounded-2xl p-4 mb-4 flex items-start gap-3.5">
          <div className="w-10 h-10 rounded-xl bg-emerald-100 text-emerald-800 flex items-center justify-center shrink-0 mt-0.5 font-bold">
            <Coins className="w-5 h-5 text-emerald-700" />
          </div>
          <div>
            <span className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">
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
          <div className="bg-amber-50 border border-amber-200 rounded-2xl p-4 mb-4 space-y-2">
            <div className="flex items-center gap-1.5 text-xs font-bold text-amber-900">
              <AlertTriangle className="w-4 h-4 text-amber-600 shrink-0" />
              <span>Eligibility Gap Analysis:</span>
            </div>
            <p className="text-xs text-amber-800 leading-relaxed font-medium">
              {near_miss_info.gap_explanation}
            </p>
            <div className="bg-white/80 rounded-xl p-3 border border-amber-200/60 mt-2">
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
        <div className="border border-slate-100 rounded-2xl overflow-hidden mb-4">
          <button
            onClick={() => setIsExpanded(!isExpanded)}
            className="w-full flex items-center justify-between px-4 py-3 bg-slate-50/80 hover:bg-slate-100 text-left transition-colors"
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
              <div>
                <span className="text-[10px] font-bold text-slate-500 uppercase tracking-wider block mb-2">
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

              {scheme.key_benefits && scheme.key_benefits.length > 0 && (
                <div className="pt-2 border-t border-slate-100">
                  <span className="text-[10px] font-bold text-slate-500 uppercase tracking-wider block mb-1.5">
                    Key Scheme Provisions:
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
            className="flex items-center gap-1.5 text-xs font-bold text-slate-700 hover:text-blue-700 bg-slate-100 hover:bg-blue-50 px-3.5 py-2 rounded-xl transition-colors"
          >
            <FileText className="w-3.5 h-3.5 text-slate-500" />
            <span>Required Documents ({scheme.required_documents?.length || 0})</span>
          </button>

          <a
            href={scheme.apply_link}
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center gap-1.5 text-xs font-bold text-white bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-xl shadow-sm shadow-blue-500/20 transition-all hover:translate-x-0.5"
          >
            <span>Official Portal</span>
            <ExternalLink className="w-3.5 h-3.5" />
          </a>
        </div>

      </div>
    </div>
  );
}
