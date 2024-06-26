usuarios = []
contrasenas = []
cedulas = []
inventario = {}
sedes = {
    "San José": "24 horas, los 7 días de la semana",
    "Alajuela": "24 horas, los 7 días de la semana",
    "Guanacaste": "Abren a las 4 am, cierran a las 11 pm.",
    "Limón": "Abren a las 6 am, cierran a las 10 pm.",
    "Puntarenas": "Abren a las 5 am, cierran a las 10 pm.",
    "Pérez Zeledón": "Abren a las 7 am, cierran a las 10 pm."
}

sede_actual = None
continuar_ejecucion = True
reservas = {}
numero_reserva = 1

while continuar_ejecucion:
    if not sede_actual:
        print("Escoge una sede: ")
        for i, sede in enumerate(sedes.keys(), start=1):
            print(f"{i}. {sede} - Horario: {sedes[sede]}")
        opcion_ingreso = int(input("Elija una opción: "))
        sedes_disponibles = list(sedes.keys())
        if opcion_ingreso > 0 and opcion_ingreso <= len(sedes_disponibles):
            sede_actual = sedes_disponibles[opcion_ingreso - 1]
        else:
            print("Opción inválida, Intente de nuevo")
            continue
    print(f"Bienvenido a la sede {sede_actual}")
    while True:
        print("Menú de ingreso:")
        print("1. Usuario registrado")
        print("2. Nuevo usuario")
        print("3. Usuario invitado")
        print("4. Cambiar de sede")
        print("5. Salir")
        opcion_ingreso = input("Elija una opción: ")

        if opcion_ingreso == "1":
            for intento in range(3):
                usuario_ingreso = input("Ingrese su usuario: ")
                contrasena_ingreso = input("Ingrese su contraseña: ")
                cedula_ingreso = input("Ingrese su cédula: ")

                if (usuario_ingreso in usuarios and
                    contrasena_ingreso == contrasenas[usuarios.index(usuario_ingreso)] and
                        cedula_ingreso == cedulas[usuarios.index(usuario_ingreso)]):
                    print("Inicio de sesión exitoso. Bienvenido")

                    while True:
                        print("Menú de usuario registrado:")
                        print("1. Agregar vehículo")
                        print("2. Inhabilitar vehículo")
                        print("3. Realizar reserva")
                        print("4. Mostrar vehículos disponibles")
                        print("5. Visualizar/Cancelar reservas")
                        print("6. Salir")
                        menu = input("Elige la opción que deseas: ")

                        if menu == "1":
                            placa = input("Ingrese la placa del vehículo: ")
                            if placa in inventario:
                                print("Ya existe un vehículo con esa placa.")
                            else:
                                marca = input(
                                    "Ingrese la marca del vehículo: ")
                                año = input("Ingrese el año del vehículo: ")
                                modelo = input(
                                    "Ingrese el modelo del vehículo: ")
                                cilindraje = input(
                                    "Ingrese el cilindraje del vehículo: ")
                                precio_alquiler = float(
                                    input("Ingrese el precio de alquiler por día del vehículo: "))
                                precio_vehiculo = float(
                                    input("Ingrese el precio del vehículo: "))
                                cantidad = int(
                                    input("Ingrese la cantidad de este vehículo: "))
                                inventario[placa] = {"Marca": marca, "Año": año, "Modelo": modelo, "Cilindraje": cilindraje,
                                                     "Precio Alquiler": precio_alquiler, "Precio Vehículo": precio_vehiculo,
                                                     "Cantidad": cantidad}
                                print("Vehículo agregado exitosamente.")
                        elif menu == "2":
                            placa = input("Ingrese la placa del vehículo: ")
                            if placa not in inventario:
                                print("No existe un vehículo con esa placa.")
                            else:
                                del inventario[placa]
                                print("Vehículo inhabilitado exitosamente.")
                        elif menu == "3":
                            marca = input(
                                "Ingrese la marca del vehículo que desea reservar: ")
                            año = input(
                                "Ingrese el año del vehículo que desea reservar: ")
                            modelo = input(
                                "Ingrese el modelo del vehículo que desea reservar: ")
                            cedula_confirmacion = input(
                                "Ingrese su cédula para confirmar la reserva: ")

                            if cedula_confirmacion == cedulas[usuarios.index(usuario_ingreso)]:
                                modelo_existente = False
                                for placa, detalles in inventario.items():
                                    if "Marca" in detalles and detalles["Marca"] == marca and detalles["Año"] == año and detalles["Modelo"] == modelo and detalles["Cantidad"] > 0:
                                        modelo_existente = True
                                        detalles["Cantidad"] -= 1
                                        reserva = f"Vehículo: {marca} {año} {modelo}"
                                        if usuario_ingreso not in reservas:
                                            reservas[usuario_ingreso] = {
                                                numero_reserva: reserva}
                                        else:
                                            reservas[usuario_ingreso][numero_reserva] = reserva
                                        precio_total_reserva = detalles["Precio Alquiler"] + (
                                            detalles["Precio Vehículo"] * 0.045) + 10
                                        print(
                                            f"Reserva realizada con éxito. El valor total de la reserva es: {precio_total_reserva}")
                                        numero_reserva += 1
                                        break

                                if not modelo_existente:
                                    print(
                                        "El modelo ingresado no está disponible para reserva o no existe en el inventario.")
                            else:
                                print(
                                    "La cédula ingresada no coincide con la registrada.")

                        elif menu == "4":
                            if inventario:
                                print("Vehículos disponibles: ")
                                for placa, detalles in inventario.items():
                                    print("Placa:", placa)
                                    print("Marca:", detalles.get(
                                        'Marca', 'No especificada'))
                                    print("Año:", detalles.get(
                                        'Año', 'No especificado'))
                                    print("Modelo:", detalles.get(
                                        'Modelo', 'No especificado'))
                                    print("------------------------")
                            else:
                                print("No hay vehículos disponibles.")

                        elif menu == "5":
                            if usuario_ingreso in reservas:
                                print("Reservas activas:")
                                for num_reserva, reserva in reservas[usuario_ingreso].items():
                                    print(f"{num_reserva}. {reserva}")
                                cancelar_reserva = input(
                                    "¿Desea cancelar alguna reserva? (si/no): ")
                                if cancelar_reserva.lower() == "si":
                                    num_reserva_cancelar = int(
                                        input("Ingrese el número de reserva que desea cancelar: "))
                                    if num_reserva_cancelar in reservas[usuario_ingreso]:
                                        del reservas[usuario_ingreso][num_reserva_cancelar]
                                        precio_total_cancelacion = 0.1 * precio_total_reserva
                                        print(
                                            f"Reserva cancelada exitosamente. El precio a pagar es: {precio_total_reserva} y el precio con la multa es: {precio_total_cancelacion + precio_total_reserva}")
                                    else:
                                        print(
                                            "El número de reserva ingresado no existe.")
                            else:
                                print("No tienes reservas activas.")

                        elif menu == "6":
                            print("Sesión cerrada. ¡Hasta luego!")
                            break
                        else:
                            print("Opción inválida. Intente de nuevo.")
                    break
                else:
                    print("Credenciales incorrectas. Intente de nuevo.")
            else:
                print("Demasiados intentos fallidos. Volviendo al menú principal.")
                break

        elif opcion_ingreso == "2":
            nuevo_usuario = input("Ingrese un nombre de usuario nuevo: ")
            if nuevo_usuario in usuarios:
                print("El nombre de usuario ya está en uso.")
                continue
            else:
                contrasena_nuevo_usuario = input("Ingrese una contraseña: ")
                cedula_nuevo_usuario = input("Ingrese su cédula: ")
                usuarios.append(nuevo_usuario)
                contrasenas.append(contrasena_nuevo_usuario)
                cedulas.append(cedula_nuevo_usuario)
                print("Usuario creado exitosamente. Ahora puede iniciar sesión.")
                continue

        elif opcion_ingreso == "3":
            print("Ingresando como usuario invitado...")
            print("Menú de usuario invitado:")
            print("1. Mostrar vehículos disponibles")
            print("2. Salir")
            opcion_invitado = input("Elija una opción: ")
            if opcion_invitado == "1":
                if inventario:
                    print("Vehículos disponibles: ")
                    for placa, detalles in inventario.items():
                        print("Placa:", placa)
                        print("Marca:", detalles.get(
                            'Marca', 'No especificada'))
                        print("Año:", detalles.get('Año', 'No especificado'))
                        print("Modelo:", detalles.get(
                            'Modelo', 'No especificado'))
                        print("------------------------")
                else:
                    print("No hay vehículos disponibles.")
            elif opcion_invitado == "2":
                print("Sesión de usuario invitado finalizada.")
            else:
                print("Opción inválida. Intente de nuevo.")

        elif opcion_ingreso == "4":
            print("Cambiando de sede...")
            sede_actual = None
            break

        elif opcion_ingreso == "5":
            print("Saliendo del sistema. ¡Hasta luego!")
            continuar_ejecucion = False
            break

        else:
            print("Opción inválida. Intente de nuevo.")

    if not continuar_ejecucion:
        break

print("*******************************************************")
