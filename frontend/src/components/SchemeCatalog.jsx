import React, { useState, useEffect } from "react";
import { 
  Search, 
  Filter, 
  Building2, 
  Coins, 
  ExternalLink, 
  FileText, 
  BookOpen, 
  Layers,
  Sparkles,
  CheckCircle2
} from "lucide-react";
import { getAllSchemes } from "../services/api";

export default function SchemeCatalog({ onViewScheme, onViewDocuments }) {
  const [schemes, setSchemes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState("");
  const [selectedDomain, setSelectedDomain] = useState("All");

  useEffect(() => {
    loadSchemes();
  }, []);

  const loadSchemes = async () => {
    try {
      const data = await getAllSchemes();
      setSchemes(data);
    } catch (err) {
      console.error("Failed to load catalog schemes:", err);
    } finally {
      setLoading(false);
    }
  };

  // Get distinct domains from schemes db
  const uniqueDomains = ["All", ...Array.from(new Set(schemes.map((s) => s.category || s.domain).filter(Boolean)))];

  const filteredSchemes = schemes.filter((s) => {
    const sDomain = s.category || s.domain || "";
    const matchesDomain = selectedDomain === "All" || sDomain === selectedDomain;

    const matchesSearch =
      s.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      s.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
      s.ministry.toLowerCase().includes(searchTerm.toLowerCase()) ||
      (s.target_beneficiaries && s.target_beneficiaries.some((b) => b.toLowerCase().includes(searchTerm.toLowerCase())));

    return matchesDomain && matchesSearch;
  });

  return (
    <div className="space-y-6">
      
      {/* Header & Search */}
      <div className="bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 shadow-sm">
        <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
          <div>
            <div className="inline-flex items-center gap-2 text-xs font-extrabold uppercase tracking-wider bg-blue-50 text-blue-700 px-3 py-1 rounded-full border border-blue-200 mb-2">
              <BookOpen className="w-3.5 h-3.5" />
              <span>National Scheme Directory (24 Domains)</span>
            </div>
            <h2 className="text-xl sm:text-2xl font-black text-slate-900">
              Explore Government Schemes & Welfare Programs
            </h2>
            <p className="text-xs sm:text-sm text-slate-500 mt-1 max-w-2xl">
              Browse official Indian central and state welfare initiatives across Health, Education, MSME, Agriculture, Disability, Social Security, and Green Energy.
            </p>
          </div>

          <div className="relative w-full lg:w-80">
            <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-3.5" />
            <input
              type="text"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              placeholder="Search by name, ministry, or benefit..."
              className="w-full pl-10 pr-4 py-2.5 text-xs sm:text-sm bg-slate-50 border border-slate-200 rounded-2xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
            />
          </div>
        </div>

        {/* 24-Domain Filter Chips */}
        <div className="mt-6 pt-5 border-t border-slate-100">
          <span className="text-[11px] font-bold text-slate-500 uppercase tracking-wider block mb-2.5">
            Filter by National Scheme Domain:
          </span>
          <div className="flex items-center gap-1.5 overflow-x-auto pb-2 scrollbar-thin">
            {uniqueDomains.map((domain, idx) => {
              const count = domain === "All" ? schemes.length : schemes.filter((s) => (s.category || s.domain) === domain).length;
              const isSelected = selectedDomain === domain;

              return (
                <button
                  key={idx}
                  onClick={() => setSelectedDomain(domain)}
                  className={`px-3 py-1.5 rounded-xl text-xs font-bold whitespace-nowrap transition-all flex items-center gap-1.5 ${
                    isSelected
                      ? "bg-blue-600 text-white shadow-sm shadow-blue-500/20"
                      : "bg-slate-100 text-slate-700 hover:bg-slate-200"
                  }`}
                >
                  <span>{domain}</span>
                  <span className={`text-[10px] px-1.5 py-0.2 rounded-md ${isSelected ? "bg-blue-700 text-white" : "bg-white text-slate-600"}`}>
                    {count}
                  </span>
                </button>
              );
            })}
          </div>
        </div>
      </div>

      {/* Grid of Scheme Cards */}
      {loading ? (
        <div className="text-center py-16">
          <div className="w-8 h-8 rounded-full border-2 border-blue-600 border-t-transparent animate-spin mx-auto mb-3" />
          <p className="text-xs text-slate-500">Loading scheme repository...</p>
        </div>
      ) : filteredSchemes.length === 0 ? (
        <div className="bg-white rounded-3xl border border-slate-200 p-12 text-center">
          <Search className="w-10 h-10 text-slate-300 mx-auto mb-3" />
          <h3 className="font-bold text-sm text-slate-800">No matching schemes found</h3>
          <p className="text-xs text-slate-500 mt-1">Try selecting a different domain or clearing your search term.</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredSchemes.map((scheme) => (
            <div
              key={scheme.id}
              className="bg-white rounded-3xl border border-slate-200 p-6 shadow-sm hover:shadow-md transition-all flex flex-col justify-between group"
            >
              <div>
                <div className="flex items-center justify-between gap-2 mb-2">
                  <span className="text-[10px] font-extrabold uppercase tracking-wider bg-blue-50 text-blue-700 border border-blue-200 px-2.5 py-0.5 rounded-full">
                    {scheme.category || scheme.domain}
                  </span>
                  <span className="text-[10px] font-semibold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">
                    {scheme.central_or_state || "Central"}
                  </span>
                </div>

                <h3 className="font-black text-base text-slate-900 mt-1 leading-snug group-hover:text-blue-600 transition-colors">
                  {scheme.name}
                </h3>
                <p className="text-[11px] text-slate-500 line-clamp-1 mt-0.5 font-medium">
                  {scheme.ministry}
                </p>

                <p className="text-xs text-slate-600 line-clamp-3 mt-3 leading-relaxed">
                  {scheme.description}
                </p>

                {/* Financial Benefit Callout */}
                <div className="bg-emerald-50/70 border border-emerald-200/80 rounded-2xl p-3.5 mt-4">
                  <span className="text-[10px] font-bold text-emerald-800 uppercase tracking-wider block">
                    Financial Benefit / Assistance
                  </span>
                  <p className="font-extrabold text-xs text-emerald-950 mt-0.5 line-clamp-2">
                    {scheme.max_subsidy_or_loan}
                  </p>
                </div>
              </div>

              <div className="pt-4 mt-5 border-t border-slate-100 flex items-center justify-between gap-2">
                <button
                  onClick={() => onViewScheme(scheme)}
                  className="text-xs font-bold text-slate-700 hover:text-blue-700 bg-slate-100 hover:bg-blue-50 px-3 py-2 rounded-xl transition-colors"
                >
                  View Eligibility Rules
                </button>

                <a
                  href={scheme.apply_link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center gap-1.5 text-xs font-bold text-white bg-blue-600 hover:bg-blue-700 px-3.5 py-2 rounded-xl transition-all shadow-xs"
                >
                  <span>Apply Portal</span>
                  <ExternalLink className="w-3.5 h-3.5" />
                </a>
              </div>
            </div>
          ))}
        </div>
      )}

    </div>
  );
}
