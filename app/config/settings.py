from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    #앱 환경 설정
    APP_NAME: str
    APP_ENV: str
    APP_DEBUG: bool
    APP_HOST: str
    APP_PORT: int

    #CORS
    CORS_ORIGINS: str

    #네이버 데이터랩 통합검색 API 호출 시 필요 정보
    CLIENT_ID: str
    CLIENT_SECRET: str

    model_config = SettingsConfigDict(
        env_file = str(BASE_DIR / ".env"),
        env_file_encoding="utf-8"
    )

    @property
    def cors_origins(self) -> list[str]:
        return [o.strip() for o in self.CORS_ORIGINS.split(",") if o.strip()]
    
settings = Settings()