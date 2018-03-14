"""Add started_at and ended_at to worker results.

Revision ID: 727aeeb88b2f
Revises: 094ea67a2baf
Create Date: 2018-02-27 17:16:53.292273

"""

# revision identifiers, used by Alembic.
revision = '727aeeb88b2f'
down_revision = '967036f90ba1'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    """Upgrade the database to a newer revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('package_worker_results', sa.Column('ended_at', sa.DateTime(), nullable=True))
    op.add_column('package_worker_results', sa.Column('started_at', sa.DateTime(), nullable=True))
    op.add_column('worker_results', sa.Column('ended_at', sa.DateTime(), nullable=True))
    op.add_column('worker_results', sa.Column('started_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    """Downgrade the database to an older revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('worker_results', 'started_at')
    op.drop_column('worker_results', 'ended_at')
    op.drop_column('package_worker_results', 'started_at')
    op.drop_column('package_worker_results', 'ended_at')
    # ### end Alembic commands ###