import numpy as n
import matplotlib.pyplot as mat
from scipy import optimize


def ff(param):
    return n.exp(param ** 2) - 2


def fdx(param):
    return 2 * param * n.exp(param * param)


def f2dx(param):
    return 2 * (2 * (param * param) + 1) * n.exp(param * param)


mat.xlabel("x")
mat.ylabel("y")

x = n.linspace(-1, 1, 50)
y = 2 * x * n.exp(x * x)

mat.plot(x, y, label="у = 2хex^2  [-1;1]")

mat.grid()
mat.legend()
mat.show()

eps = 0.0001
x1 = -1
x2 = x1 - fdx(x1) / f2dx(x1)
i = 0

while abs(x2 - x1) > eps and fdx(x2) != 0:
    x1 = x2
    x2 = x1 - fdx(x1) / f2dx(x1)
    i = i + 1

print("Mетод Ньютона-Рафсона: ")
print("Ітерації: " + str(i))
print("X " + str(x2))
print("Y " + str(ff(x2)))

eps = 0.001
i = 0
R = -1
L = 1
z = (R + L) / 2
fz = fdx(z)
while fdx(z) > eps:
    i = i + 1
    if fdx(z) < 0:
        L = z
    else:
        R = z
    z = (R + L) / 2

print("Mетод середної точки: ")
print("Ітерації: " + str(i))
print("X " + str(z))
print("Y " + str(ff(z)))

i = 0
R = 1
L = -1

while abs(L - R) >= eps:
    i = i + 1
    L = R - (R - L) * fdx(R) / (fdx(R) - fdx(L))
    R = L + (L - R) * fdx(L) / (fdx(L) - fdx(R))

print("Метод хорд")
print("Ітерації: " + str(i))
print("X " + str(R))
print("Y " + str(ff(R)))