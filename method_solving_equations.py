"""
Вариант 1
16 мая лаба
Метод биссекций
"""

import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 2
xx = 10 ** (-7)  # критерий останова


# Заданая функция
def f(x):
    return np.cos(x) * np.log10(x**4) - (x * np.cos(x)) 


# Метод Бисекций
def bisection_method(start=a, end=b, tol=xx):

    if f(start) * f(end) >= 0:
        print("ошибка")
        return None

    while (end - start) / 2 > tol:
        c = (start + end) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(start) < 0:
            end = c
        else:
            start = c

    return (start + end) / 2


bisection_method(a, b)

# Построение графика
x_plt = np.arange(a, b, 0.0001)
f_plt = [f(x) for x in x_plt]
fig, ax = plt.subplots()
ax.grid()
ax.plot(x_plt, f_plt)
plt.xlabel("Метод Бисекций")
plt.show()
