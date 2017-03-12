import ConfigParser
from os.path import expanduser, join, islink, realpath
import logging
from log import info

log = logging.getLogger(__name__)

config_file_name = None


class DatabaseCredential:
    def __init__(self, username, password, instance, host='127.0.0.1', port=3306, unix_socket=None):
        self.username = username
        self.password = password
        self.instance = instance
        self.host = host
        if isinstance(port, basestring):
            port = int(port)
        self.port = port

        self.unix_socket = unix_socket

    def __repr__(self):
        return DatabaseCredential.__dict__.__repr__()


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
            username=config().get('database', 'username'),
            password=config().get('database', 'password'),
            instance=config().get('database', 'instance'),
            host=config().get('database', 'host'),
            port=config().get('database', 'port'),
            unix_socket=config().get('database', 'unix_socket'),
        )
    return db_credential
