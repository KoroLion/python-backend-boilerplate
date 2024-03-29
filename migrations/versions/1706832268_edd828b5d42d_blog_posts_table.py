"""blog_posts_table

Revision ID: edd828b5d42d
Revises: 
Create Date: 2024-02-02 04:04:28.813880

"""
from typing import Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "edd828b5d42d"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "blog_posts",
        sa.Column("uid", sa.Uuid(), nullable=False),
        sa.Column("created_datetime", sa.DateTime(), nullable=False),
        sa.Column("updated_datetime", sa.DateTime(), nullable=True),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("content", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("uid"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("blog_posts")
    # ### end Alembic commands ###
