import datetime
from functools import partial
from uuid import UUID

from src.blog.core.domain.post import Post, PostMetadata


def mock_post_metadata(
    uid: UUID = UUID("00000000-0000-0000-0000-000000000000"),
) -> partial[PostMetadata]:
    return partial(
        PostMetadata,
        uid=uid,
        created_datetime=datetime.datetime(day=25, month=1, year=2024),
        updated_datetime=datetime.datetime(day=31, month=1, year=2024),
    )


def mock_post(
    uid: UUID = UUID("00000000-0000-0000-0000-000000000000"),
) -> partial[Post]:
    return partial(
        Post,
        title="Wolves!",
        content="**Wolves** are howling at the **moon** very loud!",
        metadata=mock_post_metadata(uid=uid)(),
    )
