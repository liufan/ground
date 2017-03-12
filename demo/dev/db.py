# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from ground.tool.log import info
from ground.tool.db_script import run_script, drop_all_tables


database_resource_dir = 'demo/db'


def init_db():
    drop_all_tables()
    create_schema()


def create_schema():
    info('creating schema ...')

    run_script('{}/schema.sql'.format(database_resource_dir))


def migrate():
    from ground.tool.migrate import migrate as do_migrate
    do_migrate(database_resource_dir)


