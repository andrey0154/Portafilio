# Ejercicio 4

print ("Bienvenido al abastecedor Don Juan")

aforo = 0

def registrar_ingreso():
    global aforo
    ingreso = int(input("Ingrese el número de personas que ingresan: "))
    if aforo + ingreso <= 100:
        aforo += ingreso
        print("Ingreso registrado. Aforo actual:", aforo)
    else:
        print("El aforo excedería el máximo con ese ingreso. No se puede registrar.")

registrar_ingreso()
def registrar_egreso():
    global aforo
    egreso = int(input("Ingrese el número de personas que salen: "))
    if aforo - egreso >= 0:
        aforo -= egreso
        print("Egreso registrado. Aforo actual:", aforo)
    else:
        print("No hay suficientes personas en el abastecedor para ese egreso. No se puede registrar.")

registrar_egreso()
