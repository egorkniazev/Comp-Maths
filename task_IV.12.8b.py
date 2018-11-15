import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x * np.exp(-x**2)


def df(x):
    return np.exp(-x**2) * (1 - 2 * x**2)


def root_bin_search(func, a, b, eps):  # searches for zero in the given interval
    x0 = (a + b) / 2
    while (b - a) > (eps / 2):
        if func(x0) > x0:
            a = x0
        elif func(x0) < 0:
            b = x0
        else:
            break
        x0 = (a + b) / 2
    return x0


# Drawing the function graph
x = np.linspace(0, 10, 100)
y = f(x)
plt.plot(x, y)
plt.grid()
plt.show()

# Searching for max in [0.5, 1]
max_x = root_bin_search(df, 0.5, 1, 0.001)
max_y = f(max_x)


def f_moved(x):  # f moved down for (max_y / 2)
    return x * np.exp(-x ** 2) - max_y / 2


# Searching for zeros
x0 = []
for i in range(99):
    if f_moved(x[i]) * f_moved(x[i+1]) < 0:
        x0.append(root_bin_search(f_moved, x[i], x[i + 1], 0.0005))
print(x0[1] - x0[0])