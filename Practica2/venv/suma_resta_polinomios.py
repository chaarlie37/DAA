def imprimir_polinomio(lista, grado):
    if lista == [0] and grado == 0:
        print(" + 0")
    elif len(lista) > 0:
        n = len(lista) - 1
        if lista[n] < 0:
            if n == 0:
                print(" - ", -lista[n], sep="")
            else:
                print(" - ", -lista[n], "x^", n, end="", sep="")
        elif lista[n] > 0:
            if n == 0:
                print(" + ", lista[n], sep="")
            else:
                print(" + ", lista[n], "x^", n, end="", sep="")
        imprimir_polinomio(lista[0:n], grado)


def suma_polinomios(p, q):
    if len(p) == 0:
        return q
    elif len(q) == 0:
        return p
    else:
        resultado = []
        resultado.append(p[0] + q[0])
        resultado = resultado + suma_polinomios(p[1:len(p)], q[1:len(q)])
        return resultado


def resta_polinomios(p, q):
    if len(p) == 0:
        for i in range(len(q)):
            q[i] = -q[i]
        return q
    elif len(q) == 0:
        return p
    else:
        resultado = []
        resultado.append(p[0] - q[0])
        resultado = resultado + resta_polinomios(p[1:len(p)], q[1:len(q)])
        return resultado


grado1 = int(input())
nums1 = input()
lista1 = []
for i in range(grado1 + 1):
    n = int(nums1.split(" ")[i])
    lista1.append(n)

grado2 = int(input())
nums2 = input()
lista2 = []
for i in range(grado2 + 1):
    n = int(nums2.split(" ")[i])
    lista2.append(n)

grado = grado1
if grado2 > grado1:
    grado = grado2


imprimir_polinomio(suma_polinomios(lista1, lista2), grado)
imprimir_polinomio(resta_polinomios(lista1, lista2), grado)
