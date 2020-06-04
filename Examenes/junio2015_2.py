from random import randrange
import numpy as np

def multiplicar_matrices(a, b):
    n = len(a)
    m = len(a[0])
    if len(a) == 1 and len(b) == 1 and len(a[0]) == 1 and len(b[0]) == 1:
        return [[a[0][0] * b[0][0]]]
    elif len(a) > 0 and len(b) > 0:
        mitad_n = n // 2
        mitad_m = m // 2
        resultado = [] * n

        a11 = sub_matriz(a, 0, mitad_n, 0, mitad_m)
        a12 = sub_matriz(a, 0, mitad_n, mitad_m, m)
        a21 = sub_matriz(a, mitad_n, n, 0, mitad_m)
        a22 = sub_matriz(a, mitad_n, n, mitad_m, m)
        b11 = sub_matriz(b, 0, mitad_n, 0, mitad_m)
        b12 = sub_matriz(b, 0, mitad_n, mitad_m, m)
        b21 = sub_matriz(b, mitad_n, n, 0, mitad_m)
        b22 = sub_matriz(b, mitad_n, n, mitad_m, m)

        resultado11 = sumar_matrices(multiplicar_matrices(a11, b11),
                                     multiplicar_matrices(a12, b21))
        resultado12 = sumar_matrices(multiplicar_matrices(a11, b12),
                                     multiplicar_matrices(a12, b22))
        resultado21 = sumar_matrices(multiplicar_matrices(a21, b11),
                                     multiplicar_matrices(a22, b21))
        resultado22 = sumar_matrices(multiplicar_matrices(a21, b12),
                                     multiplicar_matrices(a22, b22))


        for k in range(len(resultado11)):
            resultado.append(resultado11[k] + resultado12[k])
        for k in range(len(resultado11), n):
            resultado.append(resultado21[k-len(resultado21)] + resultado22[k-len(resultado22)])

        return resultado


def sumar_matrices(a, b):
    if a is None:
        return b
    elif b is None:
        return a
    elif len(a) > 0:
        resultado = [] * len(a)
        for i in range(len(a)):
            aux = []
            for j in range(len(a[i])):
                aux.append(a[i][j] + b[i][j])
            resultado.append(aux)
        return resultado


def imprimir_matriz(m):
    for i in m:
        print(i)


def sub_matriz(a, n1, n2, m1, m2):
    resultado = []
    for i in range(n1, n2):
        aux = []
        for j in range(m1, m2):
            aux.append(a[i][j])
        resultado.append(aux)
    return resultado


matriz = []
matriz2 = []
for i in range(randrange(4, 5)):
    matriz.append([])
    matriz2.append([])
    for j in range(randrange(4, 5)):
        matriz[i].append(randrange(1, 10))
        matriz2[i].append(randrange(1, 10))

imprimir_matriz(matriz)
print()
imprimir_matriz(matriz2)
print()
imprimir_matriz(multiplicar_matrices(matriz, matriz2))

