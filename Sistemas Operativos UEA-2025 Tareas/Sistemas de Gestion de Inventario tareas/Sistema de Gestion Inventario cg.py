class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID único del producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        # Verificar si el ID es único
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("Error: El ID del producto ya existe.")
            return
        self.productos.append(producto)
        print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        print("Producto eliminado si existía.")

    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        for p in self.productos:
            if p.id_producto == id_producto:
                p.actualizar_cantidad(nueva_cantidad)
                print("Cantidad actualizada.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        return encontrados

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)


def menu():
    inventario = Inventario()
    while True:
        print("\nSistema de Gestión de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad de producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto: ")
            nueva_cantidad = int(input("Nueva cantidad: "))
            inventario.actualizar_cantidad(id_producto, nueva_cantidad)
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            productos = inventario.buscar_producto_por_nombre(nombre)
            if productos:
                for p in productos:
                    print(p)
            else:
                print("No se encontraron productos con ese nombre.")
        elif opcion == "5":
            inventario.mostrar_inventario()
        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    menu()
