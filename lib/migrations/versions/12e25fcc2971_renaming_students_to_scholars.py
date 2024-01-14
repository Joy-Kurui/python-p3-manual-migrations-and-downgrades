"""Renaming students to scholars

Revision ID: 12e25fcc2971
Revises: 791279dd0760
Create Date: 2024-01-11 00:16:26.335094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12e25fcc2971'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students').q
