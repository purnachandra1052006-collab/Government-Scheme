import React from "react";
import { 
  User, 
  IndianRupee, 
  MapPin, 
  GraduationCap, 
  Briefcase, 
  Layers, 
  Check, 
  Sparkles 
} from "lucide-react";

export default function ProfileSummaryDrawer({ profile, onReset, isEvaluating }) {
  const hasAnyData = Object.values(profile).some((val) => val !== null && val !== undefined && val !== "");

  return (
    <div className="bg-white rounded-2xl border border-slate-200 shadow-sm p-5">
      <div className="flex items-center justify-between border-b border-slate-100 pb-3 mb-4">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center font-bold text-sm">
            <User className="w-4 h-4" />
          </div>
          <div>
            <h3 className="font-bold text-sm text-slate-900">Your Citizen Profile</h3>
            <p className="text-[11px] text-slate-500">Live eligibility criteria tracker</p>
          </div>
        </div>

        {hasAnyData && (
          <button
            onClick={onReset}
            className="text-[11px] font-semibold text-slate-500 hover:text-red-600 transition-colors px-2 py-1 rounded hover:bg-red-50"
          >
            Reset
          </button>
        )}
      </div>

      {!hasAnyData ? (
        <div className="text-center py-6 px-4 bg-slate-50 rounded-xl border border-dashed border-slate-200">
          <Sparkles className="w-6 h-6 text-slate-400 mx-auto mb-2 opacity-60" />
          <p className="text-xs text-slate-600 font-medium">No profile data collected yet.</p>
          <p className="text-[11px] text-slate-400 mt-1">Answer the intake questions or pick a sample preset to start.</p>
        </div>
      ) : (
        <div className="space-y-3">
          {/* Occupation */}
          <div className="flex items-start justify-between text-xs">
            <span className="text-slate-500 flex items-center gap-1.5 font-medium">
              <Briefcase className="w-3.5 h-3.5 text-blue-500" />
              Occupation:
            </span>
            <span className="font-bold text-slate-800 bg-slate-100 px-2 py-0.5 rounded">
              {profile.occupation || "Not set"}
            </span>
          </div>

          {/* Age & Gender */}
          <div className="flex items-start justify-between text-xs">
            <span className="text-slate-500 flex items-center gap-1.5 font-medium">
              <User className="w-3.5 h-3.5 text-indigo-500" />
              Demographics:
            </span>
            <span className="font-semibold text-slate-800">
              {profile.age ? `${profile.age} yrs` : "Age -"} • {profile.gender || "Gender -"}
            </span>
          </div>

          {/* Social Category */}
          <div className="flex items-start justify-between text-xs">
            <span className="text-slate-500 flex items-center gap-1.5 font-medium">
              <Layers className="w-3.5 h-3.5 text-purple-500" />
              Category:
            </span>
            <span className="font-semibold text-purple-700 bg-purple-50 border border-purple-200/60 px-2 py-0.5 rounded">
              {profile.caste || "Not set"}
            </span>
          </div>

          {/* Annual Household Income */}
          <div className="flex items-start justify-between text-xs">
            <span className="text-slate-500 flex items-center gap-1.5 font-medium">
              <IndianRupee className="w-3.5 h-3.5 text-emerald-500" />
              Annual Income:
            </span>
            <span className="font-bold text-emerald-700 bg-emerald-50 border border-emerald-200/60 px-2 py-0.5 rounded">
              {profile.annual_income !== null && profile.annual_income !== undefined
                ? `₹${Number(profile.annual_income).toLocaleString("en-IN")}`
                : "Not set"}
            </span>
          </div>

          {/* State / Location */}
          <div className="flex items-start justify-between text-xs">
            <span className="text-slate-500 flex items-center gap-1.5 font-medium">
              <MapPin className="w-3.5 h-3.5 text-rose-500" />
              State:
            </span>
            <span className="font-semibold text-slate-800">
              {profile.state || "All India"}
            </span>
          </div>

          {/* Education Level */}
          {profile.education_level && (
            <div className="flex items-start justify-between text-xs">
              <span className="text-slate-500 flex items-center gap-1.5 font-medium">
                <GraduationCap className="w-3.5 h-3.5 text-cyan-500" />
                Education:
              </span>
              <span className="font-semibold text-slate-800 bg-slate-100 px-2 py-0.5 rounded">
                {profile.education_level}
              </span>
            </div>
          )}

          {/* Business & Project Type */}
          {profile.is_new_project !== undefined && profile.occupation === "Entrepreneur" && (
            <div className="flex items-start justify-between text-xs">
              <span className="text-slate-500 flex items-center gap-1.5 font-medium">
                <Sparkles className="w-3.5 h-3.5 text-amber-500" />
                Project Stage:
              </span>
              <span className={`font-semibold px-2 py-0.5 rounded ${profile.is_new_project ? 'bg-emerald-50 text-emerald-700 border border-emerald-200' : 'bg-slate-100 text-slate-700'}`}>
                {profile.is_new_project ? "🌱 New Greenfield" : "Existing Expansion"}
              </span>
            </div>
          )}

          {/* Target Funding */}
          {profile.funding_required && (
            <div className="flex items-start justify-between text-xs">
              <span className="text-slate-500 flex items-center gap-1.5 font-medium">
                <IndianRupee className="w-3.5 h-3.5 text-blue-500" />
                Target Loan:
              </span>
              <span className="font-bold text-blue-700 bg-blue-50 border border-blue-200 px-2 py-0.5 rounded">
                ₹{Number(profile.funding_required).toLocaleString("en-IN")}
              </span>
            </div>
          )}
        </div>
      )}

      {isEvaluating && (
        <div className="mt-4 pt-3 border-t border-slate-100 flex items-center justify-center gap-2 text-xs font-semibold text-blue-600 animate-pulse">
          <div className="w-2 h-2 rounded-full bg-blue-600 animate-ping" />
          Running deterministic rule checks...
        </div>
      )}
    </div>
  );
}
