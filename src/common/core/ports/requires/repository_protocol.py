from typing import Protocol, TypeVar
from uuid import UUID

T = TypeVar("T")


class RepositoryProtocol(Protocol[T]):
    async def save(self, obj: T) -> None:
        ...

    async def get_by_uid(self, uid: UUID) -> T | None:
        ...

    async def delete_by_uid(self, uid: UUID) -> bool:
        ...
