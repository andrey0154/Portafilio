rango = range(20)

print(rango)

print("\n1) Ejemplo 1")
# El for repite la cantidad que le decimos
for i in range(20):
    print("El elemento es: ", i)

print("\n2) Ejemplo 2")
lista = ["Palabra", "Mundo"]
# El for repite para cada elemento que definimos
for elemento in lista:
    if (elemento == "Mundo"):
        print("El elemento del conjunto es: ", elemento)

print("\n3) Ejemplo 3")
# El for repite la cantidad que le decimos
for indice in range(5, 10):
    print("El numero es: ", indice)

print("\n4) Ejemplo 4")
# El for repite la cantidad que le decimos
for i in range(5, 100, 10):
    print("El elemento es: ", i)

print("\n5) Ejemplo 5 (while)")

valor = 20


while (valor > 0 and valor - 1 > 2):
    print("Multiplicando ", valor, " por 2: ", valor * 2)
    valor = valor - 1
print("Sali del while")

print("\n6) Ejemplo 6 (while)")

entrada = input("Ingrese una entrada para ingresar al while a) ingresa b) sale")

# Valida que la entrada sea a, para ingresar al ciclo
if entrada == "a":
    # El ciclo se repite siempre que entrada sea diferente a b
    while entrada != "b":
        print("Usted ingreso al ciclo while")
        entrada = input("Desea salir del ciclo? a) ingresa b) sale")
        # Evalua que la entrada sea valida, si no es valida, entra en este ciclo
        while entrada != "a" and entrada != "b":
            entrada = input("Ingrese una opcion valida a) ingresa b) sale")
elif entrada == "b":
    print("Elegiste la opcion de no ingresar")
else:
    print("Usted ingresó una opción incorrecta")

print("Termina el programa")
