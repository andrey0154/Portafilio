def agregar_datos(ruta_archivo):
    try:
        with open(ruta_archivo, "w") as file:
            print("Este archivo es para que guardes las ventas de tus empleados")

            num_vendedores = input("Ingrese el número de vendedores: ")
            while not num_vendedores.isdigit() or int(num_vendedores) <= 0:
                print("Por favor, ingrese un número entero positivo.")
                num_vendedores = input("Ingrese el número de vendedores: ")

            num_vendedores = int(num_vendedores)

            for i in range(num_vendedores):
                nombre_vendedor = input("Digite el nombre del vendedor {}: ".format(i+1))
                monto_venta = input("Digite el monto de venta en dólares: ")

                while not monto_venta.replace('.', '', 1).isdigit():
                    print("Por favor, ingrese un número válido.")
                    monto_venta = input("Digite el monto de venta en dólares: ")

                file.write("{},{}\n".format(nombre_vendedor, monto_venta))

            print("Guardaste todo con exito")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def mostrar_datos(ruta_archivo):
    try:
        with open(ruta_archivo, "r") as file:
            print("Datos de ventas:")
            for linea in file:
                nombre_vendedor, monto_venta = linea.strip().split(',')
                print("Vendedor: {}, Monto de Venta: {} dólares".format(nombre_vendedor, monto_venta))
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ruta completa del archivo
ruta_archivo = r"c:/Users/andre/OneDrive/Escritorio/Portafolio Progra basica/Python/reto_grupal.py"

# Ejemplo de uso
agregar_datos(ruta_archivo)
mostrar_datos(ruta_archivo)
