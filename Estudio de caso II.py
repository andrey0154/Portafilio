import datetime

medicos_jefes = {"109858663": "Juan Romero", "30652745": "Sofia Tames"}
citas = []

class Cita:
    def __init__(self, fecha, hora, paciente, activado):
        self.fecha = fecha
        self.hora = hora
        self.paciente = paciente
        self.activado = activado

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.paciente} - {'Activada' if self.activado else 'No activada'}"


def verificar_medico():
    cedula = input("Por favor, ingresa tu cédula: ")
    return cedula in medicos_jefes


def agregar_cita():
    fecha = input("Por favor, ingresa la fecha de la cita (dd/mm/aaaa): ")
    hora = input("Por favor, ingresa la hora de la cita (hh:mm): ")
    paciente = input("Por favor, ingresa el nombre del paciente: ")
    activado = input("¿La cita está activada? (sí/no): ") == "sí"
    cita = Cita(fecha, hora, paciente, activado)
    citas.append(cita)


def mostrar_citas():
    hoy = datetime.date.today().strftime("%d/%m/%Y")
    citas_hoy = [cita for cita in citas if cita.fecha == hoy]
    if citas_hoy:
        print("Citas para hoy:")
        for cita in citas_hoy:
            print(cita)
    else:
        print("No hay citas para hoy.")


def main():
    while True:
        print("\n1. Verificar médico")
        print("2. Agregar cita")
        print("3. Mostrar citas del día")
        print("4. Salir")
        opcion = input("Por favor, selecciona una opción: ")
        if opcion == "1":
            if verificar_medico():
                print("Médico verificado exitosamente.")
            else:
                print("Cédula no encontrada.")
        elif opcion == "2":
            agregar_cita()
            print("Cita agregada exitosamente.")
        elif opcion == "3":
            mostrar_citas()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    main()
