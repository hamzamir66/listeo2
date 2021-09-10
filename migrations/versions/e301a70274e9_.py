"""empty message

Revision ID: e301a70274e9
Revises: c69cb7934c8c
Create Date: 2021-08-06 20:11:27.434075

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e301a70274e9'
down_revision = 'c69cb7934c8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('image1', sa.String(length=20), nullable=False))
    op.add_column('event', sa.Column('image2', sa.String(length=20), nullable=True))
    op.add_column('event', sa.Column('image3', sa.String(length=20), nullable=True))
    op.add_column('event', sa.Column('image4', sa.String(length=20), nullable=True))
    op.add_column('event', sa.Column('image5', sa.String(length=20), nullable=True))
    op.add_column('event', sa.Column('image6', sa.String(length=20), nullable=True))
    op.add_column('event', sa.Column('image7', sa.String(length=20), nullable=True))
    op.drop_column('event', 'banner')
    op.drop_column('event', 'attendee_amount')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('attendee_amount', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('event', sa.Column('banner', mysql.VARCHAR(length=20), nullable=False))
    op.drop_column('event', 'image7')
    op.drop_column('event', 'image6')
    op.drop_column('event', 'image5')
    op.drop_column('event', 'image4')
    op.drop_column('event', 'image3')
    op.drop_column('event', 'image2')
    op.drop_column('event', 'image1')
    # ### end Alembic commands ###
