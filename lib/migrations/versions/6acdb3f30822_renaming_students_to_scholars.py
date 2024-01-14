"""Renaming students to scholars

Revision ID: 6acdb3f30822
Revises: 12e25fcc2971
Create Date: 2024-01-11 00:25:15.441720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6acdb3f30822'
down_revision = '12e25fcc2971'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')



def downgrade() -> None:
    op.rename_table('scholars', 'students')
