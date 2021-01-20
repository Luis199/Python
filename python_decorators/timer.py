from time import perf_counter
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        print("Duration {}".format(duration))
        return result
    return wrapper


@timer
def fib(n):
    """Returns the value of the fibonacci sequence"""

    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

fib(15)