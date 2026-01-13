

import time
import functools
from typing import Callable, Any
import math


def timer_decorator(func: Callable) -> Callable:
    """
    Декоратор для измерения времени выполнения функции
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"⏱️  Функция '{func.__name__}' выполнена за {end_time - start_time:.6f} секунд")
        return result
    return wrapper


def validate_input_decorator(min_val: float = -float('inf'), 
                            max_val: float = float('inf')) -> Callable:
    """
    Декоратор для валидации входных параметров
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(x: float) -> float:
            if not isinstance(x, (int, float)):
                raise TypeError(f"Аргумент должен быть числом, получен {type(x)}")
            
            if x < min_val or x > max_val:
                raise ValueError(f"Аргумент должен быть в пределах [{min_val}, {max_val}], получен {x}")
            
            # Проверка на особые случаи для математических функций
            if func.__name__ in ['sqrt_function', 'log_function'] and x <= 0:
                raise ValueError(f"Для функции {func.__name__} аргумент должен быть > 0")
            
            if func.__name__ == 'tan_function':
                # Проверка на аргументы, где тангенс не определен
                if abs((x - math.pi/2) % math.pi) < 1e-10:
                    raise ValueError(f"Тангенс не определен для x = {x}")
            
            return func(x)
        return wrapper
    return decorator


def cache_decorator(func: Callable) -> Callable:
    """
    Декоратор для кэширования результатов вычислений
    """
    cache = {}
    
    @functools.wraps(func)
    def wrapper(x: float) -> float:
        # Используем округление для ключа кэша
        key = round(x, 10)
        
        if key not in cache:
            cache[key] = func(x)
            print(f"💾 Вычислено новое значение для x = {x}")
        else:
            print(f"⚡ Использовано кэшированное значение для x = {x}")
        
        return cache[key]
    
    # Добавляем метод для очистки кэша
    wrapper.clear_cache = lambda: cache.clear()
    wrapper.get_cache_size = lambda: len(cache)
    
    return wrapper


def logging_decorator(func: Callable) -> Callable:
    """
    Декоратор для логирования вызовов функций
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"📝 Вызов функции '{func.__name__}' с аргументами:")
        print(f"   args: {args}")
        print(f"   kwargs: {kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"📝 Функция '{func.__name__}' вернула: {result}")
        return result
    return wrapper

