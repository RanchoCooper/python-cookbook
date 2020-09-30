#!/usr/bin/env python
# encoding: utf-8
import time
from functools import wraps


def time_this(func):
    """
    Decorator that reports the execution time.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


@time_this
def countdown(n):
    """
    counts down
    """
    while n > 0:
        n -= 1


if __name__ == '__main__':
    countdown(10)
    countdown(100)
    countdown(1000)
    countdown(10000)
    countdown(100000)
    countdown(1000000)
    print(countdown.__name__)
    print(countdown.__doc__)
    print(countdown.__annotations__)
    print(countdown.__wrapped__.__name__)
    print(countdown.__wrapped__.__doc__)
