import inspect


def info(message):
    print(green('[info]{}: {}'.format(get_caller(),message)))


def warn(message):
    print(yellow('[warn] {}'.format(message)))


def error(message):
    print(red('[error] {}'.format(message)))


def _wrap_with(code):
    def inner(text, bold=False):
        c = code
        if bold:
            c = "1;%s" % c
        return "\033[%sm%s\033[0m" % (c, text)

    return inner


def get_caller():
    return inspect.currentframe().f_back.f_back.f_code.co_filename


red = _wrap_with('31')
green = _wrap_with('32')
yellow = _wrap_with('33')

if __name__=='__main__':
    info('should tell me the caller')
