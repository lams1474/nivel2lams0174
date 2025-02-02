from abc import ABC, abstractmethod

# Clase base abstracta: Abstracción
class Personaje(ABC):
    def __init__(self, nombre, salud, fuerza, nivel):
        self.__nombre = nombre    # Encapsulamiento
        self.__salud = salud      # Encapsulamiento
        self.__fuerza = fuerza    # Encapsulamiento
        self.__nivel = nivel      # Encapsulamiento

    def get_nombre(self):
        return self.__nombre

    def get_salud(self):
        return self.__salud

    def set_salud(self, salud):
        self.__salud = salud

    def get_fuerza(self):
        return self.__fuerza

    def get_nivel(self):
        return self.__nivel

    @abstractmethod
    def atacar(self):
        pass

# Clase hija: Guerrero (Herencia y Polimorfismo)
class Guerrero(Personaje):
    def atacar(self):
        return f"{self.get_nombre()} ataca con su espada causando {self.get_fuerza() * self.get_nivel()} de daño."

# Clase hija: Mago (Herencia y Polimorfismo)
class Mago(Personaje):
    def atacar(self):
        return f"{self.get_nombre()} lanza un hechizo causando {self.get_fuerza() * 1.5 * self.get_nivel()} de daño."

# Clase hija: Arquero (Herencia y Polimorfismo)
class Arquero(Personaje):
    def atacar(self):
        return f"{self.get_nombre()} dispara una flecha causando {self.get_fuerza() * self.get_nivel()} de daño."

# Uso del sistema
def main():
    guerrero = Guerrero("Thorgar", 100, 15, 5)
    mago = Mago("Merlin", 80, 10, 6)
    arquero = Arquero("Legolas", 90, 12, 4)

    personajes = [guerrero, mago, arquero]

    for personaje in personajes:
        print(personaje.atacar())

if __name__ == "__main__":
    main()
