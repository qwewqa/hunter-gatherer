"""fixing our migrations pt 3

Revision ID: c91d379a2583
Revises: ab4c1dc5678f
Create Date: 2024-04-08 15:47:00.061521

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "c91d379a2583"
down_revision: Union[str, None] = "ab4c1dc5678f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "orders",
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("sqsp_transaction_id", sa.String(), nullable=False),
        sa.Column("sqsp_order_id", sa.String(), nullable=True),
        sa.Column("user_emails", postgresql.ARRAY(sa.String()), nullable=False),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("date", sa.DateTime(), nullable=False),
        sa.Column("skus", postgresql.ARRAY(sa.String()), nullable=False),
        sa.Column(
            "payment_platform",
            sa.Enum("STRIPE", "PAYPAL", name="paymentplatform"),
            nullable=False,
        ),
        sa.Column("fee", sa.Float(), nullable=True),
        sa.Column("external_transaction_id", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("sqsp_transaction_id", name=op.f("pk_orders")),
    )
    op.create_index(
        op.f("ix_orders_sqsp_order_id"),
        "orders",
        ["sqsp_order_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_orders_sqsp_transaction_id"),
        "orders",
        ["sqsp_transaction_id"],
        unique=True,
    )
    op.create_table(
        "tracking",
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("cursor", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("cursor", name=op.f("pk_tracking")),
    )
    op.create_index(op.f("ix_tracking_cursor"), "tracking", ["cursor"], unique=True)
    op.create_table(
        "users",
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("pk", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("address", sa.String(), nullable=True),
        sa.Column("phone", sa.String(), nullable=True),
        sa.Column("emergency_contact", sa.String(), nullable=True),
        sa.Column("emergency_contact_phone", sa.String(), nullable=True),
        sa.Column("date_joined", sa.DateTime(), nullable=True),
        sa.Column("date_renewed", sa.DateTime(), nullable=True),
        sa.Column("is_member", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("pk", name=op.f("pk_users")),
    )
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=False)
    op.create_index(op.f("ix_users_pk"), "users", ["pk"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_users_pk"), table_name="users")
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_table("users")
    op.drop_index(op.f("ix_tracking_cursor"), table_name="tracking")
    op.drop_table("tracking")
    op.drop_index(op.f("ix_orders_sqsp_transaction_id"), table_name="orders")
    op.drop_index(op.f("ix_orders_sqsp_order_id"), table_name="orders")
    op.drop_table("orders")
    # ### end Alembic commands ###
