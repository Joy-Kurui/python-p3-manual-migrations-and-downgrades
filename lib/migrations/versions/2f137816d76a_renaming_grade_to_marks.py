"""Renaming grade to marks

Revision ID: 2f137816d76a
Revises: 3622031b048a
Create Date: 2024-01-11 00:55:30.642810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f137816d76a'
down_revision = '3622031b048a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'grade', new_column_name='marks')


def downgrade() -> None:
    op.alter_column('students', 'marks', new_column_name='grade')
