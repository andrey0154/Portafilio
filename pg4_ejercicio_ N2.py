#ejercicio 2

pasajeros = [[0 for _ in range(4)] for _ in range(5)]

def capturar_pasajeros():
    for i in range(5):
        for j in range(4):
            while True:
                p = int(input(f"Ingrese la cantidad de pasajeros del servicio {j+1} del día {i+1}: "))
                if 0 <= p <= 60:
                    pasajeros[i][j] = p
                    break
                else:
                    print("La cantidad de pasajeros debe ser un número entre 0 y 60. Intente de nuevo.")

def promedio_por_dia():
    return [sum(pasajeros[i]) / 4 for i in range(5)]

def promedio_general():
    return sum(sum(pasajeros[i]) for i in range(5)) / 20

def mejor_servicio():
    servicios = [sum(pasajeros[i][j] for i in range(5)) for j in range(4)]
    return servicios.index(max(servicios)) + 1

def momento_menos_pasajeros():
    dia = min(range(5), key=lambda i: min(pasajeros[i]))
    servicio = pasajeros[dia].index(min(pasajeros[dia]))
    return dia + 1, servicio + 1

def menu():
    while True:
        print("1. Capturar pasajeros")
        print("2. Mostrar promedio por día")
        print("3. Mostrar promedio general")
        print("4. Mostrar el mejor servicio")
        print("5. Mostrar el momento con menos pasajeros")
        print("6. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            capturar_pasajeros()
        elif opcion == 2:
            print(f"Promedio por día: {promedio_por_dia()}")
        elif opcion == 3:
            print(f"Promedio general: {promedio_general()}")
        elif opcion == 4:
            print(f"El mejor servicio es el servicio {mejor_servicio()}")
        elif opcion == 5:
            dia, servicio = momento_menos_pasajeros()
            print(f"El momento con menos pasajeros es el servicio {servicio} del día {dia}")
        elif opcion == 6:
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu()