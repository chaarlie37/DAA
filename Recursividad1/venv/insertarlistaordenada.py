def f(a, x):
    if len(a) == 0:
        a[0] = x
        return a
    elif x >= a[len(a)-1]:
        return a + [x]
    else:
        if a[0] <= x:
            return [a[0]] + f(a[1:len(a)], x)
        else:
            return [x] + a


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



def auxinsert(x,a,n):
    if a[0]>x:
        a.insert(0,x)
        return a
    elif a[n] < x:
        a.insert(n+1, x)
        return a
    else:
        n= n-1
        return auxinsert(x,a,n-1)

def insertelem(x,a):
    n = len(a)
    if n==0:
        a.append(x)
        return a
    else:
        n = n-1
        return auxinsert(x,a,n)