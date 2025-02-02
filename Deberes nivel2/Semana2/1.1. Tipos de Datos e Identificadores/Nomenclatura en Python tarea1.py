class Persona:
    def __init__(self, nombre, edad):
        # Constructor: inicializa los atributos del objeto
        self.nombre = nombre
        self.edad = edad
        print(f"Persona creada: {self.nombre}, {self.edad} años")

    def __del__(self):
        # Destructor: realiza limpieza o cierre de recursos
        print(f"Persona eliminada: {self.nombre}")

# Crear una instancia de la clase Persona
persona1 = Persona("luis Maigua", 51)

# Eliminar la instancia (esto llamará al destructor)
del persona1