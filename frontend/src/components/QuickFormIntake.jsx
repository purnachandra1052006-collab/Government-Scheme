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
  Layers,
  Heart,
  Sun,
  ShieldCheck,
  Building
} from "lucide-react";

export default function QuickFormIntake({ profile, setProfile, onEvaluate, isEvaluating }) {
  const [formData, setFormData] = useState({
    occupation: profile.occupation || "Entrepreneur",
    age: profile.age || 28,
    gender: profile.gender || "Female",
    caste: profile.caste || "General",
    annual_income: profile.annual_income || 350000,
    state: profile.state || "Maharashtra",
    area_type: profile.area_type || "Rural",
    education_level: profile.education_level || "Graduate",
    specific_goal: profile.specific_goal || "Business Setup & Loan",
    beneficiary_type: profile.beneficiary_type || "All",
    is_new_project: profile.is_new_project !== undefined ? profile.is_new_project : true,
    funding_required: profile.funding_required || 2000000,
    owns_pucca_house: profile.owns_pucca_house || false,
    has_bpl_ration_card: profile.has_bpl_ration_card || false,
    is_tax_payer: profile.is_tax_payer || false,
    owns_agricultural_land: profile.owns_agricultural_land || false,
    land_holding_acres: profile.land_holding_acres || 0,
    is_landless: profile.is_landless || false,
    has_homestead_plot: profile.has_homestead_plot || false,
    owns_motorized_vehicle: profile.owns_motorized_vehicle || false,
    is_differently_abled: profile.is_differently_abled || false,
    disability_percentage: profile.disability_percentage || 40,
    is_pregnant_or_lactating: profile.is_pregnant_or_lactating || false,
    has_girl_child: profile.has_girl_child || false,
    girl_child_age: profile.girl_child_age || 6,
    has_solar_rooftop_space: profile.has_solar_rooftop_space || false,
    is_unorganised_worker: profile.is_unorganised_worker || false,
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
    <form onSubmit={handleSubmit} className="bg-white rounded-3xl border border-slate-200 shadow-sm p-6 sm:p-8 space-y-8">
      
      {/* Header */}
      <div className="border-b border-slate-100 pb-5">
        <div className="inline-flex items-center gap-2 text-xs font-extrabold uppercase tracking-wider bg-blue-50 text-blue-700 px-3 py-1 rounded-full border border-blue-200 mb-2">
          <Sparkles className="w-3.5 h-3.5 text-blue-600" />
          <span>Multi-Domain Assessment Wizard</span>
        </div>
        <h3 className="font-black text-xl text-slate-900">
          Citizen Eligibility Assessment
        </h3>
        <p className="text-xs text-slate-500 mt-1">
          Provide your demographic, economic, and specialized attributes to evaluate your profile across all 24 scheme domains.
        </p>
      </div>

      {/* SECTION 1: Core Demographics */}
      <div>
        <h4 className="text-xs font-extrabold text-slate-400 uppercase tracking-wider mb-4 flex items-center gap-1.5">
          <User className="w-3.5 h-3.5 text-blue-500" />
          <span>1. Demographics & Geography</span>
        </h4>

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
              className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white font-medium"
            >
              <option value="Entrepreneur">💼 Entrepreneur / MSME Owner</option>
              <option value="Student">🎓 Student / Scholar</option>
              <option value="Farmer">🌾 Farmer / Agri Producer</option>
              <option value="Street Vendor">🛒 Street Vendor / Hawker</option>
              <option value="Artisan">⚒️ Traditional Artisan / Weaver</option>
              <option value="Construction Worker">👷 Construction / Daily Wage Worker</option>
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
              min="10"
              max="100"
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
              <option value="Female">Female (Special Stand-Up, PMMVY & MSME Subsidies)</option>
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
              <option value="SC">SC (Scheduled Caste - 35% Subsidies)</option>
              <option value="ST">ST (Scheduled Tribe - 35% Subsidies)</option>
              <option value="EWS">EWS (Economically Weaker Section)</option>
            </select>
          </div>

          {/* Area Type */}
          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1.5 flex items-center gap-1.5">
              <MapPin className="w-3.5 h-3.5 text-rose-500" />
              Area Type (Rural / Urban):
            </label>
            <select
              value={formData.area_type}
              onChange={(e) => handleChange("area_type", e.target.value)}
              className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
            >
              <option value="Rural">🌾 Rural / Village (35% PMEGP Subsidy)</option>
              <option value="Urban">🏙️ Urban / City</option>
              <option value="Semi-Urban">Semi-Urban</option>
            </select>
          </div>

          {/* State */}
          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1.5 flex items-center gap-1.5">
              <MapPin className="w-3.5 h-3.5 text-rose-500" />
              State of Residence:
            </label>
            <select
              value={formData.state}
              onChange={(e) => handleChange("state", e.target.value)}
              className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
            >
              <option value="All India">All India (National)</option>
              <option value="Andhra Pradesh">Andhra Pradesh</option>
              <option value="Assam">Assam</option>
              <option value="Bihar">Bihar</option>
              <option value="Delhi">Delhi</option>
              <option value="Gujarat">Gujarat</option>
              <option value="Haryana">Haryana</option>
              <option value="Karnataka">Karnataka</option>
              <option value="Kerala">Kerala</option>
              <option value="Madhya Pradesh">Madhya Pradesh</option>
              <option value="Maharashtra">Maharashtra</option>
              <option value="Odisha">Odisha</option>
              <option value="Punjab">Punjab</option>
              <option value="Rajasthan">Rajasthan</option>
              <option value="Tamil Nadu">Tamil Nadu</option>
              <option value="Telangana">Telangana</option>
              <option value="Uttar Pradesh">Uttar Pradesh</option>
              <option value="West Bengal">West Bengal</option>
            </select>
          </div>
        </div>
      </div>

      {/* SECTION 2: Economic & Household Assets / Exclusions */}
      <div className="border-t border-slate-100 pt-6">
        <h4 className="text-xs font-extrabold text-slate-400 uppercase tracking-wider mb-4 flex items-center gap-1.5">
          <IndianRupee className="w-3.5 h-3.5 text-emerald-500" />
          <span>2. Household Assets, Land Ownership & Statutory Exclusions</span>
        </h4>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
          {/* Target Beneficiary Unit */}
          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1.5 flex items-center gap-1.5">
              <Building className="w-3.5 h-3.5 text-indigo-500" />
              Target Beneficiary Unit:
            </label>
            <select
              value={formData.beneficiary_type}
              onChange={(e) => handleChange("beneficiary_type", e.target.value)}
              className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
            >
              <option value="All">All Schemes (Individual & Family)</option>
              <option value="Family / Household">👨‍👩‍👧 Family / Household Schemes (Housing, Land, Health, Ration)</option>
              <option value="Individual">👤 Individual Citizen Schemes (Scholarships, Loans, Pensions)</option>
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

          {/* Income Tax Returns (ITR) */}
          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1.5">
              Income Tax Returns (ITR / Taxpayer):
            </label>
            <select
              value={formData.is_tax_payer ? "true" : "false"}
              onChange={(e) => handleChange("is_tax_payer", e.target.value === "true")}
              className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
            >
              <option value="false">Non-Taxpayer (ITR Exempt - Eligible for Welfare)</option>
              <option value="true">Yes, Family member pays Income Tax / Files ITR</option>
            </select>
          </div>

          {/* BPL / Ration Card */}
          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1.5">
              BPL / Antyodaya Ration Card:
            </label>
            <select
              value={formData.has_bpl_ration_card ? "true" : "false"}
              onChange={(e) => handleChange("has_bpl_ration_card", e.target.value === "true")}
              className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
            >
              <option value="false">No / General APL Card</option>
              <option value="true">Yes, BPL / Antyodaya / NFSA White/Pink Card</option>
            </select>
          </div>

          {/* Pucca House Ownership */}
          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1.5">
              Owns Permanent Pucca House:
            </label>
            <select
              value={formData.owns_pucca_house ? "true" : "false"}
              onChange={(e) => handleChange("owns_pucca_house", e.target.value === "true")}
              className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
            >
              <option value="false">No (Houseless / Kutcha house - Eligible for PMAY ₹1.3L-₹2.67L)</option>
              <option value="true">Yes, Family owns a permanent pucca house</option>
            </select>
          </div>

          {/* Motorized 4-Wheeler Vehicle */}
          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1.5">
              Owns Motorized 4-Wheeler Vehicle:
            </label>
            <select
              value={formData.owns_motorized_vehicle ? "true" : "false"}
              onChange={(e) => handleChange("owns_motorized_vehicle", e.target.value === "true")}
              className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
            >
              <option value="false">No 4-Wheeler (Satisfies asset caps)</option>
              <option value="true">Yes, Family owns a car / tractor / 4-wheeler</option>
            </select>
          </div>

          {/* Land Ownership & Landless Status */}
          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1.5">
              Farmland / Agricultural Land:
            </label>
            <select
              value={formData.is_landless ? "landless" : (formData.owns_agricultural_land ? "owns_land" : "no_land")}
              onChange={(e) => {
                const val = e.target.value;
                if (val === "landless") {
                  handleChange("is_landless", true);
                  handleChange("owns_agricultural_land", false);
                } else if (val === "owns_land") {
                  handleChange("is_landless", false);
                  handleChange("owns_agricultural_land", true);
                } else {
                  handleChange("is_landless", false);
                  handleChange("owns_agricultural_land", false);
                }
              }}
              className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
            >
              <option value="no_land">Non-Agricultural / Urban</option>
              <option value="owns_land">🌾 Owns Cultivable Farmland (PM-KISAN / Rythu Bandhu)</option>
              <option value="landless">🚫 Completely Landless Family (Vasundhara / Land Patta Allotment)</option>
            </select>
          </div>

          {/* House Site Plot for Construction */}
          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1.5">
              Available House Site Plot / Homestead:
            </label>
            <select
              value={formData.has_homestead_plot ? "true" : "false"}
              onChange={(e) => handleChange("has_homestead_plot", e.target.value === "true")}
              className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
            >
              <option value="true">Yes, Has land parcel / homestead site for building</option>
              <option value="false">No (Siteless family needing land patta allotment)</option>
            </select>
          </div>
        </div>
      </div>

      {/* SECTION 3: Specialized Criteria */}
      <div className="border-t border-slate-100 pt-6">
        <h4 className="text-xs font-extrabold text-slate-400 uppercase tracking-wider mb-4 flex items-center gap-1.5">
          <Heart className="w-3.5 h-3.5 text-rose-500" />
          <span>3. Specialized Welfare & Green Energy Attributes</span>
        </h4>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
          {/* Differently Abled */}
          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1.5">
              Benchmark Disability (Divyangjan):
            </label>
            <select
              value={formData.is_differently_abled ? "true" : "false"}
              onChange={(e) => handleChange("is_differently_abled", e.target.value === "true")}
              className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
            >
              <option value="false">No</option>
              <option value="true">Yes (ADIP Free Assistive Devices & Scholarships)</option>
            </select>
          </div>

          {/* Maternity Status (If Female) */}
          {formData.gender === "Female" && (
            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1.5">
                Pregnant / Lactating Mother:
              </label>
              <select
                value={formData.is_pregnant_or_lactating ? "true" : "false"}
                onChange={(e) => handleChange("is_pregnant_or_lactating", e.target.value === "true")}
                className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
              >
                <option value="false">No</option>
                <option value="true">Yes (PMMVY ₹5,000 - ₹6,000 Cash Grant)</option>
              </select>
            </div>
          )}

          {/* Girl Child */}
          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1.5">
              Parent of Girl Child (&le; 10 yrs):
            </label>
            <select
              value={formData.has_girl_child ? "true" : "false"}
              onChange={(e) => handleChange("has_girl_child", e.target.value === "true")}
              className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
            >
              <option value="false">No</option>
              <option value="true">Yes (Sukanya Samriddhi 8.2% Sovereign Savings)</option>
            </select>
          </div>

          {/* Solar Rooftop Space */}
          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1.5 flex items-center gap-1.5">
              <Sun className="w-3.5 h-3.5 text-amber-500" />
              Available Rooftop for Solar Panels:
            </label>
            <select
              value={formData.has_solar_rooftop_space ? "true" : "false"}
              onChange={(e) => handleChange("has_solar_rooftop_space", e.target.value === "true")}
              className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
            >
              <option value="false">No</option>
              <option value="true">Yes (PM Surya Ghar ₹78k Subsidy + Free Power)</option>
            </select>
          </div>

          {/* Unorganised / e-Shram Worker */}
          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1.5">
              e-Shram / Unorganised Worker:
            </label>
            <select
              value={formData.is_unorganised_worker ? "true" : "false"}
              onChange={(e) => handleChange("is_unorganised_worker", e.target.value === "true")}
              className="w-full text-xs sm:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white"
            >
              <option value="false">No</option>
              <option value="true">Yes (PM-SYM ₹3k/mo Pension & Social Security)</option>
            </select>
          </div>
        </div>
      </div>

      {/* Submit Button */}
      <div className="pt-4 border-t border-slate-100 flex items-center justify-end">
        <button
          type="submit"
          disabled={isEvaluating}
          className="px-8 py-3.5 bg-blue-600 hover:bg-blue-700 disabled:opacity-50 text-white rounded-2xl font-black text-sm flex items-center gap-2 shadow-lg shadow-blue-500/20 transition-all hover:scale-[1.01]"
        >
          <span>{isEvaluating ? "Evaluating 24 Domains..." : "Run Scheme Eligibility Match"}</span>
          <ArrowRight className="w-4 h-4" />
        </button>
      </div>

    </form>
  );
}
