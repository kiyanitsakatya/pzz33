import time
import functools
from typing import Callable, Any

def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f" {func.__name__}: {end_time - start_time:.4f} ")
        return result
    return wrapper

def validate_input(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(a: float, b: float, step: float) -> Any:
        if a >= b:
            raise ValueError
        if step <= 0:
            raise ValueError
        return func(a, b, step)
    return wrapper

def log_call(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f" {func.__name__} a={args[0]}, b={args[1]}, step={args[2]}")
        result = func(*args, **kwargs)
        print(f" {func.__name__} {len(result[0])}")
        return result
    return wrapper