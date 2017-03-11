import ConfigParser
from os.path import expanduser, join, islink, realpath
import logging
from log import info

log = logging.getLogger(__name__)


def config(filename):
    home = expanduser("~")
    config_file = join(home, filename)
    info('using config file: {}'.format(config_file))

    if islink(config_file):
        config_file = realpath(config_file)

    cf = ConfigParser.ConfigParser()
    cf.read(config_file)
    return cf
