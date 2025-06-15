from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    API_KEY: str
    API_SECRET: str
    TESTNET: bool = True
    BASE_URL: str = "https://testnet.binancefuture.com"
    DEFAULT_SYMBOL: str = "BTCUSDT"
    DEFAULT_QUANTITY: float = 0.001
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings() 