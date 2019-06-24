"""empty message

Revision ID: 48081006d781
Revises: 
Create Date: 2019-06-24 14:18:07.079699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48081006d781'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brands',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('discount', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('brand_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['brand_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['brands.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('categories')
    op.drop_table('brands')
    # ### end Alembic commands ###
