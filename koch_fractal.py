import math
import numpy as np
import matplotlib.pyplot as plt


def koch(p, q, n):
    if n == 0:
        plt.plot([p[0, 0], q[0, 0]], [p[1, 0], q[1, 0]], 'k-')
    else:
        v = q - p
        R_60 = np.matrix([[1/2, -math.sqrt(3) / 2], [math.sqrt(3) / 2, 1 / 2]])
        a = p + v / 3
        x = a + (R_60 * v) / 3
        b = p + 2 * v / 3
        koch(p, a, n - 1)
        koch(a, x, n - 1)
        koch(x, b, n - 1)
        koch(b, q, n - 1)

def copo_koch(n):
    p = np.array([[0], [0]])
    q = np.array([[1], [0]])
    r = np.array([[0.5], [math.sqrt(3) / 2]])
    s = np.array([[0], [1]])
    t = np.array([[1], [1]])
    koch(p, r, n)
    koch(r, q, n)
    koch(q, p, n)


fig = plt.figure()
fig.patch.set_facecolor('white')
p = np.array([[0], [0]])
q = np.array([[1], [0]])
copo_koch(4)
plt.axis('equal')
plt.axis('off')
plt.show()
