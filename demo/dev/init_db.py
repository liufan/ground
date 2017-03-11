# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from ground.tool.log import info
from ground.tool.db_script import run_script
from conf import cfg


def init_db():
    create_schema()


def create_schema():
    info('creating schema ...')
    run_script(cfg(), 'demo/db/schema.sql')
