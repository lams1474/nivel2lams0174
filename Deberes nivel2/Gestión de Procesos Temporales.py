import time
import logging
from concurrent.futures import ThreadPoolExecutor

# Configurar logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')


class ProcesoTemporal:
    """Gestiona procesos con tiempo de vida limitado"""

    def __init__(self, nombre, duracion):
        """
        Constructor que inicializa y comienza un proceso

        Args:
            nombre (str): Nombre del proceso
            duracion (int): Duración en segundos
        """
        self.nombre = nombre
        self.duracion = duracion
        self.completado = False
        logging.info(f"Proceso {nombre} inicializado")

    def ejecutar(self):
        """Método para ejecución del proceso"""
        try:
            logging.info(f"Iniciando {self.nombre}")
            time.sleep(self.duracion)
            logging.info(f"Proceso {self.nombre} completado")
            self.completado = True
        except Exception as e:
            logging.error(f"Error en {self.nombre}: {e}")

    def __del__(self):
        """Destructor que verifica estado del proceso"""
        if not self.completado:
            logging.warning(f"Proceso {self.nombre} no completado")


def main():
    # Crear procesos temporales
    procesos = [
        ProcesoTemporal("Proceso1", 2),
        ProcesoTemporal("Proceso2", 3),
        ProcesoTemporal("Proceso3", 1)
    ]

    # Usar ThreadPoolExecutor para manejar múltiples procesos
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Enviar procesos a ejecución
        futures = [executor.submit(proceso.ejecutar) for proceso in procesos]

        # Esperar a que todos los procesos terminen
        for future in futures:
            future.result()

    logging.info("Todos los procesos completados")


if __name__ == "__main__":
    main()