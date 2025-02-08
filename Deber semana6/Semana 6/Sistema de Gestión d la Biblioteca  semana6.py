# Sistema de Gestión de Biblioteca
# Demuestra conceptos de POO: Herencia, Encapsulación y Polimorfismo

class Material:
    """Clase base que representa un material de biblioteca"""
    def __init__(self, titulo, codigo):
        self._titulo = titulo  # Encapsulación usando protected
        self.__codigo = codigo  # Encapsulación usando private
        self._prestado = False

    def prestar(self):
        """Método para prestar el material"""
        if not self._prestado:
            self._prestado = True
            return f"Material '{self._titulo}' prestado exitosamente."
        return f"Material '{self._titulo}' no disponible."

    def devolver(self):
        """Método para devolver el material"""
        if self._prestado:
            self._prestado = False
            return f"Material '{self._titulo}' devuelto exitosamente."
        return f"Material '{self._titulo}' no estaba prestado."

    def obtener_codigo(self):
        """Método para acceder al código privado"""
        return self.__codigo

    def mostrar_detalles(self):
        """Método polimórfico para mostrar detalles del material"""
        return f"Material genérico: {self._titulo}"


class Libro(Material):
    """Clase derivada que hereda de Material"""
    def __init__(self, titulo, codigo, autor, paginas):
        # Llamada al constructor de la clase base
        super().__init__(titulo, codigo)
        self.autor = autor
        self.paginas = paginas

    def mostrar_detalles(self):
        """Sobrescritura del método mostrar_detalles (Polimorfismo)"""
        return f"Libro: {self._titulo} por {self.autor}, {self.paginas} páginas"


class Revista(Material):
    """Clase derivada que hereda de Material"""
    def __init__(self, titulo, codigo, numero, mes):
        super().__init__(titulo, codigo)
        self.numero = numero
        self.mes = mes

    def mostrar_detalles(self):
        """Sobrescritura del método mostrar_detalles (Polimorfismo)"""
        return f"Revista: {self._titulo}, Número {self.numero}, Mes: {self.mes}"


# Demostración del funcionamiento
def main():
    # Creación de instancias
    libro = Libro("Don Quijote", "L001", "Miguel de Cervantes", 863)
    revista = Revista("National Geographic", "R001", 255, "Enero")

    # Lista de materiales para demostrar polimorfismo
    materiales = [libro, revista]

    # Demostración de polimorfismo
    print("\n=== Demostración de Polimorfismo ===")
    for material in materiales:
        print(material.mostrar_detalles())

    # Demostración de encapsulación y métodos
    print("\n=== Demostración de Encapsulación y Métodos ===")
    print(f"Código del libro: {libro.obtener_codigo()}")
    print(libro.prestar())
    print(libro.prestar())  # Intento de prestar un libro ya prestado
    print(libro.devolver())

    # Demostración con la revista
    print("\n=== Operaciones con Revista ===")
    print(revista.prestar())
    print(revista.mostrar_detalles())


if __name__ == "__main__":
    main()