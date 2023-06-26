import numpy as n
import matplotlib.pyplot as mat
from scipy import optimize


def f(x):
    return 3 * x ** 2 + 12 / x ** 3 - 5


def a1(x1, x2):
    return (f(x2) - f(x1)) / (x2 - x1)


def a2(x1, x2, x3):
    return (1 / (x3 - x2)) * (((f(x3) - f(x1)) / (x3 - x1)) - a1(x1, x2))


mat.xlabel("x")
mat.ylabel("y")

x = n.linspace(0.5, 2.5, 50)
y = 3 * x ** 2 + 12 / x ** 3 - 5

mat.plot(x, y, label="y = 3x^2 + (12 / x^3) - 5")

mat.grid()
mat.legend()
mat.show()
bounds = (0.5, 2.5)

res = optimize.minimize_scalar(f, bounds=bounds, method='bounded')

print("Solution with minimize_scalar: ")
print(res)

eps = 0.00001
x1 = 0.5
h = 0.05
i = 0

x2 = x1 + h

if f(x1) > f(x2):
    x3 = x1 + 2 * h
else:
    x3 = x1 - h

if f(x1) > f(x2):
    xmin = x2
else:
    xmin = x1

if f(xmin) > f(x3):
    xmin = x3

xx = ((x2 - x1) / 2) - a1(x1, x2) / (2 * a2(x1, x2, x3))

if abs(xx - xmin) > eps:
    while abs(xx - xmin) >= eps:
        i += 1
        if f(xmin) > f(xx):
            x1 = xx
        else:
            x1 = xmin

        x2 = x1 + h
        if f(x1) > f(x2):
            x3 = x1 + 2 * h
        else:
            x3 = x1 - h

        if f(x1) > f(x2):
            xmin = x2
        else:
            xmin = x1

        if f(xmin) > f(x3):
            xmin = x3

        xx = ((x2 - x1) / 2) - a1(x1, x2) / (2 * a2(x1, x2, x3))

print('X =', xx * -1)
print('Y =', f(xx) * -1)
print('i =', i)
