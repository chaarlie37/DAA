def f(x, a):
    return x * x - a


def df(x):
    return 2 * x


def next_x(f, df, x_n, a):
    return x_n - (f(x_n, a) / df(x_n))


def newton(x, a):
    if f(x, a) <= 10 ** -6:
        return x
    else:
        return newton(next_x(f, df, x, a), a)


a = float(input())
print('%.4f' % newton(a, a))
