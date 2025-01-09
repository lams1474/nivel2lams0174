# Clase que representa un producto en la tienda virtual
class Producto:
    def __init__(self, nombre, precio, stock):
        # Atributos de la clase Producto
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio unitario del producto
        self.stock = stock    # Cantidad disponible en stock

    # Método para actualizar el stock después de una venta
    def actualizar_stock(self, cantidad):
        self.stock -= cantidad  # Reduce el stock según la cantidad vendida
        print(f"Stock de {self.nombre} actualizado. Quedan {self.stock} unidades.")

# Clase que representa un carrito de compras
class Carrito:
    def __init__(self):
        # Atributo que almacena una lista de productos en el carrito
        self.productos = []  # Lista de tuplas (producto, cantidad)

    # Método para agregar productos al carrito
    def agregar_producto(self, producto, cantidad):
        if producto.stock >= cantidad:  # Verifica si hay suficiente stock
            self.productos.append((producto, cantidad))  # Agrega el producto al carrito
            producto.actualizar_stock(cantidad)  # Actualiza el stock del producto
        else:
            print(f"No hay suficiente stock de {producto.nombre}.")  # Mensaje de error si no hay suficiente stock

    # Método para mostrar los productos que están en el carrito
    def mostrar_carrito(self):
        print("Productos en el carrito:")
        for producto, cantidad in self.productos:  # Itera sobre los productos en el carrito
            print(f"{producto.nombre} - Cantidad: {cantidad} - Precio Unitario: ${producto.precio}")
            # Muestra el nombre, cantidad y precio unitario de cada producto

# Ejemplo de uso
producto1 = Producto("Laptop", 1000, 10)  # Crear un producto llamado Laptop
producto2 = Producto("Mouse", 50, 20)    # Crear un producto llamado Mouse

carrito = Carrito()  # Crear un carrito de compras
carrito.agregar_producto(producto1, 2)  # Agregar 2 laptops al carrito
carrito.agregar_producto(producto2, 5)  # Agregar 5 mouses al carrito
carrito.mostrar_carrito()  # Mostrar los productos en el carrito
