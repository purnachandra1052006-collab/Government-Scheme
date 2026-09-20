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

  const [govtFilter, setGovtFilter] = useState("All"); // "All", "Central", "State"
  const [beneficiaryFilter, setBeneficiaryFilter] = useState("All"); // "All", "Family", "Individual"
  const [selectedState, setSelectedState] = useState("All");

  // Get distinct domains from schemes db
  const uniqueDomains = ["All", ...Array.from(new Set(schemes.map((s) => s.category || s.domain).filter(Boolean)))];

  // Get distinct states from state schemes
  const stateList = ["All", ...Array.from(new Set(schemes.map((s) => s.state_name).filter(Boolean)))].sort();

  const filteredSchemes = schemes.filter((s) => {
    const sDomain = s.category || s.domain || "";
    const matchesDomain = selectedDomain === "All" || sDomain === selectedDomain;

    const isStateScheme = s.central_or_state === "State Government" || Boolean(s.state_name);
    const matchesGovt =
      govtFilter === "All" ||
      (govtFilter === "Central" && !isStateScheme) ||
      (govtFilter === "State" && isStateScheme);

    const isFamilyScheme = s.beneficiary_level === "Family / Household";
    const matchesBeneficiary =
      beneficiaryFilter === "All" ||
      (beneficiaryFilter === "Family" && isFamilyScheme) ||
      (beneficiaryFilter === "Individual" && !isFamilyScheme);

    const matchesState =
      selectedState === "All" ||
      !isStateScheme ||
      s.state_name === selectedState ||
      (s.states_applicable && s.states_applicable.includes(selectedState));

    const matchesSearch =
      s.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      s.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
      s.ministry.toLowerCase().includes(searchTerm.toLowerCase()) ||
      (s.state_name && s.state_name.toLowerCase().includes(searchTerm.toLowerCase())) ||
      (s.target_beneficiaries && s.target_beneficiaries.some((b) => b.toLowerCase().includes(searchTerm.toLowerCase())));

    return matchesDomain && matchesGovt && matchesBeneficiary && matchesState && matchesSearch;
  });

  return (
    <div className="space-y-6">
      
      {/* Header & Search */}
      <div className="bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 shadow-sm">
        <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
          <div>
            <div className="inline-flex items-center gap-2 text-xs font-extrabold uppercase tracking-wider bg-blue-50 text-blue-700 px-3 py-1 rounded-full border border-blue-200 mb-2">
              <BookOpen className="w-3.5 h-3.5" />
              <span>National Scheme Directory (24 Domains & State/Family Schemes)</span>
            </div>
            <h2 className="text-xl sm:text-2xl font-black text-slate-900">
              Explore Government Schemes & Welfare Programs
            </h2>
            <p className="text-xs sm:text-sm text-slate-500 mt-1 max-w-2xl">
              Browse official Indian central and state welfare initiatives across Individual and Family entitlements (Health, Housing, Land Pattas, MSME, Agriculture, Education).
            </p>
          </div>

          <div className="relative w-full lg:w-80">
            <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-3.5" />
            <input
              type="text"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              placeholder="Search by name, ministry, or state..."
              className="w-full pl-10 pr-4 py-2.5 text-xs sm:text-sm bg-slate-50 border border-slate-200 rounded-2xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
            />
          </div>
        </div>

        {/* Filters Row: Level + Beneficiary Unit + State Filter */}
        <div className="mt-6 pt-5 border-t border-slate-100 flex flex-wrap items-center justify-between gap-4">
          <div className="flex flex-wrap items-center gap-3">
            {/* Govt Level */}
            <div className="flex items-center gap-1.5">
              <span className="text-[11px] font-bold text-slate-500 uppercase tracking-wider">
                Level:
              </span>
              <div className="inline-flex bg-slate-100 p-1 rounded-xl">
                <button
                  onClick={() => { setGovtFilter("All"); }}
                  className={`px-3 py-1 rounded-lg text-xs font-bold transition-all ${
                    govtFilter === "All"
                      ? "bg-white text-slate-900 shadow-xs"
                      : "text-slate-600 hover:text-slate-900"
                  }`}
                >
                  All ({schemes.length})
                </button>
                <button
                  onClick={() => { setGovtFilter("Central"); }}
                  className={`px-3 py-1 rounded-lg text-xs font-bold transition-all ${
                    govtFilter === "Central"
                      ? "bg-blue-600 text-white shadow-xs"
                      : "text-slate-600 hover:text-slate-900"
                  }`}
                >
                  🇮🇳 Central ({schemes.filter(s => s.central_or_state !== "State Government" && !s.state_name).length})
                </button>
                <button
                  onClick={() => { setGovtFilter("State"); }}
                  className={`px-3 py-1 rounded-lg text-xs font-bold transition-all ${
                    govtFilter === "State"
                      ? "bg-purple-600 text-white shadow-xs"
                      : "text-slate-600 hover:text-slate-900"
                  }`}
                >
                  🏛️ State ({schemes.filter(s => s.central_or_state === "State Government" || s.state_name).length})
                </button>
              </div>
            </div>

            {/* Beneficiary Unit */}
            <div className="flex items-center gap-1.5">
              <span className="text-[11px] font-bold text-slate-500 uppercase tracking-wider">
                Target Unit:
              </span>
              <div className="inline-flex bg-slate-100 p-1 rounded-xl">
                <button
                  onClick={() => { setBeneficiaryFilter("All"); }}
                  className={`px-2.5 py-1 rounded-lg text-xs font-bold transition-all ${
                    beneficiaryFilter === "All"
                      ? "bg-white text-slate-900 shadow-xs"
                      : "text-slate-600 hover:text-slate-900"
                  }`}
                >
                  All
                </button>
                <button
                  onClick={() => { setBeneficiaryFilter("Family"); }}
                  className={`px-2.5 py-1 rounded-lg text-xs font-bold transition-all ${
                    beneficiaryFilter === "Family"
                      ? "bg-amber-600 text-white shadow-xs"
                      : "text-slate-600 hover:text-slate-900"
                  }`}
                >
                  👨‍👩‍👧 Family
                </button>
                <button
                  onClick={() => { setBeneficiaryFilter("Individual"); }}
                  className={`px-2.5 py-1 rounded-lg text-xs font-bold transition-all ${
                    beneficiaryFilter === "Individual"
                      ? "bg-emerald-600 text-white shadow-xs"
                      : "text-slate-600 hover:text-slate-900"
                  }`}
                >
                  👤 Individual
                </button>
              </div>
            </div>
          </div>

          {govtFilter !== "Central" && (
            <div className="flex items-center gap-2">
              <span className="text-[11px] font-bold text-slate-500 uppercase tracking-wider">
                State:
              </span>
              <select
                value={selectedState}
                onChange={(e) => setSelectedState(e.target.value)}
                className="text-xs font-bold bg-slate-50 border border-slate-200 rounded-xl px-3 py-1.5 focus:ring-2 focus:ring-purple-500 focus:bg-white"
              >
                {stateList.map((st) => (
                  <option key={st} value={st}>
                    {st === "All" ? "All States" : st}
                  </option>
                ))}
              </select>
            </div>
          )}
        </div>

        {/* 24-Domain Filter Chips */}
        <div className="mt-4 pt-4 border-t border-slate-100">
          <span className="text-[11px] font-bold text-slate-500 uppercase tracking-wider block mb-2.5">
            Filter by Domain:
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
          <p className="text-xs text-slate-500 mt-1">Try selecting a different filter, state, or clearing your search term.</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredSchemes.map((scheme) => (
            <div
              key={scheme.id}
              className="bg-white rounded-3xl border border-slate-200 p-6 shadow-sm hover:shadow-md transition-all flex flex-col justify-between group"
            >
              <div>
                <div className="flex items-center justify-between gap-2 mb-2 flex-wrap">
                  <span className="text-[10px] font-extrabold uppercase tracking-wider bg-blue-50 text-blue-700 border border-blue-200 px-2.5 py-0.5 rounded-full">
                    {scheme.category || scheme.domain}
                  </span>
                  {scheme.central_or_state === "State Government" || scheme.state_name ? (
                    <span className="text-[10px] font-bold text-purple-700 bg-purple-50 border border-purple-200 px-2 py-0.5 rounded-md">
                      🏛️ {scheme.state_name || scheme.states_applicable?.[0] || "State"} Govt
                    </span>
                  ) : (
                    <span className="text-[10px] font-bold text-slate-600 bg-slate-100 border border-slate-200 px-2 py-0.5 rounded-md">
                      🇮🇳 Central Govt
                    </span>
                  )}
                  {scheme.beneficiary_level === "Family / Household" ? (
                    <span className="text-[10px] font-bold text-amber-800 bg-amber-50 border border-amber-200 px-2 py-0.5 rounded-md">
                      👨‍👩‍👧 Family
                    </span>
                  ) : (
                    <span className="text-[10px] font-bold text-emerald-800 bg-emerald-50 border border-emerald-200 px-2 py-0.5 rounded-md">
                      👤 Individual
                    </span>
                  )}
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
