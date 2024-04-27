class Estudiante:
    def __init__(self, nombre, numero_de_grupo, calificacion):
        self.nombre = nombre
        self.numero_de_grupo = numero_de_grupo
        self.calificacion = calificacion

estudiantes = []

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    numero_de_grupo = input("Ingrese el número de grupo del estudiante: ")
    calificacion = float(input("Ingrese la calificación del estudiante: "))
    estudiantes.append(Estudiante(nombre, numero_de_grupo, calificacion))

def mostrar_estudiantes():
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante.nombre}, Grupo: {estudiante.numero_de_grupo}, Calificación: {estudiante.calificacion}")

def menu():
    while True:
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            agregar_estudiante()
        elif opcion == 2:
            mostrar_estudiantes()
        elif opcion == 3:
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu()
