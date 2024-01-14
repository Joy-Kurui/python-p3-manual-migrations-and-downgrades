"""Revision -m R

Revision ID: 302268913066
Revises: 6acdb3f30822
Create Date: 2024-01-11 00:36:32.060223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '302268913066'
down_revision = '6acdb3f30822'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'grade', new_column_name='marks')




def downgrade() -> None:
    op.alter_column('students', 'marks', new_column_name='grade')
