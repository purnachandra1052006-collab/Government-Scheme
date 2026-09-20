import React, { useState, useEffect } from "react";
import { 
  Search, 
  Filter, 
  Building2, 
  Coins, 
  ExternalLink, 
  FileText, 
  BookOpen, 
  Layers 
} from "lucide-react";
import { getAllSchemes } from "../services/api";

export default function SchemeCatalog({ onViewScheme, onViewDocuments }) {
  const [schemes, setSchemes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("All");

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

  const categories = ["All", ...Array.from(new Set(schemes.map((s) => s.category)))];

  const filteredSchemes = schemes.filter((s) => {
    const matchesSearch =
      s.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      s.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
      s.ministry.toLowerCase().includes(searchTerm.toLowerCase());

    const matchesCategory = selectedCategory === "All" || s.category === selectedCategory;

    return matchesSearch && matchesCategory;
  });

  return (
    <div className="space-y-6">
      
      {/* Header & Search */}
      <div className="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
        <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
          <div>
            <h2 className="text-xl font-extrabold text-slate-900 flex items-center gap-2">
              <BookOpen className="w-5 h-5 text-blue-600" />
              <span>National Schemes & Subsidies Directory</span>
            </h2>
            <p className="text-xs text-slate-500 mt-1">
              Curated official Indian government schemes covering MSMEs, Students, Farmers, and Artisans.
            </p>
          </div>

          <div className="flex flex-col sm:flex-row items-center gap-3">
            {/* Search Input */}
            <div className="relative w-full sm:w-64">
              <Search className="w-4 h-4 text-slate-400 absolute left-3 top-3" />
              <input
                type="text"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                placeholder="Search schemes, ministry, keywords..."
                className="w-full pl-9 pr-4 py-2 text-xs bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
              />
            </div>

            {/* Category Filter */}
            <select
              value={selectedCategory}
              onChange={(e) => setSelectedCategory(e.target.value)}
              className="w-full sm:w-auto px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 font-medium text-slate-700"
            >
              {categories.map((cat, idx) => (
                <option key={idx} value={cat}>
                  {cat === "All" ? "All Categories" : cat}
                </option>
              ))}
            </select>
          </div>
        </div>
      </div>

      {/* Grid of Scheme Cards */}
      {loading ? (
        <div className="text-center py-16">
          <div className="w-8 h-8 rounded-full border-2 border-blue-600 border-t-transparent animate-spin mx-auto mb-3" />
          <p className="text-xs text-slate-500">Loading scheme directory...</p>
        </div>
      ) : filteredSchemes.length === 0 ? (
        <div className="bg-white rounded-2xl border border-slate-200 p-12 text-center">
          <Search className="w-10 h-10 text-slate-300 mx-auto mb-3" />
          <h3 className="font-bold text-sm text-slate-800">No matching schemes found</h3>
          <p className="text-xs text-slate-500 mt-1">Try adjusting your search query or category filter.</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {filteredSchemes.map((scheme) => (
            <div
              key={scheme.id}
              className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm hover:shadow-md transition-all flex flex-col justify-between"
            >
              <div>
                <span className="text-[10px] font-extrabold uppercase tracking-wider bg-blue-50 text-blue-700 border border-blue-200 px-2 py-0.5 rounded-md">
                  {scheme.category}
                </span>

                <h3 className="font-extrabold text-sm sm:text-base text-slate-900 mt-2 line-clamp-2">
                  {scheme.name}
                </h3>
                <p className="text-[11px] text-slate-500 line-clamp-1 mt-0.5">
                  {scheme.ministry}
                </p>

                <p className="text-xs text-slate-600 line-clamp-3 mt-3 leading-relaxed">
                  {scheme.description}
                </p>

                <div className="bg-emerald-50/60 border border-emerald-100 rounded-xl p-3 mt-4">
                  <span className="text-[10px] font-bold text-slate-500 uppercase tracking-wider block">
                    Financial Benefit
                  </span>
                  <p className="font-extrabold text-xs text-emerald-900 mt-0.5 line-clamp-2">
                    {scheme.max_subsidy_or_loan}
                  </p>
                </div>
              </div>

              <div className="pt-4 mt-4 border-t border-slate-100 flex items-center justify-between gap-2">
                <button
                  onClick={() => onViewScheme(scheme)}
                  className="text-xs font-bold text-slate-700 hover:text-blue-700 bg-slate-100 hover:bg-blue-50 px-3 py-1.5 rounded-lg transition-colors"
                >
                  View Details
                </button>

                <a
                  href={scheme.apply_link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center gap-1.5 text-xs font-bold text-white bg-blue-600 hover:bg-blue-700 px-3 py-1.5 rounded-lg transition-all shadow-xs"
                >
                  <span>Portal</span>
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
