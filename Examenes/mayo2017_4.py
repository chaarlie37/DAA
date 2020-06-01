# yo lo he hecho con la propia lista en vez de vector de booleanos porque no se leer xd

def subconjunto(l, s):
    solucion = [[]] # se usa esta lista como "puntero" ya que si se sustituye solucion por la solucion en la recursividad se pierde
    subc_suma(l, s, [None] * len(l), 0, 0, solucion)
    return solucion[0]


def subc_suma(lista, s, sublista, i, j, solucion):
    for k in range(i, len(lista)):
        sublista[j] = lista[k]
        if total_lista(sublista[:j + 1]) == s and (len(solucion[0]) > j + 1 or len(solucion[0]) == 0):
            solucion[0] = sublista[:j + 1]
        elif total_lista(sublista[:j + 1]) < s:
            subc_suma(lista, s, sublista, k + 1, j + 1, solucion)


def total_lista(l):
    suma = 0
    for i in l:
        suma += i
    return suma


print(subconjunto([1, 2, 3, 5, 6, 7, 9], 13))
