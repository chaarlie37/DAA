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
        return resultado + suma_polinomios(p[1:len(p)], q[1:len(q)])


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


def multiplicar_xm(p, m):
    aux = p.copy()
    for i in range(m):
        aux = [0] + aux
    return aux


def multiplicar_polinomios(p, q):
    if p == [0] or q == [0]:
        return [0]
    if len(p) == 0:
        return q
    elif len(q) == 0:
        return p
    elif len(p) == 1:
        aux = q.copy()
        for i in range(0, len(q)):
            aux[i] = aux[i] * p[0]
        return aux
    elif len(q) == 1:
        aux = p.copy()
        for i in range(0, len(p)):
            aux[i] = aux[i] * q[0]
        return aux
    m = min(len(p) // 2, len(q) // 2)
    pa = p[m:len(p)]
    pb = p[0:m]
    qa = q[m:len(q)]
    qb = q[0:m]
    pa_qa_x2m = multiplicar_xm(multiplicar_polinomios(pa, qa), 2*m)
    corchetes = multiplicar_xm(resta_polinomios(resta_polinomios(multiplicar_polinomios(suma_polinomios(pa, pb), suma_polinomios(qa, qb)), multiplicar_polinomios(pa, qa)), multiplicar_polinomios(pb, qb)), m)
    pb_qb = multiplicar_polinomios(pb, qb)
    return suma_polinomios(suma_polinomios(pa_qa_x2m, corchetes), pb_qb)


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

polinomio = multiplicar_polinomios(lista1, lista2)
imprimir_polinomio(polinomio, len(polinomio)-1)

