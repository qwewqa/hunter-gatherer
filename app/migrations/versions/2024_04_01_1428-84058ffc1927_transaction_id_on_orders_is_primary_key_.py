"""transaction id on orders is primary key now


Revision ID: 84058ffc1927
Revises: 61ba12ef75a9
Create Date: 2024-04-01 14:28:58.878327

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "84058ffc1927"
down_revision: Union[str, None] = "61ba12ef75a9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("orders", sa.Column("sqsp_order_id", sa.String(), nullable=True))
    op.drop_index("ix_orders_purchase_id", table_name="orders")
    op.create_index(
        op.f("ix_orders_sqsp_order_id"),
        "orders",
        ["sqsp_order_id"],
        unique=False,
    )
    op.drop_column("orders", "purchase_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "orders",
        sa.Column("purchase_id", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.drop_index(op.f("ix_orders_sqsp_order_id"), table_name="orders")
    op.create_index("ix_orders_purchase_id", "orders", ["purchase_id"], unique=False)
    op.drop_column("orders", "sqsp_order_id")
    # ### end Alembic commands ###
