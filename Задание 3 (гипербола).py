import matplotlib.pyplot as plt
import numpy as np

x = []
x2 = []
y = []
y2 = []

for i in range(1000):
    a = 400
    b = 200
    x.append(-i)
    x2.append(i)
    y.append(np.sqrt(b ** 2 + (b ** 2 * (i ** 2 / a ** 2))))
    y2.append(-np.sqrt(b ** 2 + (b ** 2 * (i ** 2 / a ** 2))))

plt.plot(x, y)
plt.plot(x, y2)
plt.plot(x2, y2)
plt.plot(x2, y)
plt.axis('scaled')
plt.show()