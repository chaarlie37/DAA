def s(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 4 * s(n//2) - n//2
    else:
        return 4 * s(n//2) + n//2 + 1


print(s(6))