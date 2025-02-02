# Programación Orientada a Objetos (POO) - Promedio Semanal del Clima

class ClimaSemanal:
    """
    Clase que representa la información diaria del clima.
    """
    def __init__(self):
        self.temperaturas = []  # Lista para almacenar las temperaturas

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas diarias.
        """
        print("Ingresa las temperaturas diarias:")
        for i in range(7):
            temp = float(input(f"Día {i+1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método para calcular el promedio semanal de temperaturas.
        """
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

def main():
    """
    Función principal que organiza la ejecución del programa.
    """
    print("Cálculo del Promedio Semanal del Clima - Programación Orientada a Objetos")
    clima = ClimaSemanal()  # Instancia de la clase ClimaSemanal
    clima.ingresar_temperaturas()  # Ingreso de datos mediante el método
    promedio = clima.calcular_promedio()  # Cálculo del promedio mediante el método
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
