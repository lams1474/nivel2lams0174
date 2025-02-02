import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Semana2/1.1. Tipos de Datos e Identificadores/Nomenclatura en Python tarea1.py',
        '2': 'Semana3/Programación Orientada a Objetos (POO) semana3.py/Programación Tradicional semana 3.py',
        '3': 'Semana4/Calculadorade Área Figuras Geométricas semana4.py',
        '4': 'Semana5/Sistema de Registrode Notas semana5.py',
        '5': 'Semana6/Sistema de Gestión d la Biblioteca  semana6.py',
        '6': 'Semana7/Clas CuentaBancaria tarea7.py',
        '7': 'Zejemplosvarios20/clae libro.py/Control de Conexiones de Base de Datos.py/Código Python.py/EJEMPLO AUTO CLASE 7.py/Gestión de Archivos.py/Gestión de Procesos Temporales.py/Gestión de una Cola de Tareas.py/Gestión de vehículos concesionario.py/Personaje basico.py/Policia victima y delincuente.py/Programación Orientada a Objetos (POO) semana3.py/PRUEBAS.py/Tecnicas de Programacion.py',

        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()