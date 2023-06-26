import numpy as n
import matplotlib.pyplot as mat


def f(x):
    return 3 * x ** 2 + 12 / x ** 3 - 5


def fdx(x):
    return 6 * x - 36 / x ** 4


def f2dx(x):
    return 6 + 144 / x ** 5


# Plotting the function
mat.xlabel("x")
mat.ylabel("y")

x = n.linspace(0.5, 2.5, 50)
y = 3 * x ** 2 + 12 / x ** 3 - 5

mat.plot(x, y, label="y = 3x^2 + (12 / x^3) - 5")

mat.grid()
mat.legend()
mat.show()

# Newton-Raphson method
x0 = 0.5
eps = 0.0001
i = 0

while True:
    x1 = x0 - fdx(x0) / f2dx(x0)
    i += 1
    if abs(x1 - x0) < eps:
        break
    x0 = x1

print("Newton-Raphson method:")
print("Iterations:", i)
print("X:", x1)
print("f(X):", f(x1))

# Bisection method
a = 0.5
b = 2.5
eps = 0.0001
i = 0

while abs(b - a) >= eps:
    c = (a + b) / 2
    i += 1
    if fdx(c) == 0:
        break
    elif fdx(a) * fdx(c) < 0:
        b = c
    else:
        a = c

print("Bisection method:")
print("Iterations:", i)
print("X:", c)
print("f(X):", f(c))

# Secant method
x0 = 0.5
x1 = 2.5
eps = 0.0001
i = 0

while True:
    x2 = x1 - fdx(x1) * (x1 - x0) / (fdx(x1) - fdx(x0))
    i += 1
    if abs(x2 - x1) < eps:
        break
    x0 = x1
    x1 = x2

print("Secant method:")
print("Iterations:", i)
print("X:", x2)
print("f(X):", f(x2))
