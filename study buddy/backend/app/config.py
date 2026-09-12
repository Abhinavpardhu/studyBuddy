import os
from typing import List, Optional
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

# Ensure .env is explicitly loaded into os.environ before Settings initialization
env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
if os.path.exists(env_path):
    load_dotenv(env_path)

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Regional-Language Personal Tutor"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"
    
    # Database
    DATABASE_URL: str = "sqlite:///./app.db"
    
    # Auth / JWT
    JWT_SECRET_KEY: str = "dev_hackathon_secret_key_change_me_987654321"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours
    
    # Storage & Upload limits
    MAX_UPLOAD_SIZE_MB: int = 20
    UPLOAD_DIR: str = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "uploads")
    VECTOR_DIR: str = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "vectorstore")
    
    # Gemini API Keys pool (Supports 10+ key load balancing)
    GEMINI_API_KEY_1: Optional[str] = None
    GEMINI_API_KEY_2: Optional[str] = None
    GEMINI_API_KEY_3: Optional[str] = None
    GEMINI_API_KEY_4: Optional[str] = None
    GEMINI_API_KEY_5: Optional[str] = None
    GEMINI_API_KEY_6: Optional[str] = None
    GEMINI_API_KEY_7: Optional[str] = None
    GEMINI_API_KEY_8: Optional[str] = None
    GEMINI_API_KEY_9: Optional[str] = None
    GEMINI_API_KEY_10: Optional[str] = None
    GEMINI_API_KEYS: List[str] = []

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    def refresh_api_keys(self) -> List[str]:
        # Reload .env if it exists
        if os.path.exists(env_path):
            load_dotenv(env_path, override=True)
            
        keys = []
        for env_key, env_val in os.environ.items():
            if (env_key.startswith("GEMINI_API_KEY") or env_key.startswith("GOOGLE_API_KEY")) and env_val and env_val.strip():
                val = env_val.strip()
                if val not in keys and not val.startswith("your_gemini_api_key"):
                    keys.append(val)
        
        for i in range(1, 21):
            val = getattr(self, f"GEMINI_API_KEY_{i}", None)
            if val and val.strip() and val.strip() not in keys and not val.startswith("your_gemini_api_key"):
                keys.append(val.strip())
                
        self.GEMINI_API_KEYS = keys
        return keys

    def __init__(self, **values):
        super().__init__(**values)
        self.refresh_api_keys()

settings = Settings()

# Ensure target directories exist
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
os.makedirs(settings.VECTOR_DIR, exist_ok=True)

