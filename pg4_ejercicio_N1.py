# Ejercicio 1

notas = [[], [], []]


def ingresar_notas():
    for i in range(3):
        print(f"Ingrese las notas finales para el curso {i+1}:")
        for j in range(5):
            nota = float(input(f"Nota del estudiante {j+1}: "))
            notas[i].append(nota)


def calcular_promedio_grupo(curso):
    return sum(notas[curso]) / len(notas[curso])


def calcular_porcentaje_aprobados(curso):
    aprobados = sum(1 for nota in notas[curso] if nota >= 70)
    return (aprobados / len(notas[curso])) * 100


def encontrar_max_min(curso):
    max_nota = max(notas[curso])
    min_nota = min(notas[curso])
    return max_nota, min_nota


ingresar_notas()

promedio_total = sum(sum(curso) for curso in notas) / sum(len(curso) for curso in notas)
print(f"El promedio total de todos los estudiantes es: {promedio_total}")

for i in range(3):
    promedio_grupo = calcular_promedio_grupo(i)
    print(f"Promedio del curso {i+1}: {promedio_grupo}")

for i in range(3):
    porcentaje_aprobados = calcular_porcentaje_aprobados(i)
    print(f"Porcentaje de aprobados en el curso {i+1}: {porcentaje_aprobados}%")

for i in range(3):
    max_nota, min_nota = encontrar_max_min(i)
    print(f"Nota mayor en el curso {i+1}: {max_nota}")
    print(f"Nota menor en el curso {i+1}: {min_nota}")
