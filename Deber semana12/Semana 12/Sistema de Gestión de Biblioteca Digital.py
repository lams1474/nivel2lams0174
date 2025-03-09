# -*- coding: utf-8 -*-

class Libro:
    """Representa un libro con título, autor, categoría e ISBN."""
    def __init__(self, titulo_autor, categoria, isbn):
        """Inicializa un libro con atributos inmutables."""
        self.titulo_autor = titulo_autor  # Tupla (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        """Devuelve una representación legible del libro."""
        return f"Título: {self.titulo_autor[0]}, Autor: {self.titulo_autor[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"

class Usuario:
    """Representa un usuario de la biblioteca."""
    def __init__(self, nombre, id_usuario):
        """Inicializa un usuario con nombre e ID único."""
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        """Devuelve una representación legible del usuario."""
        return f"Nombre: {self.nombre}, ID: {self.id_usuario}"

class Biblioteca:
    """Gestiona libros, usuarios y préstamos."""
    def __init__(self):
        """Inicializa la biblioteca con colecciones vacías."""
        self.libros = {}  # ISBN: Libro
        self.usuarios = set()  # Conjunto de IDs de usuario

    def añadir_libro(self, libro):
        """Añade un libro a la biblioteca."""
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya existe.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo_autor[0]}' añadido.")

    def quitar_libro(self, isbn):
        """Quita un libro de la biblioteca."""
        if isbn in self.libros:
            libro_eliminado = self.libros.pop(isbn)
            print(f"Libro '{libro_eliminado.titulo_autor[0]}' eliminado.")
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        """Registra un nuevo usuario."""
        if any(u.id_usuario == usuario.id_usuario for u in self.usuarios):
            print(f"El usuario con ID {usuario.id_usuario} ya existe.")
        else:
            self.usuarios.add(usuario)
            print(f"Usuario '{usuario.nombre}' registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        """Da de baja a un usuario."""
        usuario_a_eliminar = None
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                usuario_a_eliminar = usuario
                break
        if usuario_a_eliminar:
            self.usuarios.remove(usuario_a_eliminar)
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")

    def prestar_libro(self, isbn, id_usuario):
        """Presta un libro a un usuario."""
        if isbn not in self.libros:
            print(f"No se encontró el libro con ISBN {isbn}.")
            return
        libro = self.libros[isbn]
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                usuario.libros_prestados.append(libro)
                print(f"Libro '{libro.titulo_autor[0]}' prestado a '{usuario.nombre}'.")
                return
        print(f"No se encontró el usuario con ID {id_usuario}.")

    def devolver_libro(self, isbn, id_usuario):
        """Devuelve un libro prestado."""
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                for libro in usuario.libros_prestados:
                    if libro.isbn == isbn:
                        usuario.libros_prestados.remove(libro)
                        print(f"Libro '{libro.titulo_autor[0]}' devuelto por '{usuario.nombre}'.")
                        return
                print(f"El usuario no tiene prestado el libro con ISBN {isbn}.")
                return
        print(f"No se encontró el usuario con ID {id_usuario}.")

    def buscar_libros(self, criterio, valor):
        """Busca libros por título, autor o categoría."""
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.titulo_autor[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.titulo_autor[1].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        if resultados:
            print(f"Resultados de búsqueda por {criterio} '{valor}':")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros por {criterio} '{valor}'.")

    def listar_libros_prestados(self, id_usuario):
        """Lista los libros prestados a un usuario."""
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                if usuario.libros_prestados:
                    print(f"Libros prestados a '{usuario.nombre}':")
                    for libro in usuario.libros_prestados:
                        print(libro)
                else:
                    print(f"'{usuario.nombre}' no tiene libros prestados.")
                return
        print(f"No se encontró el usuario con ID {id_usuario}.")

# Ejemplo de uso
biblioteca = Biblioteca()

# Libros
libro1 = Libro(("Cien años de soledad", "Gabriel García Márquez"), "Novela", "978-0307474728")
libro2 = Libro(("1984", "George Orwell"), "Ciencia Ficción", "978-0451524935")
libro3 = Libro(("El Principito", "Antoine de Saint-Exupéry"), "Fábula", "978-0156012195")
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)

# Usuarios
usuario1 = Usuario("Luis Maigua", "001")
usuario2 = Usuario("Lams 1474", "002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Préstamos
biblioteca.prestar_libro("978-0307474728", "001")
biblioteca.prestar_libro("978-0451524935", "002")

# Búsquedas
biblioteca.buscar_libros("titulo", "1984")
biblioteca.buscar_libros("autor", "Gabriel García Márquez")
biblioteca.buscar_libros("categoria", "Fábula")

# Libros prestados
biblioteca.listar_libros_prestados("001")

# Devolución
biblioteca.devolver_libro("978-0307474728", "001")