class Persona:
    def __init__(self, nombre, temperatura):
        self.nombre = nombre
        self.temperatura = temperatura

class Dia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.personas = []

    def agregar_persona(self, nombre, temperatura):
        self.personas.append(Persona(nombre, temperatura))

    def mostrar_resultados(self):
        if not self.personas:
            print(f"No hay datos para el día {self.nombre}.")
            return

        temperaturas = [persona.temperatura for persona in self.personas]
        nombres = [persona.nombre for persona in self.personas]
        temp_promedio = sum(temperaturas) / len(temperaturas)
        max_temp = max(temperaturas)
        min_temp = min(temperaturas)
        max_nombre = nombres[temperaturas.index(max_temp)]
        min_nombre = nombres[temperaturas.index(min_temp)]

        print(f"{self.nombre}")
        print(f"- Temperatura promedio: {temp_promedio}")
        print(f"- Temperatura máxima: {max_temp} | {max_nombre}")
        print(f"- Temperatura mínima: {min_temp} | {min_nombre}")

dias = [Dia("Lunes"), Dia("Martes"), Dia("Miércoles"), Dia("Jueves"), Dia("Viernes")]

while True:
    print("\nSeleccione el día que desea ingresar")
    for i, dia in enumerate(dias, 1):
        print(f"[{i}] {dia.nombre}")
    print("[6] Mostrar resultados y salir")

    opcion = int(input())
    if opcion == 6:
        for dia in dias:
            dia.mostrar_resultados()
        print("Hasta luego.")
        break

    nombre = input("Ingrese su nombre: ")
    temperatura = float(input("Ingrese su temperatura: "))
    dias[opcion - 1].agregar_persona(nombre, temperatura)
