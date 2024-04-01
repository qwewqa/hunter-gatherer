"""parity changes for data import

Revision ID: cfa3bf7190f7
Revises: bf79838d9a83
Create Date: 2024-04-01 11:40:50.533126

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "cfa3bf7190f7"
down_revision: Union[str, None] = "bf79838d9a83"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    payment_platform = sa.Enum("STRIPE", "PAYPAL", name="paymentplatform")
    payment_platform.create(op.get_bind())

    op.add_column(
        "orders",
        sa.Column("user_emails", postgresql.ARRAY(sa.String()), nullable=False),
    )
    op.add_column(
        "orders",
        sa.Column(
            "payment_platform",
            sa.Enum("STRIPE", "PAYPAL", name="paymentplatform"),
            nullable=False,
        ),
    )
    op.add_column(
        "orders",
        sa.Column("external_transaction_id", sa.String(), nullable=True),
    )
    op.drop_column("orders", "foreign_transaction_id")
    op.drop_column("orders", "user_ids")
    op.drop_column("orders", "payment_method")
    op.alter_column(
        "products",
        "sku",
        existing_type=sa.VARCHAR(),
        server_default=None,
        existing_nullable=False,
    )
    op.add_column("users", sa.Column("emergency_contact", sa.String(), nullable=True))
    op.add_column(
        "users",
        sa.Column("emergency_contact_phone", sa.String(), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "emergency_contact_phone")
    op.drop_column("users", "emergency_contact")
    op.alter_column(
        "products",
        "sku",
        existing_type=sa.VARCHAR(),
        server_default=sa.text("nextval('products_sku_seq'::regclass)"),
        existing_nullable=False,
    )
    op.add_column(
        "orders",
        sa.Column("payment_method", sa.VARCHAR(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "orders",
        sa.Column(
            "user_ids",
            postgresql.ARRAY(sa.VARCHAR()),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.add_column(
        "orders",
        sa.Column(
            "foreign_transaction_id",
            sa.VARCHAR(),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.drop_column("orders", "external_transaction_id")
    op.drop_column("orders", "payment_platform")
    op.drop_column("orders", "user_emails")

    payment_platform = sa.Enum("STRIPE", "PAYPAL", name="paymentplatform")
    payment_platform.drop(op.get_bind())
    # ### end Alembic commands ###
