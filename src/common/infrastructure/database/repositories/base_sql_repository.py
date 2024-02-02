from typing import Any, TypeVar

from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker

T = TypeVar("T")


def transactional(f: Any) -> Any:
    async def _decorator(self: BaseSQLRepository, *args: Any, **kwargs: Any) -> Any:
        session = self.create_session()
        kwargs["session"] = session
        try:
            result = await f(self, *args, **kwargs)
            await session.commit()
        except Exception as err:
            await session.rollback()
            raise err
        finally:
            await session.close()
        return result

    return _decorator


class BaseSQLRepository:
    def __init__(self, async_engine: AsyncEngine) -> None:
        self._async_engine = async_engine
        self._async_sessionmaker = async_sessionmaker(bind=self._async_engine, expire_on_commit=False)

    def create_session(self) -> AsyncSession:
        return self._async_sessionmaker()
