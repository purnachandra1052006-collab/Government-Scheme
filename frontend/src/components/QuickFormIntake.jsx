import React, { useState } from "react";
import { 
  Sparkles, 
  ArrowRight, 
  CheckCircle2, 
  IndianRupee, 
  User, 
  Briefcase, 
  GraduationCap, 
  MapPin, 
  Layers 
} from "lucide-react";

export default function QuickFormIntake({ profile, setProfile, onEvaluate, isEvaluating }) {
  const [formData, setFormData] = useState({
    occupation: profile.occupation || "Entrepreneur",
    age: profile.age || 28,
    gender: profile.gender || "Female",
    caste: profile.caste || "General",
    annual_income: profile.annual_income || 350000,
    state: profile.state || "Maharashtra",
    education_level: profile.education_level || "Graduate",
    specific_goal: profile.specific_goal || "Business Setup & Loan",
    is_new_project: profile.is_new_project !== undefined ? profile.is_new_project : true,
    funding_required: profile.funding_required || 2000000,
    owns_pucca_house: profile.owns_pucca_house || false,
    is_tax_payer: profile.is_tax_payer || false,
  });

  const handleChange = (field, value) => {
    const updated = { ...formData, [field]: value };
    setFormData(updated);
    setProfile(updated);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onEvaluate(formData);
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 sm:p-8 space-y-6">
      
      {/* Header */}
      <div className="border-b border-slate-100 pb-4">
        <h3 className="font-extrabold text-base sm:text-lg text-slate-900 flex items-center gap-2">
          <Sparkles className="w-5 h-5 text-blue-600" />
          <span>Quick Scheme Eligibility Assessment</span>
        </h3>
        <p className="text-xs text-slate-500 mt-1">
          Provide your demographic and financial details to run our rule engine across all government schemes.
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
        
        {/* Occupation */}
        <div>
          <label className="block text-xs font-bold text-slate-700 mb-1.5 flex items-center gap-1.5">
            <Briefcase className="w-3.5 h-3.5 text-blue-500" />
            Primary Occupation / Status:
          </label>
          <select
            value={formData.occupation}
            onChange={(e) => handleChange("occupation", e.target.value)}
            className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
          >
            <option value="Entrepreneur">💼 Entrepreneur / MSME Owner</option>
            <option value="Student">🎓 Student / Scholar</option>
            <option value="Farmer">🌾 Farmer / Agri Producer</option>
            <option value="Street Vendor">🛒 Street Vendor / Hawker</option>
            <option value="Artisan">⚒️ Traditional Artisan / Craftsperson</option>
            <option value="Unemployed">🔍 Jobseeker / Unemployed</option>
            <option value="Salaried">🏢 Salaried Employee</option>
          </select>
        </div>

        {/* Age */}
        <div>
          <label className="block text-xs font-bold text-slate-700 mb-1.5 flex items-center gap-1.5">
            <User className="w-3.5 h-3.5 text-indigo-500" />
            Age (Years):
          </label>
          <input
            type="number"
            min="14"
            max="95"
            value={formData.age}
            onChange={(e) => handleChange("age", parseInt(e.target.value) || 18)}
            className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
          />
        </div>

        {/* Gender */}
        <div>
          <label className="block text-xs font-bold text-slate-700 mb-1.5 flex items-center gap-1.5">
            <User className="w-3.5 h-3.5 text-indigo-500" />
            Gender:
          </label>
          <select
            value={formData.gender}
            onChange={(e) => handleChange("gender", e.target.value)}
            className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
          >
            <option value="Female">Female (Special Stand-Up / MSME Subsidies)</option>
            <option value="Male">Male</option>
            <option value="Other">Other / Transgender</option>
          </select>
        </div>

        {/* Social Category */}
        <div>
          <label className="block text-xs font-bold text-slate-700 mb-1.5 flex items-center gap-1.5">
            <Layers className="w-3.5 h-3.5 text-purple-500" />
            Social Category (Caste):
          </label>
          <select
            value={formData.caste}
            onChange={(e) => handleChange("caste", e.target.value)}
            className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
          >
            <option value="General">General Category</option>
            <option value="OBC">OBC (Other Backward Class)</option>
            <option value="SC">SC (Scheduled Caste)</option>
            <option value="ST">ST (Scheduled Tribe)</option>
            <option value="EWS">EWS (Economically Weaker Section)</option>
          </select>
        </div>

        {/* Annual Income */}
        <div>
          <label className="block text-xs font-bold text-slate-700 mb-1.5 flex items-center gap-1.5">
            <IndianRupee className="w-3.5 h-3.5 text-emerald-500" />
            Annual Household Income (₹):
          </label>
          <input
            type="number"
            step="10000"
            value={formData.annual_income}
            onChange={(e) => handleChange("annual_income", parseFloat(e.target.value) || 0)}
            className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
          />
        </div>

        {/* State / UT */}
        <div>
          <label className="block text-xs font-bold text-slate-700 mb-1.5 flex items-center gap-1.5">
            <MapPin className="w-3.5 h-3.5 text-rose-500" />
            State / UT of Residence:
          </label>
          <select
            value={formData.state}
            onChange={(e) => handleChange("state", e.target.value)}
            className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
          >
            <option value="All India">All India (National)</option>
            <option value="Maharashtra">Maharashtra</option>
            <option value="Uttar Pradesh">Uttar Pradesh</option>
            <option value="Karnataka">Karnataka</option>
            <option value="Tamil Nadu">Tamil Nadu</option>
            <option value="Madhya Pradesh">Madhya Pradesh</option>
            <option value="Gujarat">Gujarat</option>
            <option value="Rajasthan">Rajasthan</option>
            <option value="Delhi">Delhi</option>
            <option value="West Bengal">West Bengal</option>
            <option value="Andhra Pradesh">Andhra Pradesh</option>
            <option value="Telangana">Telangana</option>
          </select>
        </div>

        {/* Highest Education */}
        <div>
          <label className="block text-xs font-bold text-slate-700 mb-1.5 flex items-center gap-1.5">
            <GraduationCap className="w-3.5 h-3.5 text-cyan-500" />
            Educational Qualification:
          </label>
          <select
            value={formData.education_level}
            onChange={(e) => handleChange("education_level", e.target.value)}
            className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
          >
            <option value="Below 8th">Below 8th Pass</option>
            <option value="8th Pass">8th Pass</option>
            <option value="10th Pass">10th Pass (Matriculation)</option>
            <option value="12th Pass">12th Pass (Higher Secondary)</option>
            <option value="Diploma">Diploma / ITI</option>
            <option value="Graduate">Graduate (B.A, B.Sc, B.Tech, etc.)</option>
            <option value="Post Graduate">Post Graduate / PhD</option>
          </select>
        </div>

        {/* Project Stage (For Entrepreneurs) */}
        {formData.occupation === "Entrepreneur" && (
          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1.5 flex items-center gap-1.5">
              <Sparkles className="w-3.5 h-3.5 text-amber-500" />
              Project Stage:
            </label>
            <select
              value={formData.is_new_project ? "true" : "false"}
              onChange={(e) => handleChange("is_new_project", e.target.value === "true")}
              className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
            >
              <option value="true">🌱 Brand New Project (Greenfield)</option>
              <option value="false">📈 Existing Enterprise Expansion</option>
            </select>
          </div>
        )}

        {/* Funding Required (For Entrepreneurs) */}
        {formData.occupation === "Entrepreneur" && (
          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1.5 flex items-center gap-1.5">
              <IndianRupee className="w-3.5 h-3.5 text-blue-500" />
              Target Loan / Funding (₹):
            </label>
            <input
              type="number"
              step="50000"
              value={formData.funding_required}
              onChange={(e) => handleChange("funding_required", parseFloat(e.target.value) || 0)}
              className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
            />
          </div>
        )}

      </div>

      {/* Submit Button */}
      <div className="pt-4 border-t border-slate-100 flex items-center justify-end">
        <button
          type="submit"
          disabled={isEvaluating}
          className="px-6 py-3 bg-blue-600 hover:bg-blue-700 disabled:opacity-50 text-white rounded-xl font-extrabold text-sm flex items-center gap-2 shadow-md shadow-blue-500/20 transition-all hover:scale-[1.01]"
        >
          <span>{isEvaluating ? "Evaluating Rules..." : "Run Scheme Eligibility Match"}</span>
          <ArrowRight className="w-4 h-4" />
        </button>
      </div>

    </form>
  );
}
