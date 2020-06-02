from random import randrange


def menor_elemento(a):
    if len(a) > 0:
        m = len(a)
        n = len(a[0])
        if n == 1:
            aux = []
            for i in range(m):
                aux.append(a[i][0])
            return min(aux)
        elif m == 1 and n > 0:
            return min(a[0])
        else:
            mitad_n = n // 2
            mitad_m = m // 2
            a11, a12, a13, a14 = [], [], [], []
            for i in range(mitad_m):
                a11.append(a[i][0:mitad_n])
            for i in range(mitad_m):
                a12.append(a[i][mitad_n:])
            for i in range(mitad_m, m):
                a13.append(a[i][0:mitad_n])
            for i in range(mitad_m, m):
                a14.append(a[i][mitad_n:])
            return min(menor_elemento(a11), menor_elemento(a12), menor_elemento(a13), menor_elemento(a14))


def imprimir_matriz(m):
    for i in m:
        print(i)


a = []
m = randrange(1, 10)
n = randrange(1, 10)
for i in range(m):
    aux = []
    for j in range(n):
        aux.append(randrange(1, 100))
    a.append(aux)

imprimir_matriz(a)
print(menor_elemento(a))
