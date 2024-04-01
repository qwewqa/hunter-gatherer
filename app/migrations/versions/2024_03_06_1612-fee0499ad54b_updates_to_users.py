"""updates to users

Revision ID: fee0499ad54b
Revises: 1c2c533ab573
Create Date: 2024-03-06 16:12:49.543609

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "fee0499ad54b"
down_revision: Union[str, None] = "1c2c533ab573"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("status", sa.String(), nullable=True))
    op.add_column("users", sa.Column("types", sa.String(), nullable=True))
    op.add_column("users", sa.Column("address", sa.String(), nullable=True))
    op.add_column("users", sa.Column("phone", sa.String(), nullable=True))
    op.add_column("users", sa.Column("usps", sa.String(), nullable=True))
    op.add_column("users", sa.Column("date_joined", sa.Date(), nullable=True))
    op.add_column("users", sa.Column("date_renewed", sa.Date(), nullable=True))
    op.add_column("users", sa.Column("emergency_contact", sa.String(), nullable=True))
    op.add_column("users", sa.Column("emergency_phone", sa.String(), nullable=True))
    op.add_column("users", sa.Column("is_member", sa.Boolean(), nullable=True))
    op.add_column("users", sa.Column("date_expired", sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "date_expired")
    op.drop_column("users", "is_member")
    op.drop_column("users", "emergency_phone")
    op.drop_column("users", "emergency_contact")
    op.drop_column("users", "date_renewed")
    op.drop_column("users", "date_joined")
    op.drop_column("users", "usps")
    op.drop_column("users", "phone")
    op.drop_column("users", "address")
    op.drop_column("users", "types")
    op.drop_column("users", "status")
    # ### end Alembic commands ###
