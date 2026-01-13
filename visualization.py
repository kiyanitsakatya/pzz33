import matplotlib.pyplot as plt
from typing import List, Tuple, Optional
import numpy as np


def plot_function(x_values: List[float], y_values: List[float],
                  a: float, b: float,
                  title: str = "График функции",
                  xlabel: str = "X",
                  ylabel: str = "Y") -> None:
    """
    Построение графика функции по векторам X, Y
    
    Args:
        x_values: Список значений X
        y_values: Список значений Y
        a: Начало интервала
        b: Конец интервала
        title: Заголовок графика
        xlabel: Подпись оси X
        ylabel: Подпись оси Y
    """
    
    if len(x_values) != len(y_values):
        raise ValueError(f"Длины массивов не совпадают: X={len(x_values)}, Y={len(y_values)}")
    
    if len(x_values) == 0:
        print("Нет данных для построения графика")
        return
    
    plt.figure(figsize=(12, 7))
    
    # Основной график
    plt.plot(x_values, y_values, 'b-', linewidth=2.5, label='f(x)', alpha=0.8)
    plt.plot(x_values, y_values, 'ro', markersize=4, alpha=0.6, label='точки')
    
    # Настройки графика
    plt.title(f"{title}\nИнтервал: [{a:.2f}, {b:.2f}]", 
              fontsize=14, fontweight='bold', pad=15)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    
    # Установка границ
    plt.xlim(a - (b - a) * 0.05, b + (b - a) * 0.05)
    
    # Сетка
    plt.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    
    # Оси координат
    plt.axhline(y=0, color='black', linewidth=0.8, alpha=0.7)
    plt.axvline(x=0, color='black', linewidth=0.8, alpha=0.7)
    
    # Заполнение области под графиком
    plt.fill_between(x_values, y_values, alpha=0.2, color='blue')
    
    # Легенда
    plt.legend(loc='best', fontsize=10, framealpha=0.9)
    
    # Аннотация с информацией
    info_text = f"Количество точек: {len(x_values)}\n"
    info_text += f"min(y) = {min(y_values):.4f}\n"
    info_text += f"max(y) = {max(y_values):.4f}"
    plt.text(0.02, 0.98, info_text, transform=plt.gca().transAxes,
             fontsize=9, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    plt.show()


def print_xy_table(x_values: List[float], y_values: List[float],
                   precision: int = 4,
                   max_rows: int = 15) -> None:
    """
    Вывод таблицы значений X, Y в две колонки
    
    Args:
        x_values: Список значений X
        y_values: Список значений Y
        precision: Количество знаков после запятой
        max_rows: Максимальное количество строк для вывода
    """
    
    if len(x_values) != len(y_values):
        raise ValueError(f"Длины массивов не совпадают: X={len(x_values)}, Y={len(y_values)}")
    
    if len(x_values) == 0:
        print("Таблица пуста")
        return
    
    # Форматирование чисел
    def format_number(num: float) -> str:
        if abs(num) < 1e-10:
            num = 0.0
        
        # Для очень больших/маленьких чисел используем научную нотацию
        if abs(num) > 1e6 or (0 < abs(num) < 1e-6):
            return f"{num:.{precision}e}"
        else:
            return f"{num:.{precision}f}"
    
    # Определяем ширину колонок
    x_str_list = [format_number(x) for x in x_values]
    y_str_list = [format_number(y) for y in y_values]
    
    col_width = max(
        max(len(s) for s in x_str_list),
        max(len(s) for s in y_str_list),
        len("X"), len("Y")
    ) + 4
    
    total_width = col_width * 2 + 5
    
    # Вывод заголовка
    print("\n" + "=" * total_width)
    print(f"{'ТАБЛИЦА ЗНАЧЕНИЙ':^{total_width}}")
    print("=" * total_width)
    print(f"{'X':^{col_width}} | {'Y':^{col_width}}")
    print("-" * col_width + "-+-" + "-" * col_width)
    
    # Определяем, какие строки выводить
    n = len(x_values)
    if n <= max_rows:
        indices = list(range(n))
    else:
        # Выводим начало, середину и конец
        start_count = max_rows // 3
        end_count = max_rows // 3
        middle_count = max_rows - start_count - end_count
        
        indices = (list(range(start_count)) + 
                  [n // 2 + i - middle_count // 2 for i in range(middle_count)] +
                  list(range(n - end_count, n)))
    
    # Вывод строк
    prev_index = -1
    for i in indices:
        if prev_index != -1 and i > prev_index + 1:
            # Пропущенные строки
            ellipsis_x = "···"
            ellipsis_y = "···"
            print(f"{ellipsis_x:^{col_width}} | {ellipsis_y:^{col_width}}")
        
        x_str = format_number(x_values[i])
        y_str = format_number(y_values[i])
        print(f"{x_str:>{col_width}} | {y_str:>{col_width}}")
        prev_index = i
    
    print("=" * total_width)
    
    # Статистика
    print(f"\n📊 СТАТИСТИКА:")
    print(f"   Всего точек: {n}")
    print(f"   X ∈ [{format_number(min(x_values))}, {format_number(max(x_values))}]")
    print(f"   Y ∈ [{format_number(min(y_values))}, {format_number(max(y_values))}]")
    
    if n > 1:
        step = x_values[1] - x_values[0]
        print(f"   Шаг по X: {format_number(step)}")
 
