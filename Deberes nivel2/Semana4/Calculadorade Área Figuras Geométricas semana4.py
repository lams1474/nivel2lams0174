# Programa para calcular el área de figuras geométricas
# Permite al usuario elegir entre círculo, rectángulo o triángulo y calcular su área.

import math


def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * radio ** 2


def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo dados su base y altura."""
    return base * altura


def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo dados su base y altura."""
    return (base * altura) / 2


if __name__ == "__main__":
    print("Calculadora de áreas:")
    print("1. Círculo")
    print("2. Rectángulo")
    print("3. Triángulo")

    opcion = int(input("Elija una figura (1-3): "))

    if opcion == 1:
        radio = float(input("Ingrese el radio del círculo: "))
        area = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area:.2f}")
    elif opcion == 2:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = calcular_area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area:.2f}")
    elif opcion == 3:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo es: {area:.2f}")
    else:
        print("Opción no válida.")