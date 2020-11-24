import time
from functools import wraps
from logging import getLogger


logger = getLogger()


def time_this(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.info('func {} cost: {}s'.format((func.__name__), end-start))
        return result
    return wrapper
