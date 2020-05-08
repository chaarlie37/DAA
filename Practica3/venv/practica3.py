def subcolecciones(c, m):
    subc = [None] * m
    i, j = 0, -1
    colecciones = sub_aux(c, subc, m, i, j, [])
    return len(colecciones)


def sub_aux(c, subc, m, i, j, colecciones):
    if i == m and coleccion_valida(subc):
        colecciones.append(subc[0:i])
    if i < m:
        for k in range(j + 1, len(c)):
            subc[i] = c[k]
            sub_aux(c, subc, m, i + 1, k, colecciones)
    return colecciones


def coleccion_valida(c):
    subc = c.copy()
    subc.sort()
    minimo = subc[0]
    valida = True
    i = 1
    while valida and i < len(subc):
        valida = subc[i] % minimo == 0
        i += 1
    return valida


n = int(input())
lista = input()
c = []
for i in range(n):
    n = int(lista.split(" ")[i])
    c.append(n)
m = int(input())

print(subcolecciones(c, m))
