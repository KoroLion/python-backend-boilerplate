from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.blog.core.domain.post import Post
from src.blog.core.ports.requires.posts_repository import PostsRepository
from src.container import Container
from tests.test_data.mock_post import mock_post

posts_router = APIRouter()


@posts_router.get("/blog/posts", tags=["blog"])
@inject
async def get_posts(
    posts_repo: PostsRepository = Depends(Provide[Container.posts_repository]),
) -> list[Post]:
    post = mock_post()()

    await posts_repo.save(obj=post)

    result = await posts_repo.get_by_uid(uid=post.metadata.uid)

    await posts_repo.delete_by_uid(uid=post.metadata.uid)

    if result:
        return [result]
    return []
