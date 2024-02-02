from uuid import UUID

from sqlalchemy import delete, select

from src.blog.core.domain.post import Post, PostMetadata
from src.blog.core.ports.requires.posts_repository import PostsRepository
from src.blog.infrastructure.database.repositories.sql_post_row import SQLPostRow
from src.common.infrastructure.database.repositories.base_sql_repository import (
    BaseSQLRepository,
    transactional,
)


class SQLPostsRepository(PostsRepository, BaseSQLRepository):
    @transactional
    async def save(self, obj: Post) -> None:
        await self.session.merge(instance=self._serialize_post(post=obj))

    @transactional
    async def get_by_uid(self, uid: UUID) -> Post | None:
        post_row = (await self.session.scalars(select(SQLPostRow).where(SQLPostRow.uid == uid))).one_or_none()
        if not post_row:
            return None
        return self._deserialize_sql_post_row(post_row=post_row)

    @transactional
    async def delete_by_uid(self, uid: UUID) -> bool:
        result = await self.session.execute(delete(SQLPostRow).where(SQLPostRow.uid == uid))
        return result.rowcount == 1

    @transactional
    async def get_paginated_ordered_by_created_datetime(self, page: int, size: int) -> list[Post]:
        post_rows = (
            await self.session.scalars(
                select(SQLPostRow).limit(size).offset((page - 1) * size).order_by(SQLPostRow.created_datetime.desc())
            )
        ).all()
        return [self._deserialize_sql_post_row(post_row=post_row) for post_row in post_rows]

    @staticmethod
    def _deserialize_sql_post_row(post_row: SQLPostRow) -> Post:
        return Post(
            title=post_row.title,
            content=post_row.content,
            metadata=PostMetadata(
                uid=post_row.uid,
                created_datetime=post_row.created_datetime,
                updated_datetime=post_row.updated_datetime,
            ),
        )

    @staticmethod
    def _serialize_post(post: Post) -> SQLPostRow:
        return SQLPostRow(
            uid=post.metadata.uid,
            created_datetime=post.metadata.created_datetime,
            updated_datetime=post.metadata.updated_datetime,
            title=post.title,
            content=post.content,
        )
