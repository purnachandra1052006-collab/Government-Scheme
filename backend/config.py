import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    GROQ_MODEL: str = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    GROQ_FALLBACK_MODEL: str = "llama3-8b-8192"
    GROQ_BASE_URL: str = "https://api.groq.com/openai/v1"
    
    SCHEMES_DB_PATH: str = os.path.join(
        os.path.dirname(__file__), "data", "schemes_db.json"
    )
    PORT: int = int(os.getenv("PORT", 8000))
    HOST: str = os.getenv("HOST", "0.0.0.0")


config = Config()
