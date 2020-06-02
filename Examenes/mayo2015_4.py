from random import randrange

def mochila(lista, c):
    solP = []
    solO = []
    print(buscar(len(lista), 0, 0, solP, solO, -1, lista, c))
    print(solP)
    return mochila_aux(lista, c, [None] * len(lista), [0], 0, 0)


def mochila_aux(lista, c, subl, aproximacion, i, j):
    if len(lista) == 1:
        return lista
    elif j == len(lista) or i == len(lista):
        return aproximacion
    else:
        for k in range(i, len(lista)):
            subl[j] = lista[k]
            total = total_lista(subl[0:j+1])
            if total == c:
                return subl[0:j+1]
            elif total < c:
                if total > total_lista(aproximacion):
                    aproximacion = subl[0:j+1]
                return mochila_aux(lista, c, subl, aproximacion, k + 1, j + 1)
        return mochila_aux(lista, c, subl, aproximacion, i + 1, j)


def buscar(n,i,p,solP,solO,PesoO,l,c):
    for k in range(0,2):
        if(p+k*l[i]<=c):
            solP.append(i)
            np= p+k*l[i]
            if(i==n-1):
                if(np>PesoO):
                    PesoO=np
                    for j in range (0,len(solP)):
                        solO.append(solP[j])
                    solP.clear()
            else:
                PesoO= buscar(n,i+1,np,solP,solO,PesoO,l,c)
    return PesoO



def total_lista(l):
    suma = 0
    for i in l:
        suma += i
    return suma

'''
l = []
for i in range(randrange(10, 100)):
    l.append(randrange(1, 20))

'''


l = [7, 9, 17, 8, 6, 8, 11]

# [7, 9, 17, 8, 6, 8, 11, 6, 6, 9, 9, 19, 19, 11, 7, 2, 5, 17, 3, 13, 11, 7, 1, 15, 1, 11, 3, 10, 19, 14, 10, 2, 16, 3, 4, 6, 13, 1, 15, 1, 12, 10, 10, 4, 8, 15, 3, 9]

# c = randrange(200, 500)
c = 15
print("C:", c)
print(l)
l2 = mochila(l, c)
print(l2)
print(total_lista(l2))