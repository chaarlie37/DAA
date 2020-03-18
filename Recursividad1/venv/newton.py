def f(x, a):
    return x * x - a


def df(x):
    return 2 * x


def next_x(f, df, x_n, a):
    return x_n - (f(x_n, a) / df(x_n))


def newton_rec(x, a):
    if f(x, a) <= 0.0001:
        return x
    else:
        return newton_rec(next_x(f, df, x, a), a)


def newton(a):
    return newton_rec(a, a)


print(newton(4))
