# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from ground.tool.dependencies import pip_install, yum_install


def install_dependencies():
    pip_install('flask')
    pip_install('mysql-python')

