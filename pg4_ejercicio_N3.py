# Ejercicio 3, Salarios de jugadores

denominaciones = [50000, 20000, 10000, 5000, 2000, 1000, 500, 100, 50, 25]


salarios = [int(input(f"Ingrese el salario del jugador {i+1}: ")) for i in range(25)]


def calcular_desglose(salario, denominaciones):
    desglose = []
    for den in denominaciones:
        cantidad = salario // den
        salario -= cantidad * den
        desglose.append(cantidad)
    return desglose

desgloses = [calcular_desglose(salario, denominaciones) for salario in salarios]


sumatoria = [sum(desglose[i] for desglose in desgloses) for i in range(len(denominaciones))]

for den, suma in zip(denominaciones, sumatoria):
    print(f"Se necesitan {suma} billetes/monedas de {den}")

