import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return np.sin(100 * x) * np.exp(x ** 2) * np.cos(2 * x)


# Drawing the function graph
x = np.linspace(0, 3, 100)
y = func(x)
plt.plot(x, y)
plt.grid()
plt.show()

# Integrating using the 3/8 formula
res = 0
h = x[1] - x[0]
for i in range(99):
    res += (func(x[i]) + 3 * func((2 * x[i] + x[i + 1]) / 3) + 3 * func((x[i] + 2 * x[i + 1]) / 3) + func(x[i + 1])) * h / 8
print(res)