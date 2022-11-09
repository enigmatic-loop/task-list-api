"""empty message

Revision ID: 2dd636b1570b
Revises: bdda79cf8293
Create Date: 2022-11-08 17:38:24.475840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dd636b1570b'
down_revision = 'bdda79cf8293'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('task_ids', sa.ARRAY(sa.Integer()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goal', 'task_ids')
    # ### end Alembic commands ###