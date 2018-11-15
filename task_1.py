import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return np.exp(x) * np.sin(x) - 1


# Drawing the function graph
x = np.linspace(-10, 10, 100)
y = func(x)
plt.plot(x, y)
plt.grid()
plt.show()

# Counting the zeros
k = 0
if y[0] >= 0:
    flag = 1
else:
    flag = -1
for i in range (100):
    if y[i] > 0 and flag == -1:
        k += 1
        flag = 1
    if y[i] < 0 and flag == 1:
        k += 1
        flag = -1
print('Number of zeros = ', k)

# Binary search for the zero at [8, 10]
EPS = 0.000001
a = 8
b = 10
x0 = (a + b) / 2
while (b - a) > (EPS / 2):
    if func(x0) > 0:
        a = x0
    elif func(x0) < 0:
        b = x0
    else:
        break
    x0 = (a + b) / 2
print('x = ', x0)