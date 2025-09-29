import time
import functools
from typing import Callable, Any

def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"️ Время выполнения {func.__name__}: {end_time - start_time:.4f} сек")
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
        print(f" {func.__name__} с параметрами: a={args[0]}, b={args[1]}, step={args[2]}")
        result = func(*args, **kwargs)
        print(f" {func.__name__} {len(result[0])}")
        return result
    return wrapper


import math
from decorators import validate_input, log_call, timer


@validate_input
@log_call
@timer
def linear_function(a: float, b: float, step: float) -> tuple:
  """Линейная функция: y = x"""
  x_values = []
  y_values = []

  x = a
  while x <= b:
    x_values.append(x)
    y_values.append(x)
    x += step

  return x_values, y_values


@validate_input
@log_call
@timer
def quadratic_function(a: float, b: float, step: float) -> tuple:
  """Квадратичная функция: y = x²"""
  x_values = []
  y_values = []

  x = a
  while x <= b:
    x_values.append(x)
    y_values.append(x ** 2)
    x += step

  return x_values, y_values


@validate_input
@log_call
@timer
def sin_function(a: float, b: float, step: float) -> tuple:
  """Синусоида: y = sin(x)"""
  x_values = []
  y_values = []

  x = a
  while x <= b:
    x_values.append(x)
    y_values.append(math.sin(x))
    x += step

  return x_values, y_values


@validate_input
@log_call
@timer

  x_values = []
  y_values = []

  x = a
  while x <= b:
    x_values.append(x)
    y_values.append(math.exp(x))
    x += step

  return x_values, y_values


@validate_input
@log_call
@timer
def logarithmic_function(a: float, b: float, step: float) -> tuple:
  """Логарифмическая функция: y = ln(x + 1)"""
  x_values = []
  y_values = []

  x = a
  while x <= b:
    x_values.append(x)
    # Добавляем 1 чтобы избежать ln(0)
    y_values.append(math.log(x + 1) if x + 1 > 0 else float('-inf'))
    x += step

  return x_values, y_values


@validate_input
@log_call
@timer
def trigonometric_function(a: float, b: float, step: float) -> tuple:
  """Тригонометрическая функция: y = sin(x) + cos(x)"""
  x_values = []
  y_values = []

  x = a
  while x <= b:
    x_values.append(x)
    y_values.append(math.sin(x) + math.cos(x))
    x += step

  return x_values, y_values

  '1': ('Линейная: y = x', linear_function),
  '2': ('Квадратичная: y = x²', quadratic_function),
  '3': ('Синусоида: y = sin(x)', sin_function),
  '4': ('Экспонента: y = e^x', exponential_function),
  '5': ('Логарифм: y = ln(x+1)', logarithmic_function),
  '6': ('Тригонометрическая: y = sin(x) + cos(x)', trigonometric_function)

  import matplotlib.pyplot as plt
  from typing import List

  def plot_function(x_values: List[float], y_values: List[float], function_name: str):
    """
    Построение графика функции по векторам X и Y

    Args:
        x_values: Список значений X
        y_values: Список значений Y
        function_name: Название функции для заголовка
    """
    plt.figure(figsize=(12, 6))
    plt.plot(x_values, y_values, 'b-', linewidth=2, label=function_name)
    plt.plot(x_values, y_values, 'ro', markersize=3, alpha=0.6)

    # Настройка графика
    plt.title(f'График функции: {function_name}', fontsize=14, fontweight='bold')
    plt.xlabel('X', fontsize=12)
    plt.ylabel('Y', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()

    # Добавляем линии осей
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)

    plt.tight_layout()
    plt.show()

  def print_xy_table(x_values: List[float], y_values: List[float], precision: int = 3):
    """
    Вывод таблицы значений X и Y в две колонки

    Args:
        x_values: Список значений X
        y_values: Список значений Y
        precision: Точность округления чисел
    """
    print(f"\n{'=' * 60}")
    print(f"{'ТАБЛИЦА ЗНАЧЕНИЙ':^60}")
    print(f"{'=' * 60}")
    print(f"{'X':^20} | {'Y':^20}")
    print(f"{'-' * 20}-+-{'-' * 20}")

    for i, (x, y) in enumerate(zip(x_values, y_values)):
      x_str = f"{x:.{precision}f}"
      y_str = f"{y:.{precision}f}"
      print(f"{x_str:>20} | {y_str:>20}")

      # Ограничиваем вывод для больших таблиц
      if i >= 50 and i < len(x_values) - 5:
        print(f"{'...':^20} | {'...':^20}")
        # Показываем последние 5 значений
        for j in range(len(x_values) - 5, len(x_values)):
          x_str = f"{x_values[j]:.{precision}f}"
          y_str = f"{y_values[j]:.{precision}f}"
          print(f"{x_str:>20} | {y_str:>20}")
        break

    print(f"{'=' * 60}")
    print(f"Всего точек: {len(x_values)}")
    print(f"Диапазон X: от {x_values[0]:.{precision}f} до {x_values[-1]:.{precision}f}")
    print(f"Диапазон Y: от {min(y_values):.{precision}f} до {max(y_values):.{precision}f}")

    from calculations import FUNCTIONS
    from visualization import plot_function, print_xy_table
    from decorators import timer

    def display_menu():
      """Отображение меню доступных функций"""
      print("\n" + "=" * 70)
      print(" ПРОГРАММА ДЛЯ ПОСТРОЕНИЯ ГРАФИКОВ ФУНКЦИЙ")
      print("=" * 70)
      print("Доступные функции:")
      for key, (name, _) in FUNCTIONS.items():
        print(f"  {key}. {name}")
      print("=" * 70)

    @timer
    def main():
      """Основная функция программы"""
      try:
        display_menu()

        # Выбор функции
        while True:
          choice = input("\nВыберите функцию (1-6) или 'q' для выхода: ").strip()
          if choice.lower() == 'q':
            print(" До свидания!")
            return
          if choice in FUNCTIONS:
            break
          print(" Неверный выбор! Попробуйте снова.")

        function_name, selected_function = FUNCTIONS[choice]

        # Ввод параметров
        print(f"\n Выбрана функция: {function_name}")
        print("Введите параметры диапазона:")

        a = float(input("Начало диапазона (a): "))
        b = float(input("Конец диапазона (b): "))
        step = float(input("Шаг: "))

        print(f"\n Расчет функции {function_name}...")
        print(f" Параметры: a={a}, b={b}, step={step}")

        # Расчет значений
        x_values, y_values = selected_function(a, b, step)

        # Вывод результатов
        print("\n" + "=" * 70)
        print(" РЕЗУЛЬТАТЫ РАСЧЕТА")
        print("=" * 70)

        # Вывод таблицы
        precision = int(input("Введите точность округления (количество знаков после запятой): ") or "3")
        print_xy_table(x_values, y_values, precision)

        # Построение графика
        print(f"\n Построение графика функции...")
        plot_function(x_values, y_values, function_name)

        # Предложение продолжить
        continue_choice = input("\nХотите построить еще один график? (y/n): ").strip().lower()
        if continue_choice == 'y':
          main()
        else:
          print(" До свидания!")

      except ValueError as e:
        if "could not convert string to float" in str(e):
          print(" Ошибка: Введите корректные числовые значения!")
        else:
          print(f" Ошибка ввода: {e}")
      except KeyboardInterrupt:
        print("\n\n Программа прервана пользователем!")
      except Exception as e:
        print(f" Неожиданная ошибка: {e}")

    if __name__ == "__main__":
      main()