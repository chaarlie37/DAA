import random

def ej3(lista):
    i = 0
    while i < len(lista) - 1 and lista[i] < i:
        i += 1
    if lista[i] == i:
        return i
    else:
        return -1

# no es eficiente!!!

lista = []
for i in range(100):
    num = random.randrange(-100, 100)
    if num not in lista:
        lista.append(num)
lista.sort()
print(lista)
print(ej3(lista))