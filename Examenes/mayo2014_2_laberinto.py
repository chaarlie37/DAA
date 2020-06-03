import math

# 0 derecha | 1 izquierda | 2 abajo | 3 arriba
def laberinto(n, tablero, visitados, camino_parcial, camino_final, p, acumulados):
    print("p:", p)
    print("parcial", camino_parcial)
    visitados.append(p)
    if p[0] == n - 1 and p[1] == n - 1:
        camino_parcial.append(p)
        print("SOLUCION:", camino_parcial)
        camino_final.append(1)
        for k in camino_parcial:
            tablero[k[0]][k[1]] = "*"
        return None
    else:
        if len(camino_final) > 0:
            return None
        for i in range(3, -1, -1):
            p_objetivo = [n-1, n-1]
            nuevo_p = p.copy()
            if i == 0 and p[1] + 1 < n and tablero[p[0]][p[1] + 1] != "▆":
                nuevo_p[1] += 1
                if nuevo_p not in visitados and distancia_entre_puntos(nuevo_p, p_objetivo) < distancia_entre_puntos(p, p_objetivo):
                    camino_parcial.append(p)
                    laberinto(n, tablero, visitados, camino_parcial, camino_final, nuevo_p, acumulados + 1)
            elif i == 1 and p[1] - 1 > 0 and tablero[p[0]][p[1] - 1] != "▆":
                nuevo_p[1] -= 1
                if nuevo_p not in visitados and distancia_entre_puntos(nuevo_p, p_objetivo) < distancia_entre_puntos(p, p_objetivo):
                    camino_parcial.append(p)
                    laberinto(n, tablero, visitados, camino_parcial, camino_final, nuevo_p, acumulados + 1)
            elif i == 2 and p[0] + 1 < n and tablero[p[0] + 1][p[1]] != "▆":
                nuevo_p[0] += 1
                if nuevo_p not in visitados and distancia_entre_puntos(nuevo_p, p_objetivo) < distancia_entre_puntos(p, p_objetivo):
                    camino_parcial.append(p)
                    laberinto(n, tablero, visitados, camino_parcial, camino_final, nuevo_p, acumulados + 1)
            elif i == 3 and p[0] - 1 > 0 and tablero[p[0] - 1][p[1]] != "▆":
                nuevo_p[0] -= 1
                if nuevo_p not in visitados and distancia_entre_puntos(nuevo_p, p_objetivo) < distancia_entre_puntos(p, p_objetivo):
                    camino_parcial.append(p)
                    laberinto(n, tablero, visitados, camino_parcial, camino_final, nuevo_p, acumulados + 1)


def distancia_entre_puntos(p1, p2):
    return math.sqrt(pow(abs(p1[0] - p2[0]), 2) + pow(abs(p1[1] - p2[1]), 2))


def imprimir_matriz(m):
    for i in m:
        print(i)


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



laberinto(10, tablero, [], [], [], [0,0], 0)
imprimir_matriz(tablero)
