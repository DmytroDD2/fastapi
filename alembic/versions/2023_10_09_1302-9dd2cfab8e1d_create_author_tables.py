"""create author tables

Revision ID: 9dd2cfab8e1d
Revises: 379593f15228
Create Date: 2023-10-09 13:02:50.865456

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9dd2cfab8e1d'
down_revision: Union[str, None] = '379593f15228'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
