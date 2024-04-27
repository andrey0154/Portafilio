
edades = []


for i in range(5):
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    edades.append(edad)


promedio_edades = sum(edades) / len(edades)


print(f"La edad promedio de las 5 personas es: {promedio_edades:.2f} años")
