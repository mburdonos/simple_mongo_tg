"""Settings"""
import os

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_DIR = os.path.join(BASE_DIR, "..", "..")


class Project(BaseModel):
    name: str

class TelegramBot(BaseModel):
    name: str
    token: str

class Settings(BaseSettings):
    project: Project
    telegram_bot: TelegramBot

    model_config = SettingsConfigDict(env_file=os.path.join(ENV_DIR, ".env"), env_nested_delimiter="__")


settings = Settings()