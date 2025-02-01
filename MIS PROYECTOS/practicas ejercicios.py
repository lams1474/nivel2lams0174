import os
import sys
import subprocess
from datetime import datetime
from shutil import copy2

# Configuración personalizable del proyecto
ESTRUCTURA_PROYECTO = {
    'EJERCICIOS': ['basicos', 'intermedios', 'avanzados'],
    'PROYECTOS': ['individuales', 'grupales'],
    'RECURSOS': ['documentacion', 'ejemplos']
}


class DashboardPOO:
    def __init__(self):
        self.ruta_base = os.path.dirname(os.path.abspath(__file__))
        self.crear_estructura_inicial()
        self.historial_file = 'historial.log'
        self.backup_dir = 'backups'

    def crear_estructura_inicial(self):
        """Crea la estructura inicial de carpetas del proyecto."""
        try:
            for categoria, subcategorias in ESTRUCTURA_PROYECTO.items():
                for subcategoria in subcategorias:
                    ruta = os.path.join(self.ruta_base, categoria, subcategoria)
                    os.makedirs(ruta, exist_ok=True)
            print("Estructura de carpetas creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la estructura de carpetas: {e}")
            sys.exit(1)

    def mostrar_encabezado(self):
        """Muestra el encabezado del dashboard."""
        print("\n" + "=" * 50)
        print("Sistema de Gestión de Proyectos POO".center(50))
        print("=" * 50 + "\n")

    def mostrar_codigo(self, ruta_script):
        """Muestra el contenido de un script."""
        try:
            with open(ruta_script, 'r', encoding='utf-8') as archivo:
                codigo = archivo.read()
                print(f"\n--- Código de {os.path.basename(ruta_script)} ---\n")
                print(codigo)
                return codigo
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return None

    def ejecutar_codigo(self, ruta_script):
        """Ejecuta un script en una nueva ventana."""
        try:
            if os.name == 'nt':  # Windows
                subprocess.Popen(['cmd', '/k', 'python', ruta_script])
            else:  # Unix-based
                subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
            self.registrar_ejecucion(ruta_script, "Ejecutado exitosamente")
        except Exception as e:
            print(f"Error al ejecutar el código: {e}")
            self.registrar_ejecucion(ruta_script, f"Error: {e}")

    def registrar_ejecucion(self, script, resultado):
        """Registra las ejecuciones en el archivo de historial."""
        try:
            with open(self.historial_file, 'a', encoding='utf-8') as f:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                f.write(f"{timestamp} - Script: {script} - Resultado: {resultado}\n")
        except Exception as e:
            print(f"Error al registrar en el historial: {e}")

    def crear_backup(self, ruta_script):
        """Crea una copia de respaldo del script."""
        try:
            if not os.path.exists(self.backup_dir):
                os.makedirs(self.backup_dir)

            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            nombre_backup = f"{os.path.splitext(os.path.basename(ruta_script))[0]}_{timestamp}.py"
            ruta_backup = os.path.join(self.backup_dir, nombre_backup)

            copy2(ruta_script, ruta_backup)
            print(f"Backup creado: {nombre_backup}")
            return ruta_backup
        except Exception as e:
            print(f"Error al crear backup: {e}")
            return None

    def buscar_script(self, nombre):
        """Busca scripts por nombre en todas las carpetas."""
        resultados = []
        try:
            for root, _, files in os.walk(self.ruta_base):
                for file in files:
                    if file.endswith('.py') and nombre.lower() in file.lower():
                        resultados.append(os.path.join(root, file))
            return resultados
        except Exception as e:
            print(f"Error en la búsqueda: {e}")
            return []

    def mostrar_estadisticas(self):
        """Muestra estadísticas del sistema."""
        try:
            total_scripts = 0
            scripts_por_categoria = {}

            for root, _, files in os.walk(self.ruta_base):
                scripts = [f for f in files if f.endswith('.py')]
                categoria = os.path.basename(root)
                if scripts:
                    scripts_por_categoria[categoria] = len(scripts)
                    total_scripts += len(scripts)

            print("\nEstadísticas del Sistema:")
            print(f"Total de scripts: {total_scripts}")
            for categoria, cantidad in scripts_por_categoria.items():
                print(f"{categoria}: {cantidad} scripts")
        except Exception as e:
            print(f"Error al mostrar estadísticas: {e}")

    def mostrar_menu_principal(self):
        """Muestra el menú principal del dashboard."""
        while True:
            self.mostrar_encabezado()
            print("1. Ver Proyectos")
            print("2. Buscar Scripts")
            print("3. Ver Estadísticas")
            print("4. Ver Historial")
            print("0. Salir")

            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                self.mostrar_categorias()
            elif opcion == "2":
                nombre = input("Ingrese el nombre a buscar: ")
                resultados = self.buscar_script(nombre)
                if resultados:
                    print("\nScripts encontrados:")
                    for i, script in enumerate(resultados, 1):
                        print(f"{i}. {os.path.basename(script)}")
                    self.seleccionar_script_encontrado(resultados)
                else:
                    print("No se encontraron scripts.")
            elif opcion == "3":
                self.mostrar_estadisticas()
            elif opcion == "4":
                self.mostrar_historial()
            elif opcion == "0":
                print("\nSaliendo del sistema...")
                break
            else:
                print("\nOpción no válida.")

            input("\nPresione Enter para continuar...")

    def mostrar_categorias(self):
        """Muestra las categorías disponibles."""
        while True:
            print("\nCategorías disponibles:")
            categorias = list(ESTRUCTURA_PROYECTO.keys())
            for i, categoria in enumerate(categorias, 1):
                print(f"{i}. {categoria}")
            print("0. Volver")

            opcion = input("\nSeleccione una categoría: ")
            if opcion == "0":
                break
            try:
                indice = int(opcion) - 1
                if 0 <= indice < len(categorias):
                    self.mostrar_subcategorias(categorias[indice])
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")

    def mostrar_subcategorias(self, categoria):
        """Muestra las subcategorías de una categoría."""
        while True:
            print(f"\nSubcategorías de {categoria}:")
            subcategorias = ESTRUCTURA_PROYECTO[categoria]
            for i, subcategoria in enumerate(subcategorias, 1):
                print(f"{i}. {subcategoria}")
            print("0. Volver")

            opcion = input("\nSeleccione una subcategoría: ")
            if opcion == "0":
                break
            try:
                indice = int(opcion) - 1
                if 0 <= indice < len(subcategorias):
                    ruta = os.path.join(self.ruta_base, categoria, subcategorias[indice])
                    self.mostrar_scripts(ruta)
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")

    def mostrar_scripts(self, ruta):
        """Muestra los scripts disponibles en una ruta."""
        while True:
            scripts = [f for f in os.scandir(ruta) if f.is_file() and f.name.endswith('.py')]
            if not scripts:
                print("\nNo hay scripts en esta carpeta.")
                break

            print("\nScripts disponibles:")
            for i, script in enumerate(scripts, 1):
                print(f"{i}. {script.name}")
            print("0. Volver")

            opcion = input("\nSeleccione un script: ")
            if opcion == "0":
                break

            try:
                indice = int(opcion) - 1
                if 0 <= indice < len(scripts):
                    self.manejar_script(scripts[indice].path)
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")

    def manejar_script(self, ruta_script):
        """Maneja las operaciones disponibles para un script."""
        while True:
            print("\nOperaciones disponibles:")
            print("1. Ver código")
            print("2. Ejecutar")
            print("3. Crear backup")
            print("0. Volver")

            opcion = input("\nSeleccione una operación: ")
            if opcion == "1":
                self.mostrar_codigo(ruta_script)
            elif opcion == "2":
                self.ejecutar_codigo(ruta_script)
            elif opcion == "3":
                self.crear_backup(ruta_script)
            elif opcion == "0":
                break
            else:
                print("Opción no válida.")

    def mostrar_historial(self):
        """Muestra el historial de ejecuciones."""
        try:
            with open(self.historial_file, 'r', encoding='utf-8') as f:
                print("\nHistorial de ejecuciones:")
                print("=" * 50)
                contenido = f.read()
                print(contenido if contenido else "No hay registros en el historial.")
        except FileNotFoundError:
            print("\nNo hay historial de ejecuciones.")
        except Exception as e:
            print(f"Error al leer el historial: {e}")

    def seleccionar_script_encontrado(self, resultados):
        """Permite seleccionar y manejar un script de los resultados de búsqueda."""
        if resultados:
            opcion = input("\nSeleccione un script para manejar (0 para volver): ")
            try:
                indice = int(opcion) - 1
                if 0 <= indice < len(resultados):
                    self.manejar_script(resultados[indice])
            except ValueError:
                print("Opción no válida.")


def main():
    try:
        dashboard = DashboardPOO()
        dashboard.mostrar_menu_principal()
    except Exception as e:
        print(f"Error crítico: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
