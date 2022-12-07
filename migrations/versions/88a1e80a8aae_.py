"""empty message

Revision ID: 88a1e80a8aae
Revises: 63df20fa23d0
Create Date: 2022-12-05 01:11:40.059911

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '88a1e80a8aae'
down_revision = '63df20fa23d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('producto', schema=None) as batch_op:
        batch_op.alter_column('categoria',
               existing_type=mysql.JSON(),
               type_=sa.Integer(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('producto', schema=None) as batch_op:
        batch_op.alter_column('categoria',
               existing_type=sa.Integer(),
               type_=mysql.JSON(),
               existing_nullable=True)

    # ### end Alembic commands ###