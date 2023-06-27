import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import time

def f(x):
    return 3 * x ** 2 + 12 / x ** 3 - 5



def powell_f():
    eps = 1e-6
    w1 = 0.5
    _w = 1
    # Step 1
    w2 = w1 + _w
    i = 0
    # Step 2 and 3
    if f(w1) > f(w2):
        w3 = w1 + 2 * _w
    else:
        w3 = w1 - _w

    while True:
        # Step 4
        f1, f2, f3 = map(f, [w1, w2, w3])
        Fmin, Wmin = min((f1, w1), (f2, w2), (f3, w3), key=lambda x_: x_[0])
        i = i + 1
        # Step 5
        a1 = (f2 - f1) / (w2 - w1)

        a2 = 1.0 / (w3 - w2) * (((f3 - f1) / (w3 - w1)) - a1)

        W = ((w2 + w1) / 2) - (a1 / (2 * a2)) if a2 != 0 else (w2 + w1) / 2

        # Step 6
        if abs((Fmin - f(W)) / f(W)) < eps and abs((Wmin - W) / W) < eps:
            print("Iterations = ", i)
            return W
        # Step 7
        w1, w2, w3 = sorted([w1, w2, W])


if __name__ == '__main__':
    x = np.linspace(0.5, 3, 500)
    y = f(x)
    start_time = time.time()
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Function plot')
    # plt.show()
    bounds = [(0.5, 3)]
    res = scipy.optimize.minimize(f, x0=0.5, method='powell', bounds=bounds)
    print(res)

    x_opt = powell_f()#powell(f, x0=[1.0], bounds=bounds)
    print(f"The minimum value of the function is {x_opt}, {f(x_opt)}")
    print("--- %s seconds ---" % (time.time() - start_time))
