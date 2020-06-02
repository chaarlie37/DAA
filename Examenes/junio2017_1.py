def digitos_comunes(a):
    solucion = [False] * 10
    n = len(a)
    if n == 0:
        return [True] * 10
    elif n == 1:
        aux = a[0]
        while aux != 0:
            solucion[aux % 10] = True
            aux = aux // 10
    else:
        mitad = n // 2
        for i in range(10):
            solucion[i] = digitos_comunes(a[0:mitad])[i] and digitos_comunes(a[mitad:])[i]
    return solucion





print(digitos_comunes([453, 154, 456, 452]))