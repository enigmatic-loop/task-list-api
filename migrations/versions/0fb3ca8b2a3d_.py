"""empty message

Revision ID: 0fb3ca8b2a3d
Revises: a5c7caef715a
Create Date: 2022-11-09 15:05:34.736390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fb3ca8b2a3d'
down_revision = 'a5c7caef715a'
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