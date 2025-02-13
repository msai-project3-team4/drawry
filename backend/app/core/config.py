from pydantic_settings import BaseSettings
from pydantic import validator
from typing import Any, Dict, Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Drawry"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # Azure Settings
    AZURE_SPEECH_KEY: str
    AZURE_SPEECH_REGION: str
    AZURE_STORAGE_CONNECTION_STRING: str
    AZURE_STORAGE_CONTAINER_NAME: str
    AZURE_OPENAI_KEY: str
    AZURE_OPENAI_ENDPOINT: str
    AZURE_CONTROLNET_ENDPOINT: str

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()