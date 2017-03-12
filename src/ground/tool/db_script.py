# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from fabric.api import local
from config import db


def run_script(script_with_path):
    local('mysql --user={} --password={} --database={} < {}'.format(
        db().username, db().password, db().instance, script_with_path
    ))
