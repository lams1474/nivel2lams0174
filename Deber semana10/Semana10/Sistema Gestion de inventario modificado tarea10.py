import os

# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}"

# Clase Inventario
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, "r") as file:
                    for line in file:
                        id, nombre, cantidad, precio = line.strip().split(",")
                        self.productos.append(Producto(int(id), nombre, int(cantidad), float(precio)))
                print("Inventario cargado desde archivo.")
            else:
                print("Archivo de inventario no encontrado. Se creará uno nuevo.")
        except FileNotFoundError:
            print("Error: Archivo de inventario no encontrado.")
        except PermissionError:
            print("Error: Permiso denegado para acceder al archivo.")
        except ValueError:
            print("Error: Archivo de inventario corrupto.")

    def guardar_inventario(self):
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(str(producto) + "\n")
            print("Inventario guardado en archivo.")
        except PermissionError:
            print("Error: Permiso denegado para escribir en el archivo.")

    def añadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            self.guardar_inventario()
            print("Producto añadido con éxito.")

    def actualizar_productos(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                self.guardar_inventario()
                print("Producto actualizado con éxito.")
                return
        print("Error: No se encontró un producto con ese ID.")

    def buscar_productos(self, nombre):
        resultados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        if resultados:
            print("Resultados de la búsqueda:")
            for producto in resultados:
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, "
                      f"Cantidad: {producto.get_cantidad()}, Precio: ${producto.get_precio():.2f}")
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            print("\nProductos en el inventario:")
            for producto in self.productos:
                print(f"ID: {producto.get_id()} | Nombre: {producto.get_nombre()} | "
                      f"Cantidad: {producto.get_cantidad()} | Precio: ${producto.get_precio():.2f}")
        else:
            print("\nEl inventario está vacío.")

# Interfaz de usuario (Menú interactivo en consola)
def mostrar_menu():
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar productos por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":  # Añadir producto
            try:
                id = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ").strip()
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: "))
                producto = Producto(id, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Error: Ingrese valores válidos para el ID, cantidad y precio.")

        elif opcion == "2":  # Eliminar producto
            try:
                id = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.actualizar_productos(id, cantidad=0) # Actualiza la cantidad a 0 para simular eliminación
            except ValueError:
                print("Error: Ingrese un ID válido.")

        elif opcion == "3":  # Actualizar producto
            try:
                id = int(input("Ingrese el ID del producto a actualizar: "))
                cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ").strip()
                precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ").strip()
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_productos(id, cantidad, precio)
            except ValueError:
                print("Error: Ingrese valores válidos.")

        elif opcion == "4":  # Buscar productos
            nombre = input("Ingrese el nombre del producto a buscar: ").strip()
            inventario.buscar_productos(nombre)

        elif opcion == "5":  # Mostrar todos los productos
            inventario.mostrar_productos()

        elif opcion == "6":  # Salir
            print("Saliendo del sistema...")
            break

        else:  # Opción inválida
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()