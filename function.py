import math
from decorate import validate_input, log_call, timer


@validate_input
@log_call
@timer
def linear_function(a: float, b: float, step: float) -> tuple:
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
def exponential_function(a: float, b: float, step: float) -> tuple:
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
    x_values = []
    y_values = []

    x = a
    while x <= b:
        x_values.append(x)
        y_values.append(math.log(x + 1) if x + 1 > 0 else float('-inf'))
        x += step

    return x_values, y_values


@validate_input
@log_call
@timer
def trigonometric_function(a: float, b: float, step: float) -> tuple:
    x_values = []
    y_values = []

    x = a
    while x <= b:
        x_values.append(x)
        y_values.append(math.sin(x) + math.cos(x))
        x += step


    return x_values, y_values
