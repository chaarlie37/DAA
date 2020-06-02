import math
import numpy as np
import matplotlib.pyplot as plt


def dibujar(p, q):
    plt.plot([p[0, 0], q[0, 0]], [p[1, 0], q[1, 0]], 'k-')


def koch(p, q, n):
    if n == 0:
        dibujar(p, q)
    else:
        v = q - p
        # R60 = np.matrix([[1/2, -math.sqrt(3) / 2], [math.sqrt(3) / 2, 1 / 2]])
        R60 = np.matrix(
            [[math.cos(math.pi / 3), - math.sin(math.pi / 3)], [math.sin(math.pi / 3), math.cos(math.pi / 3)]])
        a = p + v / 3
        x = a + (v * R60) / 3
        b = p + 2 * v / 3
        koch(p, a, n - 1)
        koch(a, x, n - 1)
        koch(x, b, n - 1)
        koch(b, q, n - 1)


fig = plt.figure()
fig.patch.set_facecolor('white')
p = np.array([[0], [0]])
q = np.array([[1], [0]])
koch(p, q, 1)
plt.axis('equal')
plt.axis('off')
plt.show()
