
import random

aportes = {
   500: 'Hamburguesa con papas y gaseosa',
   1000: 'Cupon cena para 2 personas',
   2000: 'Un día en el parque de diversiones con transporte y comida pago para 3 personas',
   5000: 'Fin de semana todo incluido en hotel paradisiaco para 2 personas'
}
numeros_ganadores = [random.randint(1, 100) for _ in range(4)]

miembros = {}

for _ in range(5):

    nombre = input("Nombre del miembro: ")
    cedula = input("Número de cédula: ")
    aporte = int(input("Monto aportado (500, 1000, 2000 o 5000 colones): "))
    aporte = int (aportes)

    if aportes in numeros_ganadores:
        miembros[cedula] = {"nombre": nombre, "monto": aportes}

for semana in range(4):
   print(f'Resultados de la semana {semana + 1}:')
   for i in range(1, 100):

    if i == numeros_ganadores[semana]:
        print(f'¡Felicidades! El ganador de la semana {semana + 1} es el participante {i} con aporte de {aporte} colones, el premio es {aportes.get(aporte)}')
    else:
       
        print(f'Participante {i} con aporte de {aporte} colones.')

for cedula, datos in miembros.items():
    if datos["monto"] in numeros_ganadores:
        print(f"Ganador: {datos['nombre']} (Cédula: {cedula})")
        print(f"Premio: {datos['monto']} colones")
        break

monto_total = sum(aportes["monto"] for datos in miembros.values())
print(f"Monto total recaudado: {monto_total} colones")