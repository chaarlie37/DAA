def imprimir_polinomio(lista, grado):
    if lista == [0] and grado == 0:
        print(" + 0")
    elif len(lista) > 0:
        n = len(lista) - 1
        if lista[n] < 0:
            if n == 0:
                print(" - ", -lista[n], sep="")
            else:
                print(" - ", -lista[n], "x^", n, end="", sep="")
        elif lista[n] > 0:
            if n == 0:
                print(" + ", lista[n], sep="")
            else:
                print(" + ", lista[n], "x^", n, end="", sep="")
        imprimir_polinomio(lista[0:n], grado)



grado = int(input())
nums = input()
lista = []
for i in range(grado + 1):
    n = int(nums.split(" ")[i])
    lista.append(n)

imprimir_polinomio(lista, grado)
