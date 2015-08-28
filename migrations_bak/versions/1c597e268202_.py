"""empty message

Revision ID: 1c597e268202
Revises: 272d1810d04e
Create Date: 2015-08-28 12:59:54.627307

"""

# revision identifiers, used by Alembic.
revision = '1c597e268202'
down_revision = '272d1810d04e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('signup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nume', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=40), nullable=True),
    sa.Column('parola', sa.String(length=20), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('typeevent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('TypeEvent')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('TypeEvent',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('typeevent')
    op.drop_table('type')
    op.drop_table('signup')
    ### end Alembic commands ###
