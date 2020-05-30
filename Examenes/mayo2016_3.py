def sublistas(lista):
    suma = 0;
    for i in lista:
        suma += i
    suma = suma / 2
    subconjuntos(suma, lista, [None] * len(lista), [], 0, 0)


def otramitad(original, primeramitad):
    segundamitad = []
    for i in original:
        if i not in primeramitad:
            segundamitad.append(i)
    return segundamitad


def subconjuntos(suma, lista, sublista, sol_parcial, i, j):
    for k in range(i, len(lista)):
        sublista[j] = lista[k]
        # print(sublista[:j+1])
        if total_lista(sublista[:j + 1]) > suma:
            pass
        elif total_lista(sublista[:j + 1]) == suma and sublista[:j + 1] not in sol_parcial:
            print("SOLUCION: ", sublista[:j + 1], otramitad(lista, sublista[:j + 1]))
            sol_parcial.append(otramitad(lista, sublista[:j + 1]))
        else:
            subconjuntos(suma, lista, sublista, sol_parcial, k + 1, j + 1)


def total_lista(l):
    suma = 0
    for i in l:
        suma += i
    return suma


sublistas([1, 2, 3, 4, 5, 9])
