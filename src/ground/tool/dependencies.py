# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
import pip
import imp

def yum_install(package):
    run_local('sudo yum install {}'.format(package))


def pip_install(package):
    import_or_install(package)


def run_local(cmd):
    import_or_install('fabric')
    try:
        from fabric.api import local
        local(cmd)
    except:
        print('[GROUND said:] fail to run local command: {}'.format(cmd))
        import traceback
        traceback.print_exc()


def import_or_install(package):
    try:
        imp.find_module(package)
    except ImportError:
        pip.main(['install', package])


if __name__ == '__main__':
    pip_install('flask')
