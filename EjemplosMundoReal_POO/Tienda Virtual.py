class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock -= cantidad
        print(f"Stock de {self.nombre} actualizado. Quedan {self.stock} unidades.")


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        if producto.stock >= cantidad:
            self.productos.append((producto, cantidad))
            producto.actualizar_stock(cantidad)
        else:
            print(f"No hay suficiente stock de {producto.nombre}.")

    def mostrar_carrito(self):
        print("Productos en el carrito:")
        for producto, cantidad in self.productos:
            print(f"{producto.nombre} - Cantidad: {cantidad} - Precio Unitario: ${producto.precio}")


# Ejemplo de uso
producto1 = Producto("Laptop", 1000, 10)
producto2 = Producto("Mouse", 50, 20)

carrito = Carrito()
carrito.agregar_producto(producto1, 2)
carrito.agregar_producto(producto2, 5)
carrito.mostrar_carrito()
