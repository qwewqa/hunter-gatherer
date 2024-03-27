"""adding orders table

Revision ID: 77808ff69881
Revises: fee0499ad54b
Create Date: 2024-03-27 16:29:47.522126

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '77808ff69881'
down_revision: Union[str, None] = 'fee0499ad54b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
        sa.Column('purchase_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('amount', sa.Float(), nullable=False),
        sa.Column('date', sa.DateTime(), nullable=False),
        sa.Column('type', sa.String(), nullable=False),
        sa.Column('method', sa.String(), nullable=True),
        sa.Column('fee', sa.Float(), nullable=True),
        sa.Column('stripe_paypal_id', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_orders_user_id_users')),
        sa.PrimaryKeyConstraint('purchase_id', name=op.f('pk_orders'))
    )
    op.create_index(op.f('ix_orders_purchase_id'), 'orders', ['purchase_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_orders_purchase_id'), table_name='orders')
    op.drop_table('orders')
    # ### end Alembic commands ###
