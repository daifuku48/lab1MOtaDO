import numpy as n
import matplotlib.pyplot as mat


def f(param):
    return n.exp(param * param) - 2


# інтервал перетину
A = -1
B = 1

# графік функції
x = n.linspace(A, B, 30)
y = n.exp(x * x) - 2
mat.plot(x, y, label="y = exp(x^2)-2")
mat.grid()
mat.legend()
mat.show()

eps = 0.001

L = B - A
while L > eps:
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