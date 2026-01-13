import math
from typing import Dict, Tuple, Callable
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


@validate_input_decorator(-math.pi, math.pi)
@cache_decorator
def sinc_function(x: float) -> float:
    """
    Функция sinc: y = sin(x)/x (с особенностью в x=0)
    """
    if abs(x) < 1e-10:
        return 1.0  # предел sin(x)/x при x→0 равен 1
    return math.sin(x) / x


@validate_input_decorator(-5, 5)
@cache_decorator
def gaussian_function(x: float) -> float:
    """
    Гауссова функция: y = exp(-x²/2)
    """
    return math.exp(-(x**2) / 2)


@validate_input_decorator(-5, 5)
@cache_decorator
def absolute_function(x: float) -> float:
    """
    Модуль: y = |x|
    """
    return abs(x)


@validate_input_decorator(-5, 5)
@cache_decorator
def step_function(x: float) -> float:
    """
    Ступенчатая функция: y = 0 если x<0, иначе 1
    """
    return 0.0 if x < 0 else 1.0


# Атрибут модуля - словарь всех доступных функций
get_available_functions: Dict[int, Tuple[str, Callable]] = {
    1: ("Линейная функция: y = 2x + 3", linear_function),
    2: ("Квадратичная функция: y = x² - 4", quadratic_function),
    3: ("Синусоида: y = sin(x)", sin_function),
    4: ("Косинусоида: y = cos(x)", cos_function),
    5: ("Тангенс: y = tan(x)", tan_function),
    6: ("Логарифм: y = ln(x)", log_function),
    7: ("Квадратный корень: y = √x", sqrt_function),
    8: ("Экспонента: y = e^x", exp_function),
    9: ("Кубическая функция: y = x³ - 3x", cubic_function),
    10: ("Рациональная функция: y = 1/(x² + 1)", rational_function),
    11: ("Функция sinc: y = sin(x)/x", sinc_function),
    12: ("Гауссова функция: y = exp(-x²/2)", gaussian_function),
    13: ("Функция модуля: y = |x|", absolute_function),
    14: ("Ступенчатая функция: y = 0 при x<0, 1 при x≥0", step_function)
}

# Дополнительные атрибуты модуля для удобства
__all__ = ['get_available_functions'] + [name for name in globals() if name.endswith('_function')]

# Информационные атрибуты
MODULE_NAME = "Математические функции"
VERSION = "1.0.0"
AUTHOR = "Система анализа функций"
DESCRIPTION = "Модуль содержит коллекцию математических функций для анализа и визуализации"

# Функция для получения информации о модуле
def get_module_info() -> Dict[str, str]:
    """
    Возвращает информацию о модуле
    """
    return {
        "module_name": MODULE_NAME,
        "version": VERSION,
        "author": AUTHOR,
        "description": DESCRIPTION,
        "total_functions": len(get_available_functions)
    }


# Функция для поиска функции по названию
def find_function_by_name(name: str) -> Tuple[int, str, Callable]:
    """
    Поиск функции по имени или части имени
    
    Args:
        name: Имя или часть имени функции
        
    Returns:
        Кортеж (номер, описание, функция)
    """
    name_lower = name.lower()
    for num, (desc, func) in get_available_functions.items():
        func_name = func.__name__.lower()
        desc_lower = desc.lower()
        
        if (name_lower in func_name or 
            name_lower in desc_lower or
            name_lower == str(num)):
            return num, desc, func
    
    raise ValueError(f"Функция '{name}' не найдена")


# Функция для получения функций по категориям
def get_functions_by_category() -> Dict[str, Dict[int, Tuple[str, Callable]]]:
    """
    Возвращает функции, сгруппированные по категориям
    """
    categories = {
        "Полиномы": {},
        "Тригонометрические": {},
        "Трансцендентные": {},
        "Специальные": {}
    }
    
    for num, (desc, func) in get_available_functions.items():
        func_name = func.__name__
        
        if any(poly in func_name for poly in ['linear', 'quadratic', 'cubic']):
            categories["Полиномы"][num] = (desc, func)
        elif any(trig in func_name for trig in ['sin', 'cos', 'tan']):
            categories["Тригонометрические"][num] = (desc, func)
        elif any(trans in func_name for trans in ['log', 'exp', 'sqrt']):
            categories["Трансцендентные"][num] = (desc, func)
        else:
            categories["Специальные"][num] = (desc, func)
    
    return categories


# Пример использования атрибута (можно использовать в основном коде):
if __name__ == "__main__":
    # Пример 1: Получение списка всех функций
    print("Доступные функции:")
    print("=" * 60)
    for num, (desc, func) in get_available_functions.items():
        print(f"{num:2d}. {desc}")
        print(f"    Имя функции: {func.__name__}")
        print(f"    Документация: {func.__doc__.strip() if func.__doc__ else 'Нет'}")
        print()
    
    # Пример 2: Получение информации о модуле
    print("\nИнформация о модуле:")
    print("=" * 60)
    info = get_module_info()
    for key, value in info.items():
        print(f"{key}: {value}")
    
    # Пример 3: Поиск функции
    print("\nПоиск функций:")
    print("=" * 60)
    try:
        num, desc, func = find_function_by_name("sin")
        print(f"Найдена: #{num} - {desc}")
        print(f"sin(π/2) = {func(math.pi/2):.4f}")
    except ValueError as e:
        print(e)
    
    # Пример 4: Функции по категориям
    print("\nФункции по категориям:")
    print("=" * 60)
    categories = get_functions_by_category()
    for category, funcs in categories.items():
        print(f"\n{category} ({len(funcs)} функций):")
        for num, (desc, _) in funcs.items():
            print(f"  {num:2d}. {desc}")
