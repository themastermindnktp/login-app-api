"""add_auth_tokens

Revision ID: 16e72e7ba58a
Revises: d9a8ddf02926
Create Date: 2021-06-21 15:38:01.214792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16e72e7ba58a'
down_revision = 'd9a8ddf02926'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('access_token', sa.VARCHAR(length=128), nullable=False),
    sa.Column('refresh_token', sa.VARCHAR(length=128), nullable=False),
    sa.Column('expired_in', sa.Integer(), nullable=False),
    sa.Column('token_type', sa.VARCHAR(length=128), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('access_token'),
    sa.UniqueConstraint('refresh_token')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('auth_tokens')
    # ### end Alembic commands ###