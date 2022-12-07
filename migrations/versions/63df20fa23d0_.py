"""empty message

Revision ID: 63df20fa23d0
Revises: cab6275b8ec0
Create Date: 2022-12-05 00:36:31.462290

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '63df20fa23d0'
down_revision = 'cab6275b8ec0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('producto', schema=None) as batch_op:
        batch_op.add_column(sa.Column('categoria', sa.JSON(), nullable=True))
        batch_op.drop_column('categoria_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('producto', schema=None) as batch_op:
        batch_op.add_column(sa.Column('categoria_id', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_column('categoria')

    # ### end Alembic commands ###
