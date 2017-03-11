# -*- coding: utf-8 -*-
from fabric.api import local
from log import *


def run_script(cfg, script_with_path):
    local('mysql --user={} --password={} --database={} < {}'.format(
        cfg.get('database','username'),
        cfg.get('database','password'),
        cfg.get('database','instance'),
        script_with_path
    ))

