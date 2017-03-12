# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from fabric.api import local
from config import db


def run_script(script_with_path):
    local('mysql --user={} --password={} --database={} < {}'.format(
        db().username, db().password, db().instance, script_with_path
    ))


def drop_all_tables():
    local('mysqldump -u{user} -p{passwd} -h {host} --add-drop-table --no-data {instance} '
          ' | grep ^DROP '
          ' | mysql -u{user} -p{passwd} -h {host} {instance}'.format(
            user=db().username,
            passwd=db().password,
            instance=db().instance,
            host=db().host
        )
    )
