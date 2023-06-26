import numpy as n
import matplotlib.pyplot as mat


def f(param):
    return 3 * param**2 + (12 / (param**3)) - 5


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

gold = 1.618


i = 0
eps = 0.0001
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
print("i =",i)
