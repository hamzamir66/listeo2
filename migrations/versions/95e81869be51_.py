"""empty message

Revision ID: 95e81869be51
Revises: 3424f0c297fe
Create Date: 2021-09-01 13:49:43.833364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95e81869be51'
down_revision = '3424f0c297fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_stripe_complete', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_stripe_complete')
    # ### end Alembic commands ###
