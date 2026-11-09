from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config= SettingsConfigDict(
        env_file= ".env",
        env_file_encoding= "utf-8",
        extra= "ignore",
    )

    app_name: str = "Gestion Business API"
    app_version: str = "0.1.0"
    environment: str = "dev"

    database_url: str = "sqlite:///./dev.db"

    #timezone: str = "America/Toronto"
    api_prefix: str = "/api/v1"


@lru_cache
def get_settings()-> Settings:
    return Settings()