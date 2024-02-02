import datetime
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from src.common.infrastructure.database.repositories.sql_alchemy_declarative_base import (
    SQLAlchemyDeclarativeBase,
)


class SQLPostRow(SQLAlchemyDeclarativeBase):
    __tablename__ = "blog_posts"

    # metadata
    uid: Mapped[UUID] = mapped_column(primary_key=True)
    created_datetime: Mapped[datetime.datetime]
    updated_datetime: Mapped[datetime.datetime | None]

    title: Mapped[str]
    content: Mapped[str]
