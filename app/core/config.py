from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "NaijaRates API"
    PROJECT_DESCRIPTION: str = "Expert-grade REST API for real-time Nigerian economic indicators."
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # DB
    DATABASE_URL: str = "sqlite:///./naijarates.db"
    
    # Scheduler
    EXCHANGE_REFRESH_HOURS: int = 6
    FUEL_REFRESH_HOURS: int = 24
    COMMODITY_REFRESH_HOURS: int = 48

    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env")

settings = Settings()
