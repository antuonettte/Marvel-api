"""empty message

Revision ID: 16ddbd8f62f0
Revises: 
Create Date: 2021-09-25 16:28:41.749843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16ddbd8f62f0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=250), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('marvel_character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('comics_appeared_in', sa.Integer(), nullable=True),
    sa.Column('super_power', sa.String(length=50), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('marvel_character')
    op.drop_table('user')
    # ### end Alembic commands ###
