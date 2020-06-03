import math
import time


# 0 derecha | 1 izquierda | 2 abajo | 3 arriba
def laberinto(n, tablero, visitados, camino_parcial, p, acumulados, mejor_sol):
    meta = [n - 1, n - 1]
    visitados.append(p)
    if p == meta:
        if len(camino_parcial) > acumulados:
            camino_parcial[acumulados] = p
        else:
            camino_parcial.append(p)
        if acumulados < mejor_sol[0]:
            print("mejor", mejor_sol)
            mejor_sol[0] = acumulados
            print("CAMINO OPTIMO:", camino_parcial)
            for k in camino_parcial:
                if tablero[k[0]][k[1]] == "*":
                    tablero[k[0]][k[1]] = " "
            for k in camino_parcial[:acumulados + 1]:
                tablero[k[0]][k[1]] = "*"
    else:
        #print("mejor", mejor_sol)
        #print("acumulados", acumulados)
        for k in tablero:
            for j in range(len(k)):
                if k[j] != "▆":
                    k[j] = " "
        for k in camino_parcial[:acumulados + 1]:
            tablero[k[0]][k[1]] = "*"
        if acumulados < mejor_sol[0]:
            nuevo_p = p.copy()
            for i in range(4):
                if i == 0 and p[1] + 1 < n and tablero[p[0]][p[1] + 1] != "▆":      # derecha
                    nuevo_p[1] += 1
                elif i == 1 and p[1] - 1 >= 0 and tablero[p[0]][p[1] - 1] != "▆":    # izquierda
                    nuevo_p[1] -= 1
                elif i == 2 and p[0] + 1 < n and tablero[p[0] + 1][p[1]] != "▆":    # abajo
                    nuevo_p[0] += 1
                elif i == 3 and p[0] - 1 >= 0 and tablero[p[0] - 1][p[1]] != "▆":    # arriba
                    nuevo_p[0] -= 1

                # if nuevo_p != p and (nuevo_p not in visitados or acumulados < len(visitados)) and distancia_entre_puntos(nuevo_p, meta) < distancia_entre_puntos(p, meta):
                if nuevo_p != p and (nuevo_p not in camino_parcial[:acumulados]) and distancia_entre_puntos(nuevo_p, meta) < distancia_entre_puntos(p, meta):
                    if len(camino_parcial) > acumulados:
                        camino_parcial[acumulados] = nuevo_p
                    else:
                        camino_parcial.append(nuevo_p)
                    imprimir_matriz(tablero)
                    print(camino_parcial[:acumulados])
                    # time.sleep(0.1)
                    laberinto(n, tablero, visitados, camino_parcial[:acumulados + 1], nuevo_p, acumulados + 1, mejor_sol)
                elif nuevo_p != p and (nuevo_p not in camino_parcial[:acumulados]):
                    if i == 3:
                        nuevo_p = p.copy()
            if nuevo_p == p:
                nuevo_p = p.copy()
                for i in range(4):
                    print("aaaaaaaaaaaaaaaaaaaaaaaaa")
                    if i == 0 and p[1] + 1 < n and tablero[p[0]][p[1] + 1] != "▆":      # derecha
                        nuevo_p[1] += 1
                    elif i == 1 and p[1] - 1 >= 0 and tablero[p[0]][p[1] - 1] != "▆":    # izquierda
                        nuevo_p[1] -= 1
                    elif i == 2 and p[0] + 1 < n and tablero[p[0] + 1][p[1]] != "▆":    # abajo
                        nuevo_p[0] += 1
                    elif i == 3 and p[0] - 1 >= 0 and tablero[p[0] - 1][p[1]] != "▆":    # arriba
                        nuevo_p[0] -= 1
                    print(camino_parcial[:acumulados])
                    print("nuevo_p", nuevo_p)
                    if nuevo_p != p and (nuevo_p not in camino_parcial[:acumulados]):
                        if len(camino_parcial) > acumulados:
                            camino_parcial[acumulados] = nuevo_p
                        else:
                            camino_parcial.append(nuevo_p)

                        imprimir_matriz(tablero)
                        # time.sleep(0.1)
                        laberinto(n, tablero, visitados, camino_parcial[:acumulados + 1], nuevo_p, acumulados + 1, mejor_sol)


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
           [" ", " ", " ", " ", " ", " ", " ", "▆", " ", " "],
           [" ", " ", " ", "▆", "▆", "▆", "▆", "▆", " ", " "],
           [" ", " ", " ", "▆", "▆", "▆", " ", " ", " ", " "],
           [" ", " ", " ", "▆", "▆", "▆", " ", " ", " ", " "],
           [" ", " ", " ", "▆", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", "▆", "▆", " ", "▆", " ", " ", " "],
           [" ", " ", " ", "▆", " ", " ", "▆", " ", " ", " "],
           [" ", " ", " ", "▆", " ", " ", "▆", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", "▆", "▆", "▆", " "]]

laberinto(10, tablero, [], [], [0, 0], 0, [60])
imprimir_matriz(tablero)