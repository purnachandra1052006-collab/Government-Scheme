import React, { useState } from "react";
import { X, Key, CheckCircle2, ShieldAlert, Sparkles, ExternalLink } from "lucide-react";
import { setGroqApiKey } from "../services/api";

export default function GroqKeyModal({ isOpen, onClose, onKeySaved, currentConfigured }) {
  const [keyInput, setKeyInput] = useState("");
  const [status, setStatus] = useState({ loading: false, success: false, error: null });

  if (!isOpen) return null;

  const handleSave = async (e) => {
    e.preventDefault();
    if (!keyInput.trim()) return;

    setStatus({ loading: true, success: false, error: null });
    try {
      const res = await setGroqApiKey(keyInput.trim());
      if (res.success) {
        setStatus({ loading: false, success: true, error: null });
        onKeySaved(true);
        setTimeout(() => {
          onClose();
        }, 1200);
      }
    } catch (err) {
      setStatus({ loading: false, success: false, error: err.message || "Failed to set Groq key" });
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-xs animate-fade-in">
      <div className="bg-white rounded-2xl max-w-md w-full shadow-2xl border border-slate-200 overflow-hidden">
        
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-100 flex items-center justify-between bg-slate-50">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-lg bg-emerald-100 text-emerald-800 flex items-center justify-center">
              <Key className="w-4 h-4 text-emerald-700" />
            </div>
            <div>
              <h3 className="font-bold text-sm text-slate-900">Groq LLM Configuration</h3>
              <p className="text-[11px] text-slate-500">Llama 3.3 70B Versatile Engine</p>
            </div>
          </div>
          <button onClick={onClose} className="p-1 rounded-lg text-slate-400 hover:text-slate-700">
            <X className="w-5 h-5" />
          </button>
        </div>

        <form onSubmit={handleSave} className="p-6 space-y-4">
          <p className="text-xs text-slate-600 leading-relaxed">
            Enter your <strong>Groq API Key</strong> to power instant transparent AI reasoning, adaptive conversational intake, and "Why You Qualify" breakdown summaries.
          </p>

          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1">
              Groq API Key:
            </label>
            <input
              type="password"
              value={keyInput}
              onChange={(e) => setKeyInput(e.target.value)}
              placeholder="gsk_..."
              className="w-full px-3.5 py-2.5 text-xs bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:bg-white font-mono"
            />
          </div>

          <div className="flex items-center justify-between text-[11px] text-slate-500">
            <span>Don't have a key?</span>
            <a
              href="https://console.groq.com/keys"
              target="_blank"
              rel="noopener noreferrer"
              className="font-bold text-blue-600 hover:underline flex items-center gap-1"
            >
              <span>Get Free Groq Key</span>
              <ExternalLink className="w-3 h-3" />
            </a>
          </div>

          {status.error && (
            <div className="p-3 bg-red-50 text-red-700 text-xs rounded-xl border border-red-200 flex items-center gap-2">
              <ShieldAlert className="w-4 h-4 shrink-0" />
              <span>{status.error}</span>
            </div>
          )}

          {status.success && (
            <div className="p-3 bg-emerald-50 text-emerald-800 text-xs rounded-xl border border-emerald-200 flex items-center gap-2">
              <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
              <span className="font-bold">Groq Key successfully activated!</span>
            </div>
          )}

          <div className="pt-2 flex items-center justify-end gap-2">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 text-xs font-bold text-slate-600 hover:text-slate-800"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={status.loading || !keyInput.trim()}
              className="px-4 py-2 bg-blue-600 hover:bg-blue-700 disabled:opacity-50 text-white rounded-xl text-xs font-bold shadow-xs transition-all"
            >
              {status.loading ? "Saving..." : "Save Key"}
            </button>
          </div>
        </form>

      </div>
    </div>
  );
}
