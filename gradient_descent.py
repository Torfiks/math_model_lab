"""
Градиентный спукс
Градиентный спуск — это численный метод нахождения локального минимума
или максимума функции с помощью движения вдоль градиента.
"""

import random
import numpy as np
import matplotlib.pyplot as plt


# Исходная функция
def f(x):
    return 5 * (np.sin(2 * np.pi * 10 * x) / 2 * np.pi * 10 * x) * np.cos(2 * np.pi)
# Производная функции f(x)


def df(x):
    return (2 * np.cos(x ** 2) - np.sin(x ** 2)) / (x ** 2)


# диапазон
x_start = 1
x_end = 4.1

step = 0.01  # шаг

N = 1000  # количество шагов


# График функции f(x) от 1 до 1.4 с шагом 0.01
# построение графика
def gradient_f():
    x_plt = np.arange(x_start, x_end, step)
    f_plt = [f(x) for x in x_plt]

    # параметры для отображения графика
    fig, ax = plt.subplots()
    ax.grid(True)
    ax.plot(x_plt, f_plt)  # f(x) на графике
    plt.xlabel("График функции f(x)")
    plt.show()  # демонстрация графика


gradient_f()


# График производной функции df(x) от 1 до 1.4 с шагом 0.01
# построение графика
def gradient_df():

    x_plt = np.arange(x_start, x_end, step)
    f_plt = [df(x) for x in x_plt]

    # параметры для отображения графика
    fig, ax = plt.subplots()
    ax.grid(True)
    ax.plot(x_plt, f_plt)  # df(x) на графике
    plt.xlabel("График функции df(x)")

    plt.show()  # демонстрация графика


gradient_df()


# Спуск производной
def gradient_descent():
    x = np.linspace(x_start, x_end, N)  # Задаем интервал значений x

    y = df(x)  # Вычисляем значения функции в заданных точках

    grad_y = np.gradient(y, x)  # Вычисляем градиент функции
    f_min = 0

    for i in grad_y:
        if i < f_min:
            f_min = i

    print(f_min)

    fig, ax = plt.subplots()
    ax.grid()
    ax.plot(x, grad_y)
    plt.xlabel("Спуск производной")
    plt.show()


gradient_descent()


# Спуск функции
def gradient_descent_2():
    y_min_global = 0
    x_min_global = 0

    for _ in range(100):
        x = random.uniform(x_start, x_end)

        for i in range(1000):
            learning_rate = 1 / min(i + 10, 100)
            x = x - learning_rate * np.sign(df(x))
            if x < x_start - (x_start / 10) or x > x_end - (x_end / 10):
                break
            else:
                y_min_local = f(x)

            if y_min_local < y_min_global:
                y_min_global = y_min_local
                x_min_global = x

    print(f'global minimum is: {y_min_global}')
    print(f'local minimum is: {x_min_global}')


gradient_descent_2()
