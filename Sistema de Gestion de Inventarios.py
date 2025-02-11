import os

class Producto:
    def __init__(self, ID, nombre, cantidad, precio):
        self.ID = ID
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_ID(self):
        return self.ID

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_ID(self, ID):
        self.ID = ID

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):  # Para mostrar información del producto de forma legible
        return f"ID: {self.ID}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        if not any(p.get_ID() == producto.get_ID() for p in self.productos):
            self.productos.append(producto)
            print("Producto añadido.")
        else:
            print("¡Error! ID de producto duplicado.")

    def eliminar_producto(self, ID):
        for i, producto in enumerate(self.productos):
            if producto.get_ID() == ID:
                del self.productos[i]
                print("Producto eliminado.")
                return
        print("¡Error! Producto no encontrado.")

    def actualizar_producto(self, ID, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_ID() == ID:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print("Producto actualizado.")
                return
        print("¡Error! Producto no encontrado.")

    def buscar_productos(self, nombre):
        resultados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        return resultados

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return

        print("--- Inventario ---")
        print("ID\tNombre\tCantidad\tPrecio")  # Encabezado de la tabla
        for producto in self.productos:
            print(f"{producto.get_ID()}\t{producto.get_nombre()}\t{producto.get_cantidad()}\t{producto.get_precio()}")


def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    inventario = Inventario()

    while True:
        limpiar_consola()  # Limpia la consola en cada iteración
        print("\n--- Menú de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto(s)")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Ingrese una opción: ")

        try:
            if opcion == "1":
                ID = input("ID del producto: ")
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(ID, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            elif opcion == "2":
                ID = input("ID del producto a eliminar: ")
                inventario.eliminar_producto(ID)
            elif opcion == "3":
                ID = input("ID del producto a actualizar: ")
                cantidad = input("Nueva cantidad (o Enter para omitir): ")
                precio = input("Nuevo precio (o Enter para omitir): ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(ID, cantidad, precio)
            elif opcion == "4":
                nombre = input("Nombre a buscar: ")
                resultados = inventario.buscar_productos(nombre)
                if resultados:
                    print("Productos encontrados:")
                    for producto in resultados:
                        print(producto)
                else:
                    print("No se encontraron productos con ese nombre.")
            elif opcion == "5":
                inventario.mostrar_inventario()
            elif opcion == "6":
                break
            else:
                print("Opción inválida. Intente de nuevo.")

            input("\nPresione Enter para continuar...")  # Pausa antes de limpiar la consola

        except ValueError:
            print("¡Error! Datos inválidos. Asegúrese de ingresar números para cantidad y precio.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    main()