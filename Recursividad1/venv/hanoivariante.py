def hanoi(origen, aux, destino, discos):
    if discos == 1:
        imprimir(1, origen, aux)
        imprimir(1, aux, destino)
    else:
        hanoi(origen, aux, destino, discos - 1)
        imprimir(discos, origen, aux)
        hanoi(destino, aux, origen, discos - 1)
        imprimir(discos, aux, destino)
        hanoi(origen, aux, destino, discos - 1)


def imprimir(disco, origen, destino):
    print("Mueve disco ", disco, " desde torre ", origen, " a torre ", destino)


n = int(input())

hanoi(1, 2, 3, n)
