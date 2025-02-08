# Programación Tradicional - Promedio Semanal del Clima

def ingresar_temperaturas():
    """
    Función para ingresar las temperaturas diarias.
    Retorna una lista con 7 temperaturas (una por cada día de la semana).
    """
    temperaturas = []
    print("Ingresa las temperaturas diarias:")
    for i in range(7):
        temp = float(input(f"Día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """
    Función para calcular el promedio semanal.
    """
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

def main():
    """
    Función principal que organiza la ejecución del programa.
    """
    print("Cálculo del Promedio Semanal del Clima - Programación Tradicional")
    temperaturas = ingresar_temperaturas()  # Entrada de datos
    promedio = calcular_promedio(temperaturas)  # Cálculo del promedio
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()

