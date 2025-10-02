import decorate as plt
from pandas import pd


def plot_function(x_values: List[float], y_values: List[float], function_name: str):

    Args
        x_values
        y_values
        function_name

    plt.figure(figsize=(12, 6))
    plt.plot(x_values, y_values, 'b-', linewidth=2, label=function_name)
    plt.plot(x_values, y_values, 'ro', markersize=3, alpha=0.6)


    plt.title(f'' {function_name}', fontsize=14, fontweight='bold')
    plt.xlabel('X', fontsize=12)
    plt.ylabel('Y', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()


    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)

    plt.tight_layout()
    plt.show()


def print_xy_table(x_values: List[float], y_values: List[float], precision: int = 3):


    Args
        x_values
        y_values
        precision
    """
    print(f"\n{'=' * 60}")
    print(f"{:^60}")
    print(f"{'=' * 60}")
    print(f"{'X':^20} | {'Y':^20}")
    print(f"{'-' * 20}-+-{'-' * 20}")

    for i, (x, y) in enumerate(zip(x_values, y_values)):
        x_str = f"{x:.{precision}f}"
        y_str = f"{y:.{precision}f}"
        print(f"{x_str:>20} | {y_str:>20}")

        
        if i >= 50 and i < len(x_values) - 5:
            print(f"{'...':^20} | {'...':^20}")
            
            for j in range(len(x_values) - 5, len(x_values)):
                x_str = f"{x_values[j]:.{precision}f}"
                y_str = f"{y_values[j]:.{precision}f}"
                print(f"{x_str:>20} | {y_str:>20}")
            break
