# lista
edades = []

# Solicitar edades
for i in range(5):
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    edades.append(edad)

# Calcular el promedio de edades
promedio_edades = sum(edades) / len(edades)

# resultado
print(f"La edad promedio de las 5 personas es: {promedio_edades:.2f} años")
