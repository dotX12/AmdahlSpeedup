import time
from functools import wraps


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        timing_func = float(f"{te-ts:.4f}")
        print(f'func: {f.__name__} Время выполнения - {timing_func} сек.')
        return result
    return wrap
