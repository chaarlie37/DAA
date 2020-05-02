def insertar_ordenado(a, x):  # insertar los elementos y que se ordenen por duracion
    if len(a) == 0 or a[len(a) - 1][2] <= x[2]:
        a.append(x)
    else:
        i = 0
        while a[i][2] <= x[2]:
            i += 1
        a.insert(i, x)


def voraz(tareas, t_max):
    horario = [-1] * t_max   # -1 -> hora disponible  <numero> -> hora ocupada por la tarea numero
    num_tareas = 0
    for i in range(len(tareas)):
        disponible = True
        for h in range(tareas[i][0], tareas[i][1]):
            disponible = horario[h] == -1
            if not disponible:
                break
        if disponible:
            num_tareas += 1
            for h in range(tareas[i][0], tareas[i][1]):
                horario[h] = i
    return num_tareas


num_tareas = int(input())
comienzo = input()
tiempos_comienzo = []
tiempos_finalizacion = []
for i in comienzo.split(sep=" "):
    tiempos_comienzo.append(int(i))
finalizacion = input()
for i in finalizacion.split(sep=" "):
    tiempos_finalizacion.append(int(i))

tiempo_max = max(tiempos_finalizacion)
tareas = []
for i in range(num_tareas):
    tarea = [tiempos_comienzo[i], tiempos_finalizacion[i],
             tiempos_finalizacion[i] - tiempos_comienzo[i]]  # [t_comienzo, t_finalizacion, duracion]
    insertar_ordenado(tareas, tarea)


print(voraz(tareas, tiempo_max))
