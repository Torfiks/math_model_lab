import random
import math
from sympy import symbols, sin, cos, tan, exp, log, symbols, lambdify

def random_function(complexity = 7):
    x = symbols('x')

    functions = [sin, cos, tan, log, exp]
    operators = ['+', '-', '*', '/', '**']

    function_args = [x]

    if complexity <= 0:
        return x + random.choice(operators) + random.randint(1, 10)

    expr = random.choice(function_args)  # x
    new_expr = 0

    for _ in range(complexity - 1):

        if random.random() < 0.5:
            op = random.choice(operators)
            func = random.choice(functions)
            if op in ['+', '-']:
                num = random.randint(4, 10)
                new_expr = op.join([str(expr), str(num), str(func(x)).replace("x", "")])
            elif op == '*':
                num = random.choice([2, 6, 5, 7])
                new_expr = op.join([str(expr), str(num), str(func(x)).replace("x", "")])
            elif op == '/':
                num = random.choice([8, 3, 5, 7])
                new_expr = op.join([str(expr), str(num)])
            elif op == '**':
                num = random.choice([3, 4, 6, 5])
                new_expr = op.join([str(expr), str(num)])

        else:
            func = random.choice(functions)
            try:
                if func in [sin, cos, log]:
                    new_expr = func(expr)
                elif func == log:
                    new_expr = func(expr)
                elif func == exp:
                    new_expr = func(expr, random.randint(1, 4))
            except TypeError:
                return " "

        expr = new_expr
    return expr

def bisection_method(func, a, b, tol=1e-6):
    fa = eval(func.replace('x', str(a)))
    fb = eval(func.replace('x', str(b)))
    if fa * fb >= 0:
        return None
    while abs(a - b) > tol:
        c = (a + b) / 2
        fc = eval(func.replace('x', str(c)))
        if fc == 0:
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return (a + b) / 2

def newton_method(func, x0, tol=1e-6):
    def derivative(f, x, h=1e-6):
        return (f(x + h) - f(x - h)) / (2 * h)

    f = lambda x: eval(func.replace('x', str(x)))
    df = lambda x: derivative(f, x)
    x = x0
    while abs(f(x)) > tol:
        x -= f(x) / df(x)
    return x

def simple_iteration_method(func, x0, tol=1e-6):
    f = lambda x: eval(func.replace('x', str(x)))
    x = x0
    while abs(f(x) - x) > tol:
        x = f(x)
    return x

def chord_method(func, a, b, tol=1e-6):
    while abs(a - b) > tol:
        fa = eval(func.replace('x', str(a)))
        fb = eval(func.replace('x', str(b)))
        c = a - fa * (b - a) / (fb - fa)
        fc = eval(func.replace('x', str(c)))
        if fc == 0:
            return c
        if fa * fc < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Пример использования

func = random_function()
print(f'Случайная функция: {func}')

a, b = -10, 10
root_bisection = bisection_method(func, a, b)
root_newton = newton_method(func, a)
root_simple_iteration = simple_iteration_method(func, a)
root_chord = chord_method(func, a, b)

print(f'Корень методом Биссекции: {root_bisection}')
print(f'Корень методом Ньютона: {root_newton}')
print(f'Корень методом простых итераций: {root_simple_iteration}')
print(f'Корень методом Хорд: {root_chord}')