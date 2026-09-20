import React, { useState, useEffect, useRef } from "react";
import { 
  Send, 
  Sparkles, 
  Bot, 
  User, 
  ArrowRight, 
  RotateCcw, 
  CheckCircle2, 
  Layers, 
  IndianRupee 
} from "lucide-react";
import { startChatSession, sendChatMessage } from "../services/api";

export default function ChatIntake({ profile, setProfile, onCompleteEvaluation, isEvaluating }) {
  const [session, setSession] = useState(null);
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState("");
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    initChat();
  }, []);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const initChat = async () => {
    setLoading(true);
    try {
      const sess = await startChatSession();
      setSession(sess);
      setMessages(sess.history);
      setProfile(sess.profile);
    } catch (err) {
      console.error("Failed to start chat session:", err);
      // Fallback local initial state
      const fallbackMsg = {
        role: "assistant",
        content: "Welcome! What best describes your primary occupation or current status?",
        question_payload: {
          field: "occupation",
          input_type: "select",
          step: 1,
          total_steps: 7,
          options: [
            { label: "💼 Entrepreneur / Business Owner", value: "Entrepreneur" },
            { label: "🎓 Student / Scholar", value: "Student" },
            { label: "🌾 Farmer / Agri Worker", value: "Farmer" },
            { label: "🛒 Street Vendor / Hawkers", value: "Street Vendor" },
            { label: "⚒️ Traditional Artisan", value: "Artisan" },
            { label: "🔍 Jobseeker / Unemployed", value: "Unemployed" },
            { label: "🏢 Salaried / Working Professional", value: "Salaried" }
          ]
        }
      };
      setMessages([fallbackMsg]);
    } finally {
      setLoading(false);
    }
  };

  const handleOptionSelect = async (field, value, label) => {
    if (loading) return;
    setLoading(true);

    const updatedProfile = { ...profile, [field]: value };
    setProfile(updatedProfile);

    // Optimistically append user answer message
    const userMsg = {
      role: "user",
      content: label || String(value),
    };
    setMessages((prev) => [...prev, userMsg]);

    try {
      const sessionId = session?.session_id || "session_default";
      const updatedSession = await sendChatMessage(sessionId, updatedProfile, field, value);
      setSession(updatedSession);
      setMessages(updatedSession.history);
      setProfile(updatedSession.profile);

      if (updatedSession.is_complete) {
        onCompleteEvaluation(updatedSession.profile);
      }
    } catch (err) {
      console.error("Error sending chat intake message:", err);
    } finally {
      setLoading(false);
    }
  };

  const handleCustomSubmit = (e) => {
    e.preventDefault();
    if (!inputValue.trim() || loading) return;

    const currentQ = session?.next_question || messages[messages.length - 1]?.question_payload;
    const field = currentQ?.field || "specific_goal";
    
    let parsedVal = inputValue.trim();
    if (currentQ?.input_type === "number" || currentQ?.input_type === "currency") {
      parsedVal = parseFloat(parsedVal.replace(/[^0-9.]/g, "")) || parsedVal;
    }

    handleOptionSelect(field, parsedVal, inputValue.trim());
    setInputValue("");
  };

  const currentQ = session?.next_question || (messages.length > 0 ? messages[messages.length - 1].question_payload : null);

  return (
    <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden flex flex-col h-[650px]">
      
      {/* Header */}
      <div className="px-5 py-3.5 border-b border-slate-100 bg-slate-50/70 flex items-center justify-between">
        <div className="flex items-center gap-2.5">
          <div className="w-8 h-8 rounded-lg bg-blue-600 text-white flex items-center justify-center font-bold shadow-xs">
            <Bot className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h3 className="font-extrabold text-sm text-slate-900">
                Scheme Intake Assistant
              </h3>
              <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
            </div>
            <p className="text-[11px] text-slate-500">Adaptive 5–8 conversational assessment</p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          {session && (
            <span className="text-[11px] font-bold text-blue-700 bg-blue-50 border border-blue-200 px-2.5 py-0.5 rounded-full">
              Step {session.current_step} of {session.total_steps}
            </span>
          )}
          <button
            onClick={initChat}
            className="p-1.5 text-slate-400 hover:text-slate-700 hover:bg-slate-200/60 rounded-lg transition-colors"
            title="Restart conversation"
          >
            <RotateCcw className="w-4 h-4" />
          </button>
        </div>
      </div>

      {/* Messages Scroll Area */}
      <div className="flex-1 p-5 overflow-y-auto space-y-4 bg-gradient-to-b from-white to-slate-50/30">
        {messages.map((msg, idx) => {
          const isAssistant = msg.role === "assistant";
          const isLatestAssistant = isAssistant && idx === messages.length - 1;

          return (
            <div
              key={idx}
              className={`flex items-start gap-3 ${isAssistant ? "" : "flex-row-reverse"}`}
            >
              <div
                className={`w-8 h-8 rounded-xl flex items-center justify-center shrink-0 font-bold text-xs shadow-xs ${
                  isAssistant
                    ? "bg-gradient-to-tr from-blue-700 to-indigo-600 text-white"
                    : "bg-slate-800 text-white"
                }`}
              >
                {isAssistant ? <Bot className="w-4 h-4" /> : <User className="w-4 h-4" />}
              </div>

              <div className={`max-w-[85%] space-y-2.5 ${isAssistant ? "" : "text-right"}`}>
                <div
                  className={`p-4 rounded-2xl text-xs sm:text-sm leading-relaxed shadow-xs inline-block text-left ${
                    isAssistant
                      ? "bg-white border border-slate-200 text-slate-800 rounded-tl-none font-normal"
                      : "bg-blue-600 text-white rounded-tr-none font-medium"
                  }`}
                >
                  {msg.content}
                </div>

                {/* Render Quick Action Buttons if this is the active latest assistant question */}
                {isLatestAssistant && msg.question_payload && msg.question_payload.options && !session?.is_complete && (
                  <div className="pt-1 grid grid-cols-1 sm:grid-cols-2 gap-2 text-left animate-slide-up">
                    {msg.question_payload.options.map((opt, oIdx) => (
                      <button
                        key={oIdx}
                        disabled={loading}
                        onClick={() => handleOptionSelect(msg.question_payload.field, opt.value, opt.label)}
                        className="p-3 text-left rounded-xl border border-slate-200 bg-white hover:bg-blue-50/80 hover:border-blue-300 transition-all shadow-xs group flex flex-col justify-between"
                      >
                        <span className="font-bold text-xs text-slate-800 group-hover:text-blue-700">
                          {opt.label}
                        </span>
                        {opt.description && (
                          <span className="text-[11px] text-slate-500 mt-1 line-clamp-2">
                            {opt.description}
                          </span>
                        )}
                      </button>
                    ))}
                  </div>
                )}
              </div>
            </div>
          );
        })}

        {loading && (
          <div className="flex items-center gap-2 text-slate-400 text-xs py-2">
            <div className="w-2 h-2 rounded-full bg-blue-600 animate-bounce" />
            <div className="w-2 h-2 rounded-full bg-blue-600 animate-bounce [animation-delay:0.2s]" />
            <div className="w-2 h-2 rounded-full bg-blue-600 animate-bounce [animation-delay:0.4s]" />
            <span className="text-[11px] text-slate-500 font-medium">Assistant is thinking...</span>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Input Box Footer */}
      <div className="p-3.5 border-t border-slate-200 bg-white">
        <form onSubmit={handleCustomSubmit} className="flex items-center gap-2">
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            disabled={loading || session?.is_complete}
            placeholder={
              session?.is_complete
                ? "Intake complete! Reviewing matched schemes..."
                : currentQ?.helper_text || "Type your answer or select an option above..."
            }
            className="flex-1 px-4 py-2.5 text-xs sm:text-sm bg-slate-50 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:bg-white transition-all"
          />
          
          <button
            type="submit"
            disabled={!inputValue.trim() || loading || session?.is_complete}
            className="px-4 py-2.5 bg-blue-600 hover:bg-blue-700 disabled:opacity-40 text-white rounded-xl font-bold text-xs flex items-center gap-1.5 shadow-sm transition-all"
          >
            <span>Send</span>
            <Send className="w-3.5 h-3.5" />
          </button>
        </form>
      </div>

    </div>
  );
}
