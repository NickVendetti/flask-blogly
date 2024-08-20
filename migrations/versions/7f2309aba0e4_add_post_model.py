"""Add Post model

Revision ID: 7f2309aba0e4
Revises: f247c4fa8bec
Create Date: 2024-08-19 22:14:25.958165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f2309aba0e4'
down_revision = 'f247c4fa8bec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('first_name',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.Text(),
               existing_nullable=False)
        batch_op.alter_column('last_name',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.Text(),
               existing_nullable=False)
        batch_op.alter_column('image_url',
               existing_type=sa.VARCHAR(),
               type_=sa.Text(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('image_url',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(),
               existing_nullable=False)
        batch_op.alter_column('last_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)
        batch_op.alter_column('first_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###
