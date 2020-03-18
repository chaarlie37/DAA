def f(x, a):
    return x * x - a


def df(x):
    return 2 * x


def next_x(f, df, x_n, a):
    return x_n - (f(x_n, a) / df(x_n))


def newton_rec(x, a):
    if f(x, a) <= 10**-6:
        return x
    else:
        return newton_rec(next_x(f, df, x, a), a)


def newton(a):
    return newton_rec(a, a)


a = float(input())

res = newton(a)


print("{0:.4f}".format(res))