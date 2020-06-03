import math


# 0 derecha | 1 izquierda | 2 abajo | 3 arriba
def laberinto(n, tablero, visitados, camino_parcial, p, acumulados):
    meta = [n - 1, n - 1]
    visitados.append(p)
    if p == meta:
        if len(camino_parcial) > acumulados:
            camino_parcial[acumulados] = p
        else:
            camino_parcial.append(p)
        print("CAMINO OPTIMO:", camino_parcial)
        for k in camino_parcial[:acumulados + 1]:
            tablero[k[0]][k[1]] = "*"
    else:
        if meta not in camino_parcial:
            for i in range(3):
                nuevo_p = p.copy()
                if i == 0 and p[1] + 1 < n and tablero[p[0]][p[1] + 1] != "▆":      # derecha
                    nuevo_p[1] += 1
                elif i == 1 and p[1] - 1 > 0 and tablero[p[0]][p[1] - 1] != "▆":    # izquierda
                    nuevo_p[1] -= 1
                elif i == 2 and p[0] + 1 < n and tablero[p[0] + 1][p[1]] != "▆":    # abajo
                    nuevo_p[0] += 1
                elif i == 3 and p[0] - 1 > 0 and tablero[p[0] - 1][p[1]] != "▆":    # arriba
                    nuevo_p[0] -= 1

                if nuevo_p not in visitados and distancia_entre_puntos(nuevo_p, meta) < distancia_entre_puntos(p, meta):
                    if len(camino_parcial) > acumulados:
                        camino_parcial[acumulados] = p
                    else:
                        camino_parcial.append(p)
                    laberinto(n, tablero, visitados, camino_parcial, nuevo_p, acumulados + 1)


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


tablero = [[" ", " ", " ", " ", " ", " ", " ", "▆", "▆", "▆"],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", "▆", "▆", "▆", "▆", "▆", " ", " "],
           [" ", " ", " ", "▆", "▆", "▆", " ", " ", " ", " "],
           [" ", " ", " ", "▆", "▆", "▆", " ", " ", " ", " "],
           [" ", " ", " ", "▆", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", "▆", "▆", "▆", "▆", " ", " ", " "],
           [" ", " ", " ", "▆", " ", " ", "▆", " ", " ", " "],
           [" ", " ", " ", "▆", " ", " ", "▆", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", "▆", "▆", "▆", " "]]

laberinto(10, tablero, [], [], [0, 0], 0)
imprimir_matriz(tablero)
