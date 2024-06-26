"""Added description field to Document model

Revision ID: 332cc4b0cfb7
Revises: 09aaae524f88
Create Date: 2024-04-03 22:59:09.767240

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "332cc4b0cfb7"
down_revision: Union[str, None] = "09aaae524f88"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "documents", sa.Column("description", sa.String(length=2500), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("documents", "description")
    # ### end Alembic commands ###
