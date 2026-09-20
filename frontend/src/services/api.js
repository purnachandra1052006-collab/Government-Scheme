const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function checkHealth() {
  try {
    const res = await fetch(`${API_BASE_URL}/api/health`);
    if (!res.ok) throw new Error("Backend unavailable");
    return await res.json();
  } catch (err) {
    console.warn("Backend health check warning:", err);
    return { status: "offline", schemes_loaded: 0, groq_configured: false };
  }
}

export async function getAllSchemes() {
  const res = await fetch(`${API_BASE_URL}/api/schemes`);
  if (!res.ok) throw new Error("Failed to load schemes");
  return await res.json();
}

export async function startChatSession() {
  const res = await fetch(`${API_BASE_URL}/api/chat/start`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
  });
  if (!res.ok) throw new Error("Failed to start chat session");
  return await res.json();
}

export async function sendChatMessage(sessionId, currentProfile, userMessage, field = null, value = null) {
  const res = await fetch(`${API_BASE_URL}/api/chat/message`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      session_id: sessionId,
      current_profile: currentProfile,
      user_message: userMessage,
      field: field,
      value: value,
    }),
  });
  if (!res.ok) throw new Error("Failed to process conversational turn");
  return await res.json();
}

export async function evaluateProfile(profile) {
  const res = await fetch(`${API_BASE_URL}/api/evaluate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(profile),
  });
  if (!res.ok) {
    const errData = await res.json().catch(() => ({}));
    throw new Error(errData.detail || "Evaluation failed");
  }
  return await res.json();
}

export async function setGroqApiKey(apiKey) {
  const res = await fetch(`${API_BASE_URL}/api/config/groq-key`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ api_key: apiKey }),
  });
  if (!res.ok) throw new Error("Failed to set Groq key");
  return await res.json();
}
