import random

def es_ordenada_matriz(a):
    m = len(a)
    if m == 0:
        n = 0
    else:
        n = len(a[0])
    if n == 1 and m == 1:
        return True
    elif n == 0 or m == 0:
        return True
    else:
        mitad_n = (n // 2)
        mitad_m = (m // 2)
        centrales_ordenados = True
        i = 0
        while mitad_n >= 0 and i < m and centrales_ordenados:
            centrales_ordenados = a[i][mitad_n-1] <= a[i][mitad_n]
            i += 1
        i = 0
        while mitad_m >= 0 and i < n and centrales_ordenados:
            centrales_ordenados = a[mitad_m-1][i] <= a[mitad_m][i]
            i += 1
        if centrales_ordenados:
            return es_ordenada_matriz(a[0:mitad_n][0:mitad_m]) and es_ordenada_matriz(
                a[mitad_n + 1:][mitad_m + 1:]) and es_ordenada_matriz(
                a[mitad_m + 1:][0: mitad_n]) and es_ordenada_matriz(a[mitad_m + 1:][mitad_n:])
        else:
            return False


def imprimir_matriz(m):
    for i in m:
        print(i)

matriz = []
for i in range(0, 4):
    matriz.append([])
    for j in range(0, 4):
        matriz[i].append(random.randrange(1, 30))

imprimir_matriz(matriz)
print(es_ordenada_matriz(matriz))