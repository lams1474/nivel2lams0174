# Archivo: inventario_completo.py

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        Inicializa los atributos del producto: ID, nombre, cantidad y precio.
        """
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos getters (para obtener los valores de los atributos)
    def get_id(self):
        """Devuelve el ID del producto."""
        return self.id

    def get_nombre(self):
        """Devuelve el nombre del producto."""
        return self.nombre

    def get_cantidad(self):
        """Devuelve la cantidad del producto."""
        return self.cantidad

    def get_precio(self):
        """Devuelve el precio del producto."""
        return self.precio

    # Métodos setters (para modificar los valores de los atributos)
    def set_nombre(self, nombre):
        """Modifica el nombre del producto."""
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        """Modifica la cantidad del producto."""
        self.cantidad = cantidad

    def set_precio(self, precio):
        """Modifica el precio del producto."""
        self.precio = precio


class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa una lista vacía para almacenar los productos.
        """
        self.productos = []

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario.
        Verifica que el ID del producto no esté duplicado.
        """
        # Verificar si el ID ya existe en la lista de productos
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario por su ID.
        """
        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                print("Producto eliminado con éxito.")
                return
        print("Error: No se encontró un producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto por su ID.
        """
        for producto in self.productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print("Producto actualizado con éxito.")
                return
        print("Error: No se encontró un producto con ese ID.")

    def buscar_producto(self, nombre):
        """
        Busca productos por nombre (puede haber nombres similares).
        """
        resultados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        """
        Muestra todos los productos en el inventario.
        """
        if self.productos:
            for producto in self.productos:
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
        else:
            print("El inventario está vacío.")


def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    """
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def main():
    """
    Función principal del programa.
    """
    inventario = Inventario()  # Creamos una instancia de Inventario

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Añadir un nuevo producto
            id = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            # Eliminar un producto por ID
            id = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(id)

        elif opcion == "3":
            # Actualizar un producto por ID
            id = int(input("Ingrese el ID del producto a actualizar: "))
            cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            # Buscar productos por nombre
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            # Mostrar todos los productos
            inventario.mostrar_productos()

        elif opcion == "6":
            # Salir del programa
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()