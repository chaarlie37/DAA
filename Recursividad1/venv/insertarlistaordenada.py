def f(a, x):
    if len(a) == 0:
        a[0] = x
        return a
    elif x >= a[len(a)-1]:
        return a + [x]
    else:
        if a[0] <= x:
            lista = [a[0]]
            length = len(a)
            return lista + f(a[1:length], x)
        else:
            lista = [x]
            return lista + a


n = int(input())
lista = []
cadena_entrada = input()
for i in range(n):
    lista.append(int(cadena_entrada.split(" ")[i]))

num = int(input())
lista = f(lista, num)
for i in range(n):
    print(lista[i], end=' ')
print(lista[n])

