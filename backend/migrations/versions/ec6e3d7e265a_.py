"""empty message

Revision ID: ec6e3d7e265a
Revises: 
Create Date: 2019-03-15 14:47:03.955152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec6e3d7e265a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password1', sa.String(length=120), nullable=False))
    op.drop_constraint(u'users_password_key', 'users', type_='unique')
    op.create_unique_constraint(None, 'users', ['password1'])
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=20), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'users', type_='unique')
    op.create_unique_constraint(u'users_password_key', 'users', ['password'])
    op.drop_column('users', 'password1')
    # ### end Alembic commands ###