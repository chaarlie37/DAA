import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

cedge = (80/255,113/255,118/255)
cface = (185/255,206/255,209/255)

def dibuja_cuadrado(ax, p, l):
    print("Cuadrado: P:", p, "Lado:", l);
    ax.add_patch(Rectangle((p[0] - l / 2, p[1] - l / 2),
                           l, l, facecolor=cface, edgecolor=cedge, linewidth=0.5))

def fractales(ax, p, s, n):
    if n > 0:
        dibuja_cuadrado(ax, p, 2 * s)
        fractales(ax, [p[0] - 2*s, p[1] + 2 *s], s/2, n-1)
        fractales(ax, [p[0] + 2*s, p[1] + 2 *s], s/2, n-1)
        fractales(ax, [p[0] - 2*s, p[1] - 2 *s], s/2, n-1)
        fractales(ax, [p[0] + 2*s, p[1] - 2 *s], s/2, n-1)


fig = plt.figure()
fig.patch.set_facecolor('white')
ax = plt.gca()
p = [0,0]
s = 100
n = 5
fractales(ax, p, s, n)
plt.axis('equal')
plt.axis('off')
plt.show()
