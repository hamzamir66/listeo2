"""empty message

Revision ID: 277274f960f6
Revises: f8684cf0cb47
Create Date: 2021-08-06 20:51:11.437152

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '277274f960f6'
down_revision = 'f8684cf0cb47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('event_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('content', mysql.VARCHAR(length=1800), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], name='comment_ibfk_2'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='comment_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###