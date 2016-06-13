"""add_sql_rule_table

Revision ID: 89b2ca53facd
Revises: 64227a34252e
Create Date: 2016-06-09 17:15:20.252620

"""

# revision identifiers, used by Alembic.
revision = '89b2ca53facd'
down_revision = '64227a34252e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def upgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def upgrade_user_manager():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_user_manager():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def upgrade_validation():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rule_sql',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('rule_sql_id', sa.Integer(), nullable=False),
    sa.Column('rule_sql', sa.Text(), nullable=False),
    sa.Column('rule_number', sa.Text(), nullable=True),
    sa.Column('rule_description', sa.Text(), nullable=False),
    sa.Column('rule_error_message', sa.Text(), nullable=False),
    sa.Column('rule_critical_flag', sa.Boolean(), nullable=False),
    sa.Column('rule_crossfile_flag', sa.Boolean(), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['file_id'], ['file_type.file_id'], ),
    sa.PrimaryKeyConstraint('rule_sql_id')
    )
    ### end Alembic commands ###


def downgrade_validation():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rule_sql')
    ### end Alembic commands ###


def upgrade_staging():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_staging():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###

