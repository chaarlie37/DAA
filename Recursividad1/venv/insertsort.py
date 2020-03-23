def insertar(a, x):
    if len(a) == 0:
        a[0] = x
        return a
    elif x >= a[len(a)-1]:
        return a + [x]
    else:
        if a[0] <= x:
            lista = [a[0]]
            length = len(a)
            return lista + insertar(a[1:length], x)
        else:
            lista = [x]
            return lista + a

def insertSort(a):
    n = len(a)
    if n <= 1:
        return a
    else:
        return insertar(insertSort(a[0:n-1]), a[n-1])


num = int(input())
lista = []
cadena_entrada = input()
for i in range(num):
    lista.append(int(cadena_entrada.split(" ")[i]))

lista = insertSort(lista)

for i in range(num-1):
    print(lista[i], end=' ')
print(lista[num-1])