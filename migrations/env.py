import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy.engine import Connection

from src.common.infrastructure.database.repositories.sql_alchemy_declarative_base import (
    SQLAlchemyDeclarativeBase,
)
from src.common.infrastructure.database.repositories.get_rows_for_alembic_tracking import (
get_rows_for_alembic_tracking
)

config = context.config


if config.config_file_name is not None:
    fileConfig(config.config_file_name)


get_rows_for_alembic_tracking()
target_metadata = SQLAlchemyDeclarativeBase.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    from sqlalchemy.ext.asyncio import create_async_engine

    from src.config import Config

    connectable = create_async_engine(url=Config().DATABASE_URL)

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
