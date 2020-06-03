import math


def laberinto(n, tablero, pasos_minimos, camino_parcial, camino_optimo, p, pasos_acumulados, mejor_sol):
    meta = [n - 1, n - 1]
    if p == meta:
        camino_parcial.append(p)
        if pasos_acumulados < pasos_minimos[p[0]][p[1]]:
            pasos_minimos[p[0]][p[1]] = pasos_acumulados
        if pasos_acumulados < mejor_sol[0]:
            mejor_sol[0] = pasos_acumulados
            camino_optimo.clear()
            for i in camino_parcial:
                camino_optimo.append(i)
    else:
        camino_parcial.append(p)
        if pasos_acumulados < mejor_sol[0] and pasos_acumulados < pasos_minimos[p[0]][p[1]]:
            pasos_minimos[p[0]][p[1]] = pasos_acumulados
            # 0 derecha | 1 izquierda | 2 abajo | 3 arriba
            for i in range(4):
                nuevo_p = p.copy()
                if i == 0 and p[1] + 1 < n and tablero[p[0]][p[1] + 1] != "▆":  # derecha
                    nuevo_p[1] += 1
                elif i == 1 and p[1] - 1 >= 0 and tablero[p[0]][p[1] - 1] != "▆":  # izquierda
                    nuevo_p[1] -= 1
                elif i == 2 and p[0] + 1 < n and tablero[p[0] + 1][p[1]] != "▆":  # abajo
                    nuevo_p[0] += 1
                elif i == 3 and p[0] - 1 >= 0 and tablero[p[0] - 1][p[1]] != "▆":  # arriba
                    nuevo_p[0] -= 1

                if nuevo_p != p and (nuevo_p not in camino_parcial) and (
                        distancia_entre_puntos(nuevo_p, meta) < distancia_entre_puntos(p, meta) or pasos_acumulados + 1 <=
                        pasos_minimos[nuevo_p[0]][nuevo_p[1]]):
                    laberinto(n, tablero, pasos_minimos, camino_parcial[:pasos_acumulados + 1], camino_optimo, nuevo_p,
                              pasos_acumulados + 1,
                              mejor_sol)

    if pasos_acumulados == 0 and len(camino_optimo) > 0:
        print("CAMINO OPTIMO:", camino_optimo)
        print("Pasos desde la salida hasta la meta:", mejor_sol[0])
        limpiar_tablero(tablero)
        for k in camino_optimo:
            tablero[k[0]][k[1]] = "*"
        imprimir_matriz(tablero)


def distancia_entre_puntos(p1, p2):
    return math.sqrt(pow(abs(p1[0] - p2[0]), 2) + pow(abs(p1[1] - p2[1]), 2))


def imprimir_matriz(m):
    for i in range(len(m) + 1):
        print("___", end="")
    print()
    for i in m:
        print("|", end=" ")
        for j in i:
            print(j, "", end=" ")
        print("|")
    for i in range(len(m) + 1):
        print("___", end="")
    print()


def limpiar_tablero(tablero):
    for k in tablero:
        for j in range(len(k)):
            if k[j] != "▆":
                k[j] = " "


tablero = [[" ", " ", " ", " ", " ", " ", " ", "▆", "▆", "▆"],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", "▆", "▆", "▆", "▆", "▆", "▆", " "],
           ["▆", " ", " ", "▆", " ", " ", " ", " ", "▆", " "],
           [" ", "▆", " ", "▆", " ", "▆", " ", " ", " ", "▆"],
           [" ", " ", " ", "▆", " ", " ", "▆", " ", " ", " "],
           ["▆", " ", " ", "▆", "▆", " ", "▆", " ", " ", " "],
           [" ", " ", " ", " ", "▆", " ", "▆", " ", " ", " "],
           [" ", "▆", " ", "▆", "▆", " ", "▆", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", "▆", "▆", "▆", " "]]

tablero2 = [[" ", " ", " ", " ", " ", " ", " ", "▆", "▆", "▆"],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", "▆", "▆", "▆", "▆", "▆", " ", " "],
           [" ", " ", " ", "▆", "▆", "▆", " ", " ", " ", " "],
           [" ", " ", " ", "▆", "▆", "▆", " ", " ", " ", " "],
           [" ", " ", " ", "▆", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", "▆", "▆", "▆", "▆", " ", " ", " "],
           [" ", " ", " ", "▆", " ", " ", "▆", " ", " ", " "],
           [" ", " ", " ", "▆", " ", " ", "▆", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", "▆", "▆", "▆", " "]]

# para otras matrices de otros tamaños n*n, sustituir 10 por n
m = []
for i in range(10):
    aux = []
    for j in range(10):
        aux.append(100)
    m.append(aux)

laberinto(10, tablero, m, [], [], [0, 0], 0, [10*10])
