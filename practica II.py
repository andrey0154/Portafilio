class Administrador:
    def __init__(self):
        self.productos = {
            'Articulos enlatados': [],
            'Productos de limpieza': [],
            'Carnes': [],
            'Granos': []
        }

    def agregar_producto(self, grupo, producto):
        if producto not in self.productos[grupo]:
            self.productos[grupo].append(producto)
            print(f'Producto {producto} agregado al grupo {grupo}.')
        else:
            print('El producto ya existe.')

    def eliminar_producto(self, grupo, producto):
        if producto in self.productos[grupo]:
            self.productos[grupo].remove(producto)
            print(f'Producto {producto} eliminado del grupo {grupo}.')
        else:
            print('El producto no existe.')

    def actualizar_producto(self, grupo, producto_viejo, producto_nuevo):
        if producto_viejo in self.productos[grupo]:
            indice = self.productos[grupo].index(producto_viejo)
            self.productos[grupo][indice] = producto_nuevo
            print(f'Producto {producto_viejo} actualizado a {producto_nuevo} en el grupo {grupo}.')
        else:
            print('El producto no existe.')

    def mostrar_productos(self):
        for grupo, productos in self.productos.items():
            print(f'\nGrupo {grupo}:')
            for i, producto in enumerate(productos, 1):
                print(f'- Producto {i}: {producto}')

    def buscar_producto(self, producto):
        for grupo, productos in self.productos.items():
            if producto in productos:
                print(f'El producto {producto} se encuentra en el grupo {grupo}.')
                return
        print('El producto no existe.')

admin = Administrador()

while True:
    print("\n1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Mostrar productos")
    print("5. Buscar producto")
    print("6. Salir")
    opcion = input("Elige una opción: ")

    if opcion == '1':
        grupo = input("Ingresa el grupo del producto: ")
        producto = input("Ingresa el nombre del producto: ")
        admin.agregar_producto(grupo, producto)
    elif opcion == '2':
        grupo = input("Ingresa el grupo del producto: ")
        producto = input("Ingresa el nombre del producto: ")
        admin.eliminar_producto(grupo, producto)
    elif opcion == '3':
        grupo = input("Ingresa el grupo del producto: ")
        producto_viejo = input("Ingresa el nombre del producto viejo: ")
        producto_nuevo = input("Ingresa el nombre del producto nuevo: ")
        admin.actualizar_producto(grupo, producto_viejo, producto_nuevo)
    elif opcion == '4':
        admin.mostrar_productos()
    elif opcion == '5':
        producto = input("Ingresa el nombre del producto: ")
        resultado = admin.buscar_producto(producto)
        print(resultado)
    elif opcion == '6':
        break
    

    else:
        print("Opción inválida. Por favor, intenta de nuevo.")

print("****Saliste del Programa****")
