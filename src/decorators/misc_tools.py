import functools as ft
from collections.abc import Callable


def register(func=None, reg: dict = None):
    """Register a function in a function dictionary"""
    if reg is None:
        reg = {}
    if func:
        reg[func.__name__] = func
    else:
        @ft.wraps(func)
        def wrapper(func):
            reg[func.__name__] = func
            return func
        return wrapper


def repeat(_func=None, *, num_times: (int, Callable[[], int]) = 2):
    """decorator used to repeat the execution of a function as specified by num_times
    :arg num_times: the number of repetitions (default=2)"""
    def decorator_repeat(func):
        @ft.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)
