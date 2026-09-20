import React from "react";
import { 
  X, 
  ExternalLink, 
  CheckCircle2, 
  Building, 
  Coins, 
  FileText, 
  Layers, 
  UserCheck 
} from "lucide-react";

export default function SchemeDetailModal({ scheme, onClose }) {
  if (!scheme) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-xs animate-fade-in">
      <div className="bg-white rounded-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto shadow-2xl border border-slate-200">
        
        {/* Header */}
        <div className="sticky top-0 bg-white/95 backdrop-blur-md px-6 py-4 border-b border-slate-100 flex items-center justify-between z-10">
          <div>
            <span className="text-[10px] font-extrabold uppercase tracking-wider bg-blue-100 text-blue-800 px-2 py-0.5 rounded-full border border-blue-200">
              {scheme.category}
            </span>
            <h2 className="text-lg font-extrabold text-slate-900 mt-1">
              {scheme.name}
            </h2>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-slate-700 hover:bg-slate-100 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="p-6 space-y-5 text-xs sm:text-sm">
          
          {/* Ministry */}
          <div className="flex items-center gap-2 text-slate-600 bg-slate-50 p-3 rounded-xl border border-slate-200/70">
            <Building className="w-4 h-4 text-blue-600 shrink-0" />
            <span className="font-semibold">{scheme.ministry}</span>
          </div>

          {/* Description */}
          <div>
            <h4 className="font-bold text-slate-900 mb-1 text-xs uppercase tracking-wider text-slate-500">
              Overview & Objective
            </h4>
            <p className="text-slate-700 leading-relaxed bg-slate-50/50 p-3 rounded-xl border border-slate-100">
              {scheme.description}
            </p>
          </div>

          {/* Financial Benefits */}
          <div className="bg-emerald-50/60 border border-emerald-200/80 rounded-xl p-4">
            <div className="flex items-center gap-2 text-emerald-900 font-bold text-xs uppercase tracking-wider mb-1">
              <Coins className="w-4 h-4 text-emerald-700" />
              <span>Financial Benefits & Subsidies</span>
            </div>
            <p className="text-emerald-950 font-extrabold text-sm sm:text-base mt-1">
              {scheme.max_subsidy_or_loan}
            </p>
            {scheme.subsidy_percentage && (
              <p className="text-xs font-semibold text-emerald-800 mt-1">
                {scheme.subsidy_percentage}
              </p>
            )}
          </div>

          {/* Key Benefits List */}
          {scheme.key_benefits && scheme.key_benefits.length > 0 && (
            <div>
              <h4 className="font-bold text-slate-900 mb-2 text-xs uppercase tracking-wider text-slate-500">
                Key Features & Provisions
              </h4>
              <ul className="space-y-1.5">
                {scheme.key_benefits.map((b, idx) => (
                  <li key={idx} className="flex items-start gap-2 text-slate-700 text-xs">
                    <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 shrink-0 mt-0.5" />
                    <span>{b}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* Required Documents */}
          <div>
            <h4 className="font-bold text-slate-900 mb-2 text-xs uppercase tracking-wider text-slate-500 flex items-center gap-1.5">
              <FileText className="w-4 h-4 text-blue-600" />
              <span>Required Documents ({scheme.required_documents?.length || 0})</span>
            </h4>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
              {scheme.required_documents?.map((doc, idx) => (
                <div key={idx} className="p-2.5 rounded-lg bg-slate-50 border border-slate-200/80 text-xs text-slate-800 font-medium">
                  • {doc}
                </div>
              ))}
            </div>
          </div>

        </div>

        {/* Footer */}
        <div className="sticky bottom-0 bg-slate-50 px-6 py-4 border-t border-slate-200 flex items-center justify-between">
          <button
            onClick={onClose}
            className="px-4 py-2 text-xs font-bold text-slate-600 hover:text-slate-800 transition-colors"
          >
            Close
          </button>

          <a
            href={scheme.apply_link}
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center gap-2 px-5 py-2.5 bg-blue-600 hover:bg-blue-700 text-white rounded-xl font-bold text-xs shadow-md shadow-blue-500/20 transition-all"
          >
            <span>Apply on Official Portal</span>
            <ExternalLink className="w-4 h-4" />
          </a>
        </div>

      </div>
    </div>
  );
}
