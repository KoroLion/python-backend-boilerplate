from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import create_async_engine

from src import blog
from src.blog.infrastructure.database.repositories.sql_posts_repository import (
    SQLPostsRepository,
)
from src.config import Config


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    sql_async_engine = providers.Singleton(create_async_engine, url=config.DATABASE_URL)

    posts_repository = providers.Singleton(SQLPostsRepository, async_engine=sql_async_engine)


def initialize_container(config: Config) -> Container:
    container = Container()
    container.config.from_dict(config.model_dump(mode="json"))

    container.wire(packages=[blog])

    return container
