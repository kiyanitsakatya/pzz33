from function import FUNCTIONS
from visualization import plot_function, print_xy_table
from decorate import timer


def display_menu():
    print("\n" + "=" * 70)
    print(" ПРОГРАММА ДЛЯ ПОСТРОЕНИЯ ГРАФИКОВ ФУНКЦИЙ")
    print("=" * 70)
    print("Доступные функции:")
    for key, (name, _) in FUNCTIONS.items():
        print(f"  {key}. {name}")
    print("=" * 70)


@timer
def main():
    try:
        display_menu()

        while True:
            choice = input("\nВыберите функцию (1-6) или 'q' для выхода: ").strip()
            if choice.lower() == 'q':
                print(" До свидания!")
                return
            if choice in FUNCTIONS:
                break
            print("Попробуйте снова.")

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
            print("Пока!")

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