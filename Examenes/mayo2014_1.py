def elemento_mayoritario(a, elemento, num_apariciones):
    if len(a) == 1:
        elemento[0] = a[0]
        num_apariciones[0] = 1
        return True
    elif len(a) > 1:
        mitad = len(a) // 2
        hayMayoritario = False
        if elemento_mayoritario(a[:mitad], elemento, num_apariciones):
            for i in a[mitad:]:
                if i == elemento[0]:
                    num_apariciones[0] += 1
            if num_apariciones[0] > mitad:
                hayMayoritario = True

        if not hayMayoritario:
            if elemento_mayoritario(a[mitad:], elemento, num_apariciones):
                for i in a[:mitad]:
                    if i == elemento[0]:
                        num_apariciones[0] += 1
                if num_apariciones[0] > mitad:
                    hayMayoritario = True

        return hayMayoritario



l = [4, 4, 2, 3, 3, 3, 3, 3]
num = [None]
print(elemento_mayoritario(l, num, [0]))
print(num)