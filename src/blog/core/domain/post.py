import datetime
from uuid import UUID

from src.common.core.domain.base_domain_model import BaseDomainModel


class PostMetadata(BaseDomainModel, frozen=True):
    uid: UUID
    created_datetime: datetime.datetime
    updated_datetime: datetime.datetime | None


class Post(BaseDomainModel, frozen=True):
    title: str
    content: str
    metadata: PostMetadata
