import numpy as n
import matplotlib.pyplot as mat
import scipy.optimize as sc

# підписуємо осі
mat.xlabel("X1")
mat.ylabel("X2")

# описуємо функції
x2 = n.linspace(0, 10, 10)
x11 = (21 - x2) / 3
x12 = (30 - 3 * x2) / 2
x13 = 8 + x2 * 0
F6 = (28 - 2 * x2) / 3
x0 = n.linspace(0, 13, 100)
x01 = n.linspace(0, 0, 100)

# показуємо функції на графіку
mat.plot(x11, x2, label="3*X1 + X2 >=21")
mat.plot(x12, x2, label="2*X1 + 3*X2 >=30")
mat.plot(x13, x2, label="2*X1 <=16")
mat.plot(x0, x01, label="x1>=0")
mat.plot(x01, x0, label="x2>=0")
mat.plot(F6, x2, "g--", label="F")

# обозначаэмо графік сіткою
mat.grid()

# автоматично малює кольори ліній, якщо не вказувати елемент, розподілить кольори автоматично
mat.legend()

# виведення графіку
mat.show()

# об'являємо елементи у виді массивів, щоб знайти максимум
# функція idprog потрібна для пошуку мінімуму, тому значення вектору F вказуємо з протилежними знакам
f_max = [-3, -2]
a_max = [[3, 1], [2, 3], [2, 0], [0, -1], [-1, 0]]
b_max = [21, 30, 16, 0, 0]

# виклик функції для знаходження максимуму
answer = sc.linprog(f_max, a_max, b_max)

# виведення результату функції
print(answer)
