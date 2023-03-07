import numpy as n
import matplotlib.pyplot as mat

mat.xlabel("x")
mat.ylabel("y")

A = -1
B = 1

x = n.linspace(A, B, 50)
y = n.exp(x*x) - 2

mat.plot(x, y, label="у = e^x^2 - 2 [-1;1]")

mat.grid()
mat.legend()
mat.show()


