def sublistas(lista):
    suma = 0;
    for i in lista:
        suma += i
    suma = suma / 2
    subl_rec(suma, lista, [], 0, 0)

def subl_rec(suma, lista, sublista, i, j):
    if total_lista(sublista) == suma:
        print("Solucion", sublista)
    else:
        if total_lista(sublista) < suma:
            for k in range(i, len(lista)):
                # sublista[j] = lista[i]
                sublista.append(lista[k])
                print(i, "   ", sublista)
                if total_lista(sublista) > suma:
                    print("Poda")
                    sublista.pop()
                else:
                    subl_rec(suma, lista, sublista, k + 1, j + 1)
        sublista.pop()


def total_lista(l):
    suma = 0
    for i in l:
        suma += i
    return suma


sublistas([1,2,3,4,5,9])