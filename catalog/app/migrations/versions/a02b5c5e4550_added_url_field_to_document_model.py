"""Added url field to Document model

Revision ID: a02b5c5e4550
Revises: f741ba4c6bb1
Create Date: 2024-04-03 22:54:46.398573

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a02b5c5e4550"
down_revision: Union[str, None] = "f741ba4c6bb1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
