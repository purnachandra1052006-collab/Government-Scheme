import React from "react";
import { 
  Building, 
  Coins, 
  CheckCircle2, 
  AlertTriangle, 
  ExternalLink, 
  FileText,
  ShieldCheck 
} from "lucide-react";

export default function SchemeComparison({ directMatches, nearMissMatches, onViewDocuments }) {
  const allMatches = [...(directMatches || []), ...(nearMissMatches || [])];

  if (!allMatches.length) {
    return null;
  }

  return (
    <div className="bg-white rounded-2xl border border-slate-200 shadow-sm p-5 sm:p-6 overflow-hidden">
      <div className="mb-4">
        <h3 className="font-extrabold text-base sm:text-lg text-slate-900">
          Scheme Feature & Benefit Comparison
        </h3>
        <p className="text-xs text-slate-500 mt-0.5">
          Side-by-side financial benefits, eligibility rules, and application requirements
        </p>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full text-left border-collapse min-w-[700px]">
          <thead>
            <tr className="bg-slate-50 text-slate-700 text-xs font-bold border-b border-slate-200">
              <th className="py-3 px-4 rounded-l-lg">Scheme & Ministry</th>
              <th className="py-3 px-4">Status</th>
              <th className="py-3 px-4">Max Benefit / Loan</th>
              <th className="py-3 px-4">Subsidy / Concession</th>
              <th className="py-3 px-4">Key Criteria</th>
              <th className="py-3 px-4 rounded-r-lg text-right">Action</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100 text-xs text-slate-700">
            {allMatches.map((match, idx) => {
              const { scheme, match_type } = match;
              const isDirect = match_type === "direct";

              return (
                <tr key={idx} className="hover:bg-slate-50/70 transition-colors">
                  
                  {/* Scheme Name */}
                  <td className="py-3.5 px-4 font-bold text-slate-900">
                    <div className="max-w-[220px]">
                      <div className="font-extrabold text-slate-900 line-clamp-1">{scheme.name}</div>
                      <div className="text-[11px] text-slate-500 font-normal line-clamp-1">{scheme.ministry}</div>
                    </div>
                  </td>

                  {/* Status */}
                  <td className="py-3.5 px-4">
                    {isDirect ? (
                      <span className="inline-flex items-center gap-1 text-[11px] font-bold text-emerald-800 bg-emerald-50 border border-emerald-200 px-2 py-0.5 rounded-full">
                        <CheckCircle2 className="w-3 h-3 text-emerald-600" />
                        Direct Eligible
                      </span>
                    ) : (
                      <span className="inline-flex items-center gap-1 text-[11px] font-bold text-amber-800 bg-amber-50 border border-amber-200 px-2 py-0.5 rounded-full">
                        <AlertTriangle className="w-3 h-3 text-amber-600" />
                        Near Miss
                      </span>
                    )}
                  </td>

                  {/* Benefit */}
                  <td className="py-3.5 px-4 font-extrabold text-emerald-800 max-w-[180px]">
                    <span className="line-clamp-2">{scheme.max_subsidy_or_loan}</span>
                  </td>

                  {/* Subsidy */}
                  <td className="py-3.5 px-4 text-slate-600 font-medium">
                    {scheme.subsidy_percentage || "Direct Subsidy / Concession"}
                  </td>

                  {/* Key Criteria */}
                  <td className="py-3.5 px-4 text-slate-500 text-[11px] max-w-[160px]">
                    <div className="line-clamp-2">
                      Age: {scheme.min_age || 0}-{scheme.max_age || "No limit"} • 
                      Income: {scheme.max_income ? `≤₹${scheme.max_income/100000}L` : "No limit"}
                    </div>
                  </td>

                  {/* Action */}
                  <td className="py-3.5 px-4 text-right space-x-1.5 whitespace-nowrap">
                    <button
                      onClick={() => onViewDocuments(scheme)}
                      className="inline-flex items-center gap-1 text-slate-700 hover:text-blue-700 bg-slate-100 hover:bg-blue-50 px-2.5 py-1.5 rounded-md font-semibold transition-colors"
                      title="View Documents"
                    >
                      <FileText className="w-3.5 h-3.5" />
                      <span>Docs</span>
                    </button>

                    <a
                      href={scheme.apply_link}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="inline-flex items-center gap-1 text-white bg-blue-600 hover:bg-blue-700 px-2.5 py-1.5 rounded-md font-bold transition-all shadow-xs"
                    >
                      <span>Apply</span>
                      <ExternalLink className="w-3 h-3" />
                    </a>
                  </td>

                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}
