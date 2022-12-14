"""Migracion inicial 3

Revision ID: ed94abf0b6eb
Revises: 
Create Date: 2022-11-16 12:22:47.539450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed94abf0b6eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('salon',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('aula', sa.String(length=20), nullable=True),
    sa.Column('horaEntrada', sa.Time(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('alumno',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('apellido', sa.String(length=100), nullable=False),
    sa.Column('idaula', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['idaula'], ['salon.id'], ),
    sa.PrimaryKeyConstraint('id', 'nombre', 'apellido', 'idaula')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alumno')
    op.drop_table('salon')
    # ### end Alembic commands ###
