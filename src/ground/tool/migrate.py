# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
import os
import sys
from dbi import from_db, transactional
from log import *
from db_script import run_script

migration_record_table_name = 'db_migration'


@transactional
def ensure_migration_record_table_exist():
    if len(from_db().list("show tables like '{}'".format(migration_record_table_name))) == 0:
        info('init db migration record table...')
        from_db().execute('CREATE TABLE db_migration (latest_version INT)')
        from_db().insert('db_migration', latest_version=0)


def migrate(script_dir):
    ensure_migration_record_table_exist()
    versions = load_versions(script_dir)
    if len(versions) == 0:
        warn('No migration script found!')
        sys.exit(0)
    latest_version = get_database_latest_version()
    version_numbers = sorted(versions.keys())
    if latest_version > version_numbers[-1]:
        error('Error: database version is late than migration script, SOMETHING WRONG!')
        sys.exit(-1)
    elif latest_version == version_numbers[-1]:
        info('database version [{}] is up to date'.format(latest_version))
        sys.exit(0)
    for version_number in version_numbers:
        if version_number > latest_version:
            info('migrating: {}'.format(versions[version_number]))
            run_script(versions[version_number])
            update_database_version(version_number)

    warn('database migration finished, from {} to {}'.format(latest_version, version_numbers[-1]))


@transactional
def update_database_version(version):
    from_db().execute('update db_migration set latest_version=%(version)s', version=version)


def get_database_latest_version():
    return from_db().get_scalar('select latest_version from db_migration')


def load_versions(script_dir):
    versions = {}
    for file_name in os.listdir(script_dir):
        if '-' in file_name and file_name.endswith('.sql'):
            version = int(file_name.split('-')[0])
            versions[version] = '{}/{}'.format(script_dir, file_name)
    return versions
