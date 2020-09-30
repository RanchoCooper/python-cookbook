#!/usr/bin/env python
# encoding: utf-8
import logging
from functools import wraps


def logged(level, name=None, message=None):
    def decorate(func):
        logName = name if name else func.__module__
        log = logging.getLogger(logName)
        logMsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logMsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.INFO, 'example message')
def spam():
    return 'spam'


if __name__ == '__main__':
    print(add(1, 2))
    print(spam())
