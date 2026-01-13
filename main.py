"""
Основной модуль программы для работы с математическими функциями
"""

import sys
from typing import Tuple, List
import functions as funcs
import visualization as vis


def get_user_input() -> Tuple[float, float, float, int]:
    """
    Получение входных данных от пользователя
    """
    print("=" * 60)
    print("ПРОГРАММА ДЛЯ ИССЛЕДОВАНИЯ МАТЕМАТИЧЕСКИХ ФУНКЦИЙ")
    print("=" * 60)
    
    # Вывод списка доступных функций
    available_funcs = funcs.get_available_functions()
    print("\nДоступные функции:")
    for num, (desc, _) in available_funcs.items():
        print(f"  {num:2d}. {desc}")
    
    # Выбор функции
    while True:
        try:
            choice = int(input("\nВыберите номер функции (1-10): "))
            if choice in available_funcs:
                func_desc, selected_func = available_funcs[choice]
                print(f"✓ Выбрана функция: {func_desc}")
                break
            else:
                print("❌ Ошибка: введите число от 1 до 10")
        except ValueError:
            print("❌ Ошибка: введите целое число")
    
    # Ввод интервала
    print("\nВведите интервал исследования [a, b]:")
    while True:
        try:
            a = float(input("  a = "))
            b = float(input("  b = "))
            
            if a >= b:
                print("❌ Ошибка: a должно быть меньше b")
                continue
                
            # Проверка интервала для выбранной функции
            func_name = selected_func.__name__
            if 'tan' in func_name and (abs(a % (3.14159/2)) < 0.1 or abs(b % (3.14159/2)) < 0.1):
                print("⚠️  Внимание: тангенс не определен в точках π/2 + πk")
                response = input("  Продолжить? (да/нет): ").lower()
                if response not in ['да', 'yes', 'y', 'д']:
                    continue
            
            break
        except ValueError:
            print("❌ Ошибка: введите числа")
    
    # Ввод шага
    while True:
        try:
            step = float(input("\nВведите шаг (положительное число): "))
            if step <= 0:
                print("❌ Ошибка: шаг должен быть положительным")
                continue
            
            # Проверка на слишком мелкий/крупный шаг
            n_points = int((b - a) / step) + 1
            if n_points > 10000:
                print(f"⚠️  Будет создано {n_points} точек - это много!")
                response = input("  Продолжить? (да/нет): ").lower()
                if response not in ['да', 'yes', 'y', 'д']:
                    continue
            elif n_points < 10:
                print(f"⚠️  Будет создано всего {n_points} точек - график будет неточным")
                response = input("  Продолжить? (да/нет): ").lower()
                if response not in ['да', 'yes', 'y', 'д']:
                    continue
            
            break
        except ValueError:
            print("❌ Ошибка: введите число")
    
    return a, b, step, selected_func, func_desc


def calculate_vectors(a: float, b: float, step: float, func) -> Tuple[List[float], List[float]]:
    """
    Расчет векторов X и Y
    """
    print("\n" + "=" * 60)
    print("РАСЧЕТ ЗНАЧЕНИЙ ФУНКЦИИ...")
    print("=" * 60)
    
    x_values = []
    y_values = []
    errors = []
    
    # Генерация значений X
    current = a
    while current <= b + step/100:  # Добавляем небольшую погрешность для включения b
        x_values.append(current)
        current += step
    
    # Расчет значений Y
    for i, x in enumerate(x_values):
        try:
            y = func(x)
            y_values.append(y)
            print(f"  f({x:.4f}) = {y:.6f}")
        except Exception as e:
            errors.append((x, str(e)))
            y_values.append(float('nan'))  # Используем NaN для ошибок
            print(f"  f({x:.4f}) = ОШИБКА: {e}")
    
    # Сообщение об ошибках
    if errors:
        print(f"\n⚠️  Обнаружено {len(errors)} ошибок при вычислениях:")
        for x, error in errors[:5]:  # Показываем только первые 5 ошибок
            print(f"   x = {x:.4f}: {error}")
        if len(errors) > 5:
            print(f"   ... и еще {len(errors) - 5} ошибок")
    
    return x_values, y_values


def main():
    """
    Основная функция программы
    """
    try:
        # Получение данных от пользователя
        a, b, step, func, func_desc = get_user_input()
        
        # Расчет векторов
        x_values, y_values = calculate_vectors(a, b, step, func)
        
        # Проверка на наличие корректных данных
        valid_y = [y for y in y_values if not (isinstance(y, float) and (y != y or abs(y) == float('inf')))]
        if not valid_y:
            print("\n❌ Нет корректных значений функции для отображения")
            return
        
        # Вывод таблицы
        print("\n" + "=" * 60)
        print("ТАБЛИЧНОЕ ПРЕДСТАВЛЕНИЕ")
        print("=" * 60)
        vis.print_xy_table(x_values, y_values, precision=6, max_rows=20)
        
        # Построение графика
        print("\n" + "=" * 60)
        print("ПОСТРОЕНИЕ ГРАФИКА...")
        print("=" * 60)
        
        # Удаляем NaN значения для графика
        clean_x = []
        clean_y = []
        for x, y in zip(x_values, y_values):
            if isinstance(y, (int, float)) and not (y != y or abs(y) == float('inf')):
                clean_x.append(x)
                clean_y.append(y)
        
        if clean_x:
            vis.plot_function(clean_x, clean_y, a, b, 
                             title=f"График функции: {func_desc}")
        else:
            print("❌ Нет данных для построения графика")
        
        # Предложение продолжить
        print("\n" + "=" * 60)
        response = input("Хотите исследовать другую функцию? (да/нет): ").lower()
        if response in ['да', 'yes', 'y', 'д']:
            main()
        else:
            print("\nСпасибо за использование программы! До свидания!")
            print("=" * 60)
    
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем")
    except Exception as e:
        print(f"\n❌ Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

   
