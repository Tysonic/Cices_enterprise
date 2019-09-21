"""empty message

Revision ID: 1b54a2f1cfde
Revises: 58eeaf73e8c8
Create Date: 2019-09-21 01:36:48.264996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b54a2f1cfde'
down_revision = '58eeaf73e8c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Staffs',
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('other_name', sa.String(), nullable=True),
    sa.Column('home_address', sa.String(), nullable=True),
    sa.Column('next_of_kin', sa.String(), nullable=True),
    sa.Column('date_of_birth', sa.DateTime(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('telephone_contact', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('user_name')
    )
    op.create_index(op.f('ix_Staffs_user_name'), 'Staffs', ['user_name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Staffs_user_name'), table_name='Staffs')
    op.drop_table('Staffs')
    # ### end Alembic commands ###
