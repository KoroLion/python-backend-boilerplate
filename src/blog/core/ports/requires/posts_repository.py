from typing import Protocol

from sqlalchemy.ext.asyncio import AsyncSession

from src.blog.core.domain.post import Post
from src.common.core.ports.requires.repository_protocol import (
    RepositoryProtocol,
)


class PostsRepository(RepositoryProtocol[Post], Protocol):
    async def get_paginated_ordered_by_created_datetime(
        self, page: int, size: int, **kwargs: AsyncSession
    ) -> list[Post]:
        ...
