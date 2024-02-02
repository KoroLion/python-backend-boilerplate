from typing import AsyncGenerator

import pytest

from src.common.infrastructure.database.repositories.sql_alchemy_declarative_base import (
    SQLAlchemyDeclarativeBase,
)
from src.container import Container, initialize_container
from tests.config import TestConfig


@pytest.fixture(scope="module")
def config() -> TestConfig:
    return TestConfig()


@pytest.fixture(scope="module")
def container(config: TestConfig) -> Container:
    return initialize_container(config=TestConfig())


@pytest.fixture(scope="module")
async def init_test_database(container: Container) -> AsyncGenerator[None, None]:
    async with container.sql_async_engine().begin() as conn:
        await conn.run_sync(SQLAlchemyDeclarativeBase.metadata.create_all)

    yield

    async with container.sql_async_engine().begin() as conn:
        await conn.run_sync(SQLAlchemyDeclarativeBase.metadata.drop_all)
