import datetime
from uuid import UUID

import pytest

from src.container import Container
from tests.test_data.mock_post import mock_post, mock_post_metadata


@pytest.mark.usefixtures("init_test_database")
async def test_posts_repository(container: Container) -> None:
    posts_repo = container.posts_repository()

    test_posts = {
        mock_post()(
            preview_image="wolf.png",
            metadata=mock_post_metadata(uid=UUID("00000000-0000-0000-0000-000000000001"))(
                created_datetime=datetime.datetime(year=2024, month=1, day=25),
                updated_datetime=datetime.datetime(year=2024, month=1, day=31),
            ),
        ),
        mock_post()(
            preview_image=None,
            metadata=mock_post_metadata(uid=UUID("00000000-0000-0000-0000-000000000002"))(
                created_datetime=datetime.datetime(year=2024, month=1, day=25),
                updated_datetime=None,
            ),
        ),
    }
    for test_post in test_posts:
        await posts_repo.save(obj=test_post)

    for test_post in test_posts:
        assert test_post == await posts_repo.get_by_uid(uid=test_post.metadata.uid)

    assert await posts_repo.get_by_uid(uid=UUID("00000000-0000-0000-0000-000000000010")) is None

    assert await posts_repo.delete_by_uid(uid=UUID("00000000-0000-0000-0000-000000000005")) == 0
    assert await posts_repo.delete_by_uid(uid=UUID("00000000-0000-0000-0000-000000000002")) == 1

    assert await posts_repo.get_by_uid(uid=UUID("00000000-0000-0000-0000-000000000002")) is None
