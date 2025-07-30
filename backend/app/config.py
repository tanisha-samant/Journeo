from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    # Database - Using SQLite for testing
    database_url: str = "sqlite:///./journeo.db"
    
    # JWT
    secret_key: str = "your-secret-key-here"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # API Keys
    groq_api_key: str = ""
    openweather_api_key: str = ""
    openroute_api_key: str = ""
    
    # External API URLs
    exchangerate_api_url: str = "https://api.exchangerate.host"
    libretranslate_api_url: str = "https://libretranslate.de/translate"
    overpass_api_url: str = "https://overpass-api.de/api/interpreter"
    
    # Application
    debug: bool = True
    cors_origins: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings() 