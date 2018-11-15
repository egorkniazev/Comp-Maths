import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return x * np.cos(x) - 0.56


def root_bin_search (a, b, eps):  # searches for zeros in the given interval
    x0 = (a + b) / 2
    while (b - a) > (eps / 2):
        if func(x0) > 0:
            a = x0
        elif func(x0) < 0:
            b = x0
        else:
            break
        x0 = (a + b) / 2
    return x0


# Drawing the function graph
x = np.linspace(-2, 2, 50)
y = func(x)
plt.plot(x, y)
plt.grid()
plt.show()

# Root localisation
for i in range(49):
    if func(x[i]) * func(x[i+1]) < 0:
        print('x = ', root_bin_search(x[i], x[i + 1], 0.000001))
