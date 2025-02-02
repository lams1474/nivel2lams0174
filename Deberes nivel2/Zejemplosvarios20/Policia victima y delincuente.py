from abc import ABC, abstractmethod

# Clase base: Personaje
class Personaje(ABC):
    def __init__(self, nombre):
        self.__nombre = nombre  # Encapsulamiento

    def get_nombre(self):
        return self.__nombre

    @abstractmethod
    def accion(self):
        pass

# Clase: Policía
class Policia(Personaje):
    def __init__(self, nombre, rango):
        super().__init__(nombre)
        self.__rango = rango  # Encapsulamiento

    def arrestar(self, delincuente):
        return f"{self.get_nombre()} arrestó a {delincuente.get_nombre()}."

    def proteger(self, victima):
        return f"{self.get_nombre()} está protegiendo a {victima.get_nombre()}."

    def accion(self):
        return f"{self.get_nombre()}, un policía {self.__rango}, patrulla la zona."

# Clase: Víctima
class Victima(Personaje):
    def __init__(self, nombre, estado):
        super().__init__(nombre)
        self.__estado = estado  # Encapsulamiento

    def pedir_ayuda(self):
        return f"{self.get_nombre()} está pidiendo ayuda."

    def reportar_delito(self):
        return f"{self.get_nombre()} ha reportado un delito."

    def accion(self):
        return f"{self.get_nombre()} está {self.__estado} y busca ayuda."

# Clase: Delincuente
class Delincuente(Personaje):
    def __init__(self, nombre, delito):
        super().__init__(nombre)
        self.__delito = delito  # Encapsulamiento

    def cometer_delito(self):
        return f"{self.get_nombre()} está cometiendo un {self.__delito}."

    def escapar(self):
        return f"{self.get_nombre()} está tratando de escapar."

    def accion(self):
        return f"{self.get_nombre()} planea su próximo movimiento criminal."

# Uso del sistema
def main():
    # Crear personajes
    policia = Policia("Oficial Pérez", "Teniente")
    victima = Victima("María López", "asustada")
    delincuente = Delincuente("Carlos García", "robo")

    # Acciones generales
    print(policia.accion())
    print(victima.accion())
    print(delincuente.accion())
    print()

    # Interacciones entre personajes
    print(victima.pedir_ayuda())
    print(delincuente.cometer_delito())
    print(policia.arrestar(delincuente))
    print(policia.proteger(victima))

if __name__ == "__main__":
    main()
