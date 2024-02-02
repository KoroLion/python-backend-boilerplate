from src.config import Config


class TestConfig(Config):
    def __init__(self) -> None:
        super().__init__()
        self.DATABASE_URL = "sqlite+aiosqlite://"
