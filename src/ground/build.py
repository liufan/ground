# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division


if __name__ == '__main__':
    import sys

    command = sys.argv[1]
    args = sys.argv[2:]
    module = __import__('dev')
    method = getattr(module, command)
    if args:
        method(*args)
    else:
        method()
