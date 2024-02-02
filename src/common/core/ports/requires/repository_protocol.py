from typing import Protocol, TypeVar
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar("T")


class RepositoryProtocol(Protocol[T]):
    async def save(self, obj: T, **kwargs: AsyncSession) -> None:
        ...

    async def get_by_uid(self, uid: UUID, **kwargs: AsyncSession) -> T | None:
        ...

    async def delete_by_uid(self, uid: UUID, **kwargs: AsyncSession) -> bool:
        ...
