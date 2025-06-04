"""add content column to posts table

Revision ID: 1372262ec6c3
Revises: 2e4ede2228ac
Create Date: 2025-06-03 17:12:34.777615

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '1372262ec6c3'
down_revision: Union[str, None] = '2e4ede2228ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=True))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
