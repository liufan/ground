import ConfigParser
from os.path import expanduser, join, islink, realpath
import logging
from log import info

log = logging.getLogger(__name__)

config_file_name = None


class DatabaseCredential:
    def __init__(self, username, password, instance, unix_socket=None):
        self.username = username
        self.password = password
        self.instance = instance
        self.unix_socket = unix_socket


db_credential = None
cf = None


def init(filename):
    info('init config using file: {}'.format(filename))
    global config_file_name
    config_file_name = filename
    home = expanduser("~")
    config_file = join(home, config_file_name)

    if islink(config_file):
        config_file_name = realpath(config_file)
    global cf
    cf = ConfigParser.ConfigParser()
    cf.read(config_file)


def config():
    if not cf:
        raise Exception('[GROUND said:] config.init() should be called first')
    return cf


def db():
    global db_credential
    if not db_credential:
        db_credential = DatabaseCredential(
            config().get('database', 'username'),
            config().get('database', 'password'),
            config().get('database', 'instance'),
        )
    return db_credential
