"""empty message

Revision ID: 6a3f54c2ab7e
Revises: e09365b6a359
Create Date: 2023-01-04 14:51:22.660606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a3f54c2ab7e'
down_revision = 'e09365b6a359'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=255), nullable=True),
    sa.Column('apellido', sa.String(length=255), nullable=True),
    sa.Column('rut', sa.String(length=255), nullable=True),
    sa.Column('correo', sa.String(length=255), nullable=True),
    sa.Column('telefono', sa.String(length=255), nullable=True),
    sa.Column('contrasena', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('usuario_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    # ### end Alembic commands ###
