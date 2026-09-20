import React, { useState, useEffect, useRef } from "react";
import { 
  Send, 
  Sparkles, 
  Bot, 
  User, 
  RotateCcw, 
  ArrowRight,
  HelpCircle,
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
  const [quickReplies, setQuickReplies] = useState([]);
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
      setMessages(sess.history || []);
      setProfile(sess.profile || {});
      setQuickReplies(sess.suggested_quick_replies || []);
    } catch (err) {
      console.error("Failed to start chat session:", err);
      const fallbackWelcome = {
        role: "assistant",
        content: "Namaste & Welcome to GovScheme.AI! I am your AI Government Welfare Advisor. Tell me about yourself (such as your occupation, age, state, or any specific support you need), or pick an option below to begin.",
        quick_options: [
            "💼 I am an Entrepreneur seeking business loans",
            "🎓 I am a Student looking for scholarships",
            "🌾 I am a Farmer looking for crop & income support",
            "☀️ I want Solar Rooftop subsidies for my home",
            "🤰 I am an expecting mother looking for maternity benefits"
        ]
      };
      setMessages([fallbackWelcome]);
      setQuickReplies(fallbackWelcome.quick_options);
    } finally {
      setLoading(false);
    }
  };

  const handleSendMessage = async (textToSend, field = null, value = null) => {
    const text = textToSend?.trim();
    if (!text || loading) return;

    setLoading(true);
    setInputValue("");

    // Optimistically append user message
    const userMsg = { role: "user", content: text };
    setMessages((prev) => [...prev, userMsg]);

    try {
      const sessionId = session?.session_id || "session_default";
      const updatedSession = await sendChatMessage(sessionId, profile, text, field, value);
      
      setSession(updatedSession);
      setMessages(updatedSession.history);
      setProfile(updatedSession.profile);
      setQuickReplies(updatedSession.suggested_quick_replies || []);

      // If user requested or profile is ready for evaluation
      if (updatedSession.is_complete) {
        onCompleteEvaluation(updatedSession.profile);
      }
    } catch (err) {
      console.error("Error communicating with AI Advisor:", err);
      const errMsg = {
        role: "assistant",
        content: "I understood your response and updated your profile. You can continue sharing details or click below to evaluate your schemes.",
        quick_options: ["🚀 Run Scheme Eligibility Match", "☀️ Tell me about Solar Subsidy", "💼 Business Loan Subsidy"]
      };
      setMessages((prev) => [...prev, errMsg]);
    } finally {
      setLoading(false);
    }
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();
    if (inputValue.trim()) {
      handleSendMessage(inputValue.trim());
    }
  };

  const handleQuickReplyClick = (replyText) => {
    if (replyText.includes("Run Scheme Eligibility Match") || replyText.includes("Evaluate")) {
      onCompleteEvaluation(profile);
    } else {
      handleSendMessage(replyText);
    }
  };

  return (
    <div className="bg-white rounded-3xl border border-slate-200 shadow-sm overflow-hidden flex flex-col h-[680px]">
      
      {/* Header */}
      <div className="px-6 py-4 border-b border-slate-100 bg-slate-50/80 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-2xl bg-gradient-to-tr from-blue-700 via-indigo-600 to-amber-500 text-white flex items-center justify-center font-bold shadow-sm">
            <Bot className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h3 className="font-extrabold text-sm text-slate-900">
                AI Welfare Advisor (Conversational Intake)
              </h3>
              <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
            </div>
            <p className="text-[11px] text-slate-500">Talk naturally in English/Hinglish • Extracts attributes & answers queries</p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          {session && (
            <span className="text-[11px] font-bold text-blue-700 bg-blue-50 border border-blue-200 px-3 py-1 rounded-full">
              Step {session.current_step} of {session.total_steps}
            </span>
          )}
          <button
            onClick={initChat}
            className="p-2 text-slate-400 hover:text-slate-700 hover:bg-slate-200/60 rounded-xl transition-colors"
            title="Restart conversation"
          >
            <RotateCcw className="w-4 h-4" />
          </button>
        </div>
      </div>

      {/* Messages Scroll Area */}
      <div className="flex-1 p-6 overflow-y-auto space-y-4 bg-gradient-to-b from-white via-slate-50/20 to-slate-50/50">
        {messages.map((msg, idx) => {
          const isAssistant = msg.role === "assistant";

          return (
            <div
              key={idx}
              className={`flex items-start gap-3.5 ${isAssistant ? "" : "flex-row-reverse"}`}
            >
              <div
                className={`w-8 h-8 rounded-2xl flex items-center justify-center shrink-0 font-bold text-xs shadow-xs ${
                  isAssistant
                    ? "bg-gradient-to-tr from-blue-700 to-indigo-600 text-white"
                    : "bg-slate-800 text-white"
                }`}
              >
                {isAssistant ? <Bot className="w-4 h-4" /> : <User className="w-4 h-4" />}
              </div>

              <div className={`max-w-[85%] space-y-2 ${isAssistant ? "" : "text-right"}`}>
                <div
                  className={`p-4 rounded-3xl text-xs sm:text-sm leading-relaxed shadow-xs inline-block text-left ${
                    isAssistant
                      ? "bg-white border border-slate-200/80 text-slate-800 rounded-tl-none font-normal"
                      : "bg-blue-600 text-white rounded-tr-none font-medium"
                  }`}
                >
                  {msg.content}
                </div>
              </div>
            </div>
          );
        })}

        {loading && (
          <div className="flex items-center gap-2 text-slate-400 text-xs py-2">
            <div className="w-2 h-2 rounded-full bg-blue-600 animate-bounce" />
            <div className="w-2 h-2 rounded-full bg-blue-600 animate-bounce [animation-delay:0.2s]" />
            <div className="w-2 h-2 rounded-full bg-blue-600 animate-bounce [animation-delay:0.4s]" />
            <span className="text-[11px] text-slate-500 font-medium">AI Advisor is thinking & extracting attributes...</span>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Dynamic Suggested Quick-Replies Chips */}
      {quickReplies && quickReplies.length > 0 && !loading && (
        <div className="px-5 py-2.5 bg-slate-50 border-t border-slate-100 flex items-center gap-2 overflow-x-auto scrollbar-thin">
          <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider shrink-0 flex items-center gap-1">
            <Sparkles className="w-3 h-3 text-amber-500" />
            Suggested:
          </span>
          {quickReplies.map((reply, rIdx) => (
            <button
              key={rIdx}
              onClick={() => handleQuickReplyClick(reply)}
              className="px-3 py-1.5 rounded-xl text-xs font-semibold bg-white border border-slate-200 text-slate-700 hover:bg-blue-50 hover:border-blue-300 hover:text-blue-700 whitespace-nowrap transition-all shadow-2xs shrink-0"
            >
              {reply}
            </button>
          ))}
        </div>
      )}

      {/* Input Box Footer */}
      <div className="p-4 border-t border-slate-200 bg-white">
        <form onSubmit={handleFormSubmit} className="flex items-center gap-2">
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            disabled={loading}
            placeholder="Type your message, ask about any scheme, or tell me your details (e.g. 'I am a 24 yr old student in UP')..."
            className="flex-1 px-4 py-3 text-xs sm:text-sm bg-slate-50 border border-slate-200 rounded-2xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:bg-white transition-all"
          />
          
          <button
            type="submit"
            disabled={!inputValue.trim() || loading}
            className="px-5 py-3 bg-blue-600 hover:bg-blue-700 disabled:opacity-40 text-white rounded-2xl font-bold text-xs flex items-center gap-2 shadow-sm transition-all"
          >
            <span>Send</span>
            <Send className="w-3.5 h-3.5" />
          </button>
        </form>
      </div>

    </div>
  );
}
