"""add foreign key to posts table

Revision ID: 99a802144231
Revises: 3826c6dbfa0f
Create Date: 2025-06-03 17:31:24.848261

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '99a802144231'
down_revision: Union[str, None] = '3826c6dbfa0f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('user_id', sa.Integer, nullable=False))
    op.create_foreign_key('post_users_fk', 'posts', 'users', ['user_id'], ['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', 'posts', type_='foreignkey')
    op.drop_column('posts', 'user_id')
    pass
