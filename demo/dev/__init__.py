# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

from setup import install_dependencies
from db import init_db, migrate
from init import do_init

do_init()

