"""Renaming grade to marks

Revision ID: 3622031b048a
Revises: 302268913066
Create Date: 2024-01-11 00:49:03.275253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3622031b048a'
down_revision = '302268913066'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'grade', new_column_name='marks')



def downgrade() -> None:
    op.alter_column('students', 'marks', new_column_name='grade')
