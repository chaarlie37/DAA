import sympy


def ej1(n):
    if n == 1:
        return 1
    else:
        return (2 * n - 1) + ej1(n - 1)


def ej2(n):
    if n < 10:
        return 1
    else:
        return 1 + ej2(n // 10)


def ej3(x, d):
    if len(d) == 1:
        return d[0]
    else:
        aux = d[0]
        d.pop(0)
        return aux + x * ej3(x, d)


def ej4_1(n):
    if n == 1:
        return ej4(n)
    else:
        return ej4(n) + ej4_1(n - 1)


def ej4(n):
    if n == 1 or n == 2:
        return 1
    elif n >= 3:
        return 1 + ej4_1(n - 2)


def ej6(n):
    # TODO
    return 0


def ej7(a):
    n = len(a)
    if n <= 1:
        return a
    else:
        return ej6(ej7(a[0:n - 1]), a[n - 1])


# variante torres hanoi
def reloj(n,o,d,a):
    if n>0:
        antireloj(n-1, o, a, d)
        # mover disco n desde Origen hasta Destino
        antireloj(n-1, a, d, o)

def antireloj(n, o, d, a):
    if n > 0:
        antireloj(n-1, o, d, a)
        # mover disco n desde O a A



print(ej4(7))
