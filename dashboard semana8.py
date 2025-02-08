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
        '1': 'Deberes nivel2/Semana2/1.1. Tipos de Datos e Identificadores/Nomenclatura en Python tarea1.py',
        '2': 'Deberes nivel2/Semana3/1.2. SEMANA 3/Programación Orientada a Objetos (POO) semana3.py/Programación Tradicional semana 3.py',
        '3': 'Deberes nivel2/Semana4/1.1. Tipos de Datos e Identificadores/Nomenclatura en Python tarea1.py',
        '4': 'Deberes nivel2/Semana5/1.1. Tipos de Datos e Identificadores/Nomenclatura en Python tarea1.py',
        '5': 'Deberes nivel2/Semana6/1.1. Tipos de Datos e Identificadores/Nomenclatura en Python tarea1.py',
        '6': 'Deberes nivel2/Semana7/1.1. Tipos de Datos e Identificadores/Nomenclatura en Python tarea1.py',
        '7': 'Deberes nivel2/Semana8/1.1. Tipos de Datos e Identificadores/Nomenclatura en Python tarea1.py',


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