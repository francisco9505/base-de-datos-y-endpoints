"""empty message

Revision ID: ca61691c6b7a
Revises: eede3c218788
Create Date: 2024-01-11 09:42:04.912826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca61691c6b7a'
down_revision = 'eede3c218788'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rotation_period', sa.String(length=120), nullable=False),
    sa.Column('orbital_period', sa.String(length=80), nullable=False),
    sa.Column('diameter', sa.String(length=80), nullable=False),
    sa.Column('climate', sa.String(length=80), nullable=False),
    sa.Column('gravity', sa.String(length=80), nullable=False),
    sa.Column('terrain', sa.String(length=80), nullable=False),
    sa.Column('surface_water', sa.String(length=80), nullable=False),
    sa.Column('population', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('rotation_period')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###
