import numpy as n
import matplotlib.pyplot as mat
import time

def f(param):
    return 3 * param**2 + (12 / (param**3)) - 5


start_time = time.time()
# інтервал перетину
A = 0.5
B = 2.5

# графік функції
x = n.linspace(A, B, 30)
y = 3 * x**2 + (12 / (x**3)) - 5
mat.plot(x, y, label="y = 3x^2 + (12 / x^3) - 5")
mat.grid()
mat.legend()
mat.show()

eps = 0.001
i = 0
L = B - A
while L > eps:
    i = i + 1
    x1 = A + L / 4
    xm = (A + B) / 2
    x2 = B - L / 4

    if f(x1) > f(xm):
        if f(xm) < f(x2):
            A = x1
            B = x2
        else:
            A = xm
    else:
        B = xm
    L = B - A


print("Мінімальний оптимум функцїї методом перетину = ", A, ",", f(A))
print("i =", i)
print("--- %s seconds ---" % (time.time() - start_time))