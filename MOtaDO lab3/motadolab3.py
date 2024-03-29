import numpy as n
import matplotlib.pyplot as mat
from scipy import optimize
import time

def f(param):
    return n.exp(param ** 2) - 2

def a1(x1, x2):
    return (f(x2) - f(x1)) / (x2 - x1)


def a2(x1, x2, x3):
    return (1 / (x3 - x2)) * (((f(x3) - f(x1)) / (x3 - x1)) - a1(x1, x2))

start_time = time.time()
eps = 0.001
x1 = -1
h = 1
i = 0

#крок 1
x2 = x1 + h

#крок 2 та 3
if f(x1) > f(x2):
    x3 = x1 + 2 * h
else:
    x3 = x1 - h

#крок 4
if f(x1) > f(x2):
    xmin = x2
else:
    xmin = x1

if f(xmin) > f(x3):
    xmin = x3

#крок 5
#для знаходження квадратичної аппроксимації використувуємо коефіцієнти полінома а1 та а2 за формулами у функціях
xx = ((x2 - x1) / 2) - a1(x1, x2) / 2 * a2(x1, x2, x3)

if abs(xx - xmin) > eps:
    while abs(xx - xmin) >= eps or abs(f(xx) - f(xmin)) > eps: #крок 6 виконуэться у циклі кожну ітерацію
        i = i + 1
        if f(xmin) > f(xx):
            x1 = xx
        else:
            x1 = xmin
        h = h / 2
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

        xx = ((x2 - x1) / 2) - a1(x1, x2) / 2 * a2(x1, x2, x3)


print("Realization")
print(f(xx), xx, "Number of iteration:", i)
print("--- %s seconds ---" % (time.time() - start_time))