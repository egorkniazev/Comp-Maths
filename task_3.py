import numpy as np
import matplotlib.pyplot as plt


def func1(x):
    return np.tan(x)


def func2(x):
    return np.sqrt(1 - x**2)


def func(x):
    return func2(x) - func1(x)


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
x = np.linspace(-1.1, 1.1, 50)
y1 = func1(x)
circle1 = plt.Circle((0, 0), 1, fill=False)
fig, ax = plt.subplots()
ax.add_artist(circle1)
plt.plot(x, y1)
plt.grid()
plt.show()

# Searching the root in [0.6, 0.7]
x1 = root_bin_search(0.6, 0.7, 0.000001)
y1 = func1(x1)

# Using symmetry, finding the second root
x2 = -x1
y2 = -y1

print('(x1, y1) = (%f, %f)\n(x2, y2) = (%f, %f)' % (x1, y1, x2, y2))