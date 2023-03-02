
import numpy as n
import matplotlib.pyplot as mat

def f(param):
    return n.exp(param*param) - 2

#інтервал перетину
A = -1
B = 1

#графік функції
x = n.linspace(A, B, 30)
y = n.exp(x*x) - 2
mat.plot(x, y, label="y = exp(x^2)-2")
mat.grid()
mat.legend()
mat.show()

eps = 0.001
i = 0

while abs(B - A) > eps:
    i = i + 1
    midl = (A + B) * 0.5

    if f(B) > f(A):
        B = midl
    else:
        A = midl

print("Мінімальний оптимум функцїї методом перетину = ", A, ",", f(A))
