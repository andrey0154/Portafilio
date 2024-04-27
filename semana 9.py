
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


kilometros = [0]*7


for i in range(7):
    kilometros[i] = float(input(f"Por favor, ingresa los kilómetros que recorriste el {dias[i]}: "))


total = sum(kilometros)


for i in range(7):
    print(f"El {dias[i]} recorriste {kilometros[i]} kilómetros.")

print(f"En total, recorriste {total} kilómetros esta semana.")

#****************************************


butacas = [None]*10

def asignar_butaca(nombre, numero_de_butaca):
    
    if numero_de_butaca < 1 or numero_de_butaca > 10:
        print("El número de butaca no es válido. Debe ser un número entre 1 y 10.")
        return


    butacas[numero_de_butaca - 1] = nombre

def main():
    while True:
        nombre = input("Por favor, ingresa el nombre de la persona: ")
        numero_de_butaca = int(input("Por favor, ingresa el número de butaca: "))
        asignar_butaca(nombre, numero_de_butaca)

        print("Estado actual de las butacas:")
        for i in range(10):
            if butacas[i] is None:
                print(f"Butaca {i+1}: Vacía")
            else:
                print(f"Butaca {i+1}: {butacas[i]}")

        continuar = input("¿Deseas asignar otra butaca? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()

#***********************************************

def invertir_palabra(palabra):
    palabra_invertida = ''
    for caracter in palabra:
        palabra_invertida = caracter + palabra_invertida
    return palabra_invertida

def main():
    palabra = input("Por favor, ingresa una palabra: ")
    print(f"La palabra {palabra} al revés es {invertir_palabra(palabra)}.")

if __name__ == "__main__":
    main()

#**************************************************
    

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


ganancias = [0]*7


for i in range(7):
    ganancias[i] = float(input(f"Por favor, ingresa el monto que ganaste el {dias[i]}: "))


total = sum(ganancias)


dia_menor_ganancia = dias[ganancias.index(min(ganancias))]


print(f"El total de ganancias en la semana es {total}.")
print(f"El día que ganaste menos dinero fue el {dia_menor_ganancia}.")
