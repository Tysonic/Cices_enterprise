"""empty message

Revision ID: ab3cd8e5ace6
Revises: a32ec6f8be9e
Create Date: 2019-10-29 11:33:17.912899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab3cd8e5ace6'
down_revision = 'a32ec6f8be9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Staffs', sa.Column('date_of_birth', sa.DateTime(), nullable=True))
    op.add_column('Staffs', sa.Column('email', sa.String(), nullable=True))
    op.add_column('Staffs', sa.Column('first_name', sa.String(), nullable=True))
    op.add_column('Staffs', sa.Column('home_address', sa.String(), nullable=True))
    op.add_column('Staffs', sa.Column('next_of_kin', sa.String(), nullable=True))
    op.add_column('Staffs', sa.Column('other_name', sa.String(), nullable=True))
    op.add_column('Staffs', sa.Column('role', sa.String(), nullable=True))
    op.add_column('Staffs', sa.Column('telephone_contact', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Staffs', 'telephone_contact')
    op.drop_column('Staffs', 'role')
    op.drop_column('Staffs', 'other_name')
    op.drop_column('Staffs', 'next_of_kin')
    op.drop_column('Staffs', 'home_address')
    op.drop_column('Staffs', 'first_name')
    op.drop_column('Staffs', 'email')
    op.drop_column('Staffs', 'date_of_birth')
    # ### end Alembic commands ###
