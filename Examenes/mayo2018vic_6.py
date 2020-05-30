def cuadrados_magicos(n, sol_parcial, suma_filas, suma_columnas, suma_diagonalp, suma_diagonals):
    if len(sol_parcial) == 0:
        for i in range(n):
            sol_parcial.append([])
            for j in range(n):
                sol_parcial[i].append(None)
        imprimir_matriz(sol_parcial)
        lista_booleanos = [True] * n*n
        for i in range(n):
            for j in range(1, n*n + 1):
                if lista_booleanos[j-1]:
                    sol_parcial[0][i] = j
                    lista_booleanos[j-1] = False

                imprimir_matriz(sol_parcial)

'''
        for i in range(n):
            for j in range(n):
                suma_filas[i] += sol_parcial[i][j]
        for i in range(n):
            for j in range(n):
                suma_columnas[i] += sol_parcial[j][i]
        for i in range(n):
            suma_diagonalp += sol_parcial[i][i]
        for i in range(n):
            suma_diagonals += sol_parcial[n-1-i][i]

'''


def imprimir_matriz(m):
    for i in m:
        print(i)

cuadrados_magicos(3, [], [0] * 3, [0] * 3, 0, 0)