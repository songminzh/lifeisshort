# -*- coding: utf-8 -*-
# author by : murphy

import functools
import time

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2018-12-28')

now()

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2018-12-28')

today()
print(today.__name__)

# 设计一个decorator，作用于任何函数，并打印该函数的执行时间

def metric(fn):
    @functools.wraps(fn)
    def counter()
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    return fn