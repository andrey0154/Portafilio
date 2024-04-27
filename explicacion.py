# Lista para almacenar usuarios, contraseñas y cédulas
usuarios = []
contrasenas = []
cedulas = []

# Diccionario para almacenar el inventario de vehículos por placa
inventario = {}

# Diccionario de sedes con sus respectivos horarios de atención
sedes = {
    "San José": "24 horas, los 7 días de la semana",
    "Alajuela": "24 horas, los 7 días de la semana",
    "Guanacaste": "Abren a las 4 am, cierran a las 11 pm.",
    "Limón": "Abren a las 6 am, cierran a las 10 pm.",
    "Puntarenas": "Abren a las 5 am, cierran a las 10 pm.",
    "Pérez Zeledón": "Abren a las 7 am, cierran a las 10 pm."
}

# Variable para almacenar la sede actual seleccionada
sede_actual = None

# Variable para controlar la ejecución del programa
continuar_ejecucion = True

# Diccionario para almacenar las reservas de los usuarios
reservas = {}

# Número de reserva inicial
numero_reserva = 1

# Bucle principal del programa
while continuar_ejecucion:
    # Verificar si no se ha seleccionado una sede
    if not sede_actual:
        print("Escoge una sede: ")
        # Mostrar las opciones de sedes disponibles
        for i, sede in enumerate(sedes.keys(), start=1):
            print(f"{i}. {sede} - Horario: {sedes[sede]}")
        # Seleccionar una sede
        opcion_ingreso = int(input("Elija una opción: "))
        sedes_disponibles = list(sedes.keys())
        if opcion_ingreso > 0 and opcion_ingreso <= len(sedes_disponibles):
            sede_actual = sedes_disponibles[opcion_ingreso - 1]
        else:
            print("Opción inválida, Intente de nuevo")
            continue

    print(f"Bienvenido a la sede {sede_actual}")

    # Bucle de ingreso de usuarios
    while True:
        print("Menú de ingreso:")
        print("1. Usuario registrado")
        print("2. Nuevo usuario")
        print("3. Usuario invitado")
        print("4. Cambiar de sede")
        print("5. Salir")
        opcion_ingreso = input("Elija una opción: ")

        # Opción para usuarios registrados
        if opcion_ingreso == "1":
            # Autenticación del usuario
            for intento in range(3):
                usuario_ingreso = input("Ingrese su usuario: ")
                contrasena_ingreso = input("Ingrese su contraseña: ")
                cedula_ingreso = input("Ingrese su cédula: ")

                # Verificar credenciales de usuario
                if (usuario_ingreso in usuarios and
                    contrasena_ingreso == contrasenas[usuarios.index(usuario_ingreso)] and
                        cedula_ingreso == cedulas[usuarios.index(usuario_ingreso)]):
                    print("Inicio de sesión exitoso. Bienvenido")

                    # Menú para usuarios registrados
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
                            # Agregar un vehículo al inventario
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
                                # Añadir vehículo al inventario
                                inventario[placa] = {"Marca": marca, "Año": año, "Modelo": modelo, "Cilindraje": cilindraje,
                                                     "Precio Alquiler": precio_alquiler, "Precio Vehículo": precio_vehiculo,
                                                     "Cantidad": cantidad}
                                print("Vehículo agregado exitosamente.")
                        # Opción para inhabilitar un vehículo
                        elif menu == "2":
                            placa = input("Ingrese la placa del vehículo: ")
                            if placa not in inventario:
                                print("No existe un vehículo con esa placa.")
                            else:
                                # Eliminar vehículo del inventario
                                del inventario[placa]
                                print("Vehículo inhabilitado exitosamente.")
                        # Opción para realizar una reserva
                        elif menu == "3":
                            marca = input(
                                "Ingrese la marca del vehículo que desea reservar: ")
                            año = input(
                                "Ingrese el año del vehículo que desea reservar: ")
                            modelo = input(
                                "Ingrese el modelo del vehículo que desea reservar: ")
                            cedula_confirmacion = input(
                                "Ingrese su cédula para confirmar la reserva: ")
                            # Verificar cédula para confirmar reserva
                            if cedula_confirmacion == cedulas[usuarios.index(usuario_ingreso)]:
                                modelo_existente = False
                                for placa, detalles in inventario.items():
                                    # Verificar disponibilidad del vehículo
                                    if "Marca" in detalles and detalles["Marca"] == marca and detalles["Año"] == año and detalles["Modelo"] == modelo and detalles["Cantidad"] > 0:
                                        modelo_existente = True
                                        detalles["Cantidad"] -= 1
                                        reserva = f"Vehículo: {marca} {año} {modelo}"
                                        if usuario_ingreso not in reservas:
                                            reservas[usuario_ingreso] = {
                                                numero_reserva: reserva}
                                        else:
                                            reservas[usuario_ingreso][numero_reserva] = reserva
                                        # Calcular precio total de la reserva
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
                        # Opción para mostrar vehículos disponibles
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
                        # Opción para visualizar y cancelar reservas
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
                        # Opción para salir del menú de usuario registrado
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
        # Opción para crear un nuevo usuario
        elif opcion_ingreso == "2":
            nuevo_usuario = input("Ingrese un nombre de usuario nuevo: ")
            if nuevo_usuario in usuarios:
                print("El nombre de usuario ya está en uso.")
                continue
            else:
                contrasena_nuevo_usuario = input("Ingrese una contraseña: ")
                cedula_nuevo_usuario = input("Ingrese su cédula: ")
                # Añadir nuevo usuario a las listas
                usuarios.append(nuevo_usuario)
                contrasenas.append(contrasena_nuevo_usuario)
                cedulas.append(cedula_nuevo_usuario)
                print("Usuario creado exitosamente. Ahora puede iniciar sesión.")
                continue
        # Opción para ingresar como usuario invitado
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
        # Opción para cambiar de sede
        elif opcion_ingreso == "4":
            print("Cambiando de sede...")
            sede_actual = None
            break
        # Opción para salir del programa
        elif opcion_ingreso == "5":
            print("Saliendo del sistema. ¡Hasta luego!")
            continuar_ejecucion = False
            break
        else:
            print("Opción inválida. Intente de nuevo.")

    if not continuar_ejecucion:
        break

""" True: La función True es una palabra reservada de Python que representa el valor lógico Verdadero. Se utiliza en este contexto para iniciar un bucle que se ejecutará siempre.
Enumerate: enumerate es una función incorporada de Python que devuelve un objeto enumerado. Este objeto es útil para obtener los índices y los elementos correspondientes de una secuencia iterable.
keys: keys es un método de los diccionarios de Python que devuelve una vista de todas las claves del diccionario.
continue: continue es una declaración de control de flujo en Python que se utiliza para saltar el resto del código dentro de un bucle y continuar con la siguiente iteración.
index: index es un método de las listas en Python que devuelve el índice de la primera aparición de un elemento en la lista.
items: items es un método de los diccionarios de Python que devuelve una vista de tuplas que contienen los pares (clave, valor) del diccionario.
get: get es un método de los diccionarios de Python que devuelve el valor asociado con una clave especificada.
false: False es una palabra reservada de Python que representa el valor lógico Falso. Se utiliza en este contexto para finalizar un bucle.
break: break es una declaración de control de flujo en Python que se utiliza para salir de un bucle antes de que se complete todas las iteraciones. """
