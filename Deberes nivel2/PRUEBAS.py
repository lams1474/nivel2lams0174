class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias

    def prestar(self):
        if self.copias > 0:
            self.copias -= 1
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"No hay copias disponibles de '{self.titulo}'.")

    def devolver(self):
        self.copias += 1
        print(f"El libro '{self.titulo}' ha sido devuelto.")


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        libro.prestar()
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        libro.devolver()
        self.libros_prestados.remove(libro)


# Ejemplo de uso
libro1 = Libro("1984", "George Orwell", 3)
libro2 = Libro("El Quijote", "Miguel de Cervantes", 2)

usuario = Usuario("Carlos")
usuario.tomar_prestado(libro1)
usuario.tomar_prestado(libro2)
usuario.devolver_libro(libro1)
