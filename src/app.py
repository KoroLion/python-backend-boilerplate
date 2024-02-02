import uvicorn
from fastapi import FastAPI

from src.blog.application.routers.posts import posts_router
from src.config import Config
from src.container import initialize_container


def create_app() -> FastAPI:
    initialize_container(config=Config())

    app = FastAPI()
    app.include_router(router=posts_router)

    return app


if __name__ == "__main__":
    uvicorn.run(app="src.app:create_app", host="127.0.0.1", port=8080, reload=True, factory=True)
