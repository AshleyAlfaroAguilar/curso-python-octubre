"""create alumnos and notas tables

Revision ID: 0e7c8efaf97d
Revises: 
Create Date: 2022-12-13 16:49:06.764242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e7c8efaf97d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alumnos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombres', sa.String(), nullable=False),
    sa.Column('apellidos', sa.String(), nullable=False),
    sa.Column('carnet', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('curso', sa.String(), nullable=True),
    sa.Column('nota', sa.Integer(), nullable=True),
    sa.Column('alumno_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['alumno_id'], ['alumnos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notas')
    op.drop_table('alumnos')
    # ### end Alembic commands ###
