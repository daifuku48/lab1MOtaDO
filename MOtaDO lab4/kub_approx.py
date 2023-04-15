import numpy as np

x = np.arange(-1.5, 1.6, 0.1)

f = lambda x: np.exp(x ** 2) - 2
f1 = lambda x: 2 * x * np.exp(x ** 2)

a1 = lambda x1, x2: (f(x2) - f(x1)) / (x2 - x1)
a2 = lambda x1, x2: ((f(x2) - f(x1)) / ((x2 - x1) ** 2)) - (f1(x1) / (x2 - x1))
a3 = lambda x1, x2: ((f1(x2) - f1(x1)) / ((x2 - x1) ** 2)) - 2 * ((f(x2) - f(x1)) / ((x2 - x1) ** 3))
Z = lambda x1, x2: f1(x1) + f1(x2) - 3 * a1(x1, x2)
delt = lambda x1, x2: np.sqrt((Z(x1, x2)) ** 2 - f1(x1) * f1(x2))
sigm = lambda x1, x2: (Z(x1, x2) + delt(x1, x2) - f1(x1)) / (2 * delt(x1, x2) - f1(x1) + f1(x2))

eps = 0.0001
x1 = -1
h = 0.5

x2 = 1
i = 0

while True:
    i += 1

    if f1(x1) < 0:
        x2 = x1 + h
    else:
        x2 = x1 - h

    if f1(x1) * f1(x2) <= 0:
        break
    else:
        x1 = x2

a = 0
b = 0
if x1 <= x2:
    a = x1
    b = x2
else:
    a = x2
    b = x1

while True:
    i = i + 1
    xx = a + sigm(a, b)

    if (f1(xx)) < eps:
        break
    else:
        if f1(xx) * f1(x2) < 0:
            a = xx
        else:
            b = xx

print("Метод куб. аппроксимації")
print("Ітерації: " + str(i))
print("X " + str(xx))
print("Y " + str(f(xx)))