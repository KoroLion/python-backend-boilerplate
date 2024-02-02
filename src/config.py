import os

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DATABASE_URL: str = os.environ.get("DATABASE_URL", "postgresql+psycopg://admin:admin@localhost:15432/dev_database")
