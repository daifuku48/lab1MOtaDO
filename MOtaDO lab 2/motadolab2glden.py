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

gold = 1.618

A = -1
B = 1

i = 0
eps = 0.001
while abs(B - A) > eps:
    i = i + 1
    x1 = B - (B - A) / gold
    x2 = A + (B - A) / gold
    if f(x1) >= f(x2):
        A = x1
    else:
        B = x2

midl = (A + B) * 0.5

print("Мінімальний оптимум методом золотого перетину:", midl, f(midl))
print(i)