"""empty message

Revision ID: 31b5190e4c92
Revises: 41e8e796ac85
Create Date: 2023-02-07 13:06:02.419180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31b5190e4c92'
down_revision = '41e8e796ac85'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_id', table_name='users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    # ### end Alembic commands ###
