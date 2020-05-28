def mezclar(l1, l2):
    resultado = []
    for e in l1:
        resultado.append(e)
    for e in l2:
        i = 0
        while i < len(resultado) and e > resultado[i]:
            i += 1
        resultado.insert(i, e)
    return resultado


def mergesort(l):
    if len(l) == 1 or len(l) == 0:
        return l
    else:
        return mezclar(mergesort(l[0:len(l)//2]), mergesort(l[len(l)//2:len(l)]))


lista = [38, 27, 43, 3, 9, 82, 10]
print(mergesort(lista))
