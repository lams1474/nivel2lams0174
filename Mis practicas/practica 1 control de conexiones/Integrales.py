import scipy.integrate as integrate
import numpy as np

# Función para evaluar la función ingresada por el usuario
def evaluar_funcion(x, funcion):
    return eval(funcion)

# Solicitar datos al usuario
print("Resolución de integrales definidas")
print("---------------------------------")

# Ingresar la función a integrar
funcion_str = input("Ingresa la función a integrar (usa 'x' como variable, ej: x**2 + np.sin(x)): ")

# Ingresar los límites de integración
a = float(input("Ingresa el límite inferior de integración (a): "))
b = float(input("Ingresa el límite superior de integración (b): "))

# Resolver la integral
try:
    resultado, error = integrate.quad(lambda x: evaluar_funcion(x, funcion_str), a, b)
    print("\nResultado de la integral:")
    print(f"El valor de la integral es: {resultado}")
    print(f"El error estimado es: {error}")
except Exception as e:
    print("\nError al calcular la integral. Verifica la función ingresada.")
    print(f"Detalles del error: {e}")