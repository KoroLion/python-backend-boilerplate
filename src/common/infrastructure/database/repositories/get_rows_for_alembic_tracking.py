from src.blog.infrastructure.database.repositories.sql_post_row import SQLPostRow
from src.common.infrastructure.database.repositories.sql_alchemy_declarative_base import SQLAlchemyDeclarativeBase


def get_rows_for_alembic_tracking() -> list[type[SQLAlchemyDeclarativeBase]]:
    return [SQLPostRow]
