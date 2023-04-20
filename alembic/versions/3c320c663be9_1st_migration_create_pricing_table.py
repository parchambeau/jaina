"""1st migration create pricing table

Revision ID: 3c320c663be9
Revises: 
Create Date: 2023-04-20 02:06:13.421537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c320c663be9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'pricing_data',
        sa.Column('id', sa.String(255), primary_key=True),
        sa.Column('datetime', sa.DateTime, nullable=False),
        sa.Column('interval', sa.String(10), nullable=False),
        sa.Column('ticker', sa.String(10), nullable=False),
        sa.Column('open', sa.Numeric, nullable=False),
        sa.Column('high', sa.Numeric, nullable=False),
        sa.Column('low', sa.Numeric, nullable=False),
        sa.Column('close', sa.Numeric, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('pricing_data')
