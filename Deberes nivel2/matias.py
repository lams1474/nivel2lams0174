from abc import ABC, abstractmethod  # Para clases abstractas


# Clase base abstracta: Abstracción
class Vehiculo(ABC):
    def __init__(self, marca, modelo, precio):
        self.__marca = marca  # Encapsulamiento
        self.__modelo = modelo  # Encapsulamiento
        self.__precio = precio  # Encapsulamiento

    # Métodos getters y setters para el encapsulamiento
    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    # Método abstracto (debe ser implementado por las clases hijas)
    @abstractmethod
    def mostrar_informacion(self):
        pass


# Clase hija: Coche (Herencia y Polimorfismo)
class Coche(Vehiculo):
    def __init__(self, marca, modelo, precio, puertas):
        super().__init__(marca, modelo, precio)
        self.__puertas = puertas  # Atributo específico de Coche

    def mostrar_informacion(self):
        return f"Coche: {self.get_marca()} {self.get_modelo()} - ${self.get_precio()} - Puertas: {self.__puertas}"


# Clase hija: Moto (Herencia y Polimorfismo)
class Moto(Vehiculo):
    def __init__(self, marca, modelo, precio, cilindrada):
        super().__init__(marca, modelo, precio)
        self.__cilindrada = cilindrada  # Atributo específico de Moto

    def mostrar_informacion(self):
        return f"Moto: {self.get_marca()} {self.get_modelo()} - ${self.get_precio()} - Cilindrada: {self.__cilindrada}cc"


# Clase hija: Camion (Herencia y Polimorfismo)
class Camion(Vehiculo):
    def __init__(self, marca, modelo, precio, capacidad_carga):
        super().__init__(marca, modelo, precio)
        self.__capacidad_carga = capacidad_carga  # Atributo específico de Camion

    def mostrar_informacion(self):
        return f"Camion: {self.get_marca()} {self.get_modelo()} - ${self.get_precio()} - Capacidad: {self.__capacidad_carga}kg"


# Uso del sistema
def main():
    # Crear objetos de diferentes tipos de vehículos
    coche = Coche("Toyota", "Corolla", 20000, 4)
    moto = Moto("Honda", "CBR", 15000, 600)
    camion = Camion("Volvo", "FH", 50000, 20000)

    # Lista de vehículos (Polimorfismo: todos son Vehiculos)
    vehiculos = [coche, moto, camion]

    # Mostrar información de cada vehículo
    for vehiculo in vehiculos:
        print(vehiculo.mostrar_informacion())


if __name__ == "__main__":
    main()
