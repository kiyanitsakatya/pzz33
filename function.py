"""
Модуль с математическими функциями
"""

import math
from decorators import validate_input_decorator, timer_decorator, cache_decorator, logging_decorator


# Базовые математические функции
@validate_input_decorator(-100, 100)
@cache_decorator
def linear_function(x: float) -> float:
    """
    Линейная функция: y = 2x + 3
    """
    return 2 * x + 3


@validate_input_decorator(-10, 10)
@cache_decorator
def quadratic_function(x: float) -> float:
    """
    Квадратичная функция: y = x² - 4
    """
    return x**2 - 4


@validate_input_decorator(-2*math.pi, 2*math.pi)
@cache_decorator
def sin_function(x: float) -> float:
    """
    Синусоида: y = sin(x)
    """
    return math.sin(x)


@validate_input_decorator(-2*math.pi, 2*math.pi)
@cache_decorator
def cos_function(x: float) -> float:
    """
    Косинусоида: y = cos(x)
    """
    return math.cos(x)


@validate_input_decorator(-math.pi/2 + 0.01, math.pi/2 - 0.01)
@cache_decorator
def tan_function(x: float) -> float:
    """
    Тангенс: y = tan(x)
    """
    return math.tan(x)


@validate_input_decorator(0.01, 100)
@cache_decorator
def log_function(x: float) -> float:
    """
    Натуральный логарифм: y = ln(x)
    """
    return math.log(x)


@validate_input_decorator(0, 100)
@cache_decorator
def sqrt_function(x: float) -> float:
    """
    Квадратный корень: y = √x
    """
    return math.sqrt(x)


@validate_input_decorator(-10, 10)
@cache_decorator
def exp_function(x: float) -> float:
    """
    Экспонента: y = e^x
    """
    return math.exp(x)


@validate_input_decorator(-10, 10)
@cache_decorator
def cubic_function(x: float) -> float:
    """
    Кубическая функция: y = x³ - 3x
    """
    return x**3 - 3*x


@validate_input_decorator(-5, 5)
@cache_decorator
def rational_function(x: float) -> float:
    """
    Рациональная функция: y = 1/(x² + 1)
    """
    return 1 / (x**2 + 1)


# Функция для получения списка доступных функций
def get_available_functions() -> dict:
    """
    Возвращает словарь доступных функций
    """
    return {
        1: ("Линейная (y = 2x + 3)", linear_function),
        2: ("Квадратичная (y = x² - 4)", quadratic_function),
        3: ("Синус (y = sin(x))", sin_function),
        4: ("Косинус (y = cos(x))", cos_function),
        5: ("Тангенс (y = tan(x))", tan_function),
        6: ("Логарифм (y = ln(x))", log_function),
        7: ("Квадратный корень (y = √x)", sqrt_function),
        8: ("Экспонента (y = e^x)", exp_function),
        9: ("Кубическая (y = x³ - 3x)", cubic_function),
        10: ("Рациональная (y = 1/(x² + 1))", rational_function)
    }
