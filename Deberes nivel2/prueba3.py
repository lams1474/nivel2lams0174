import logging

# Configurar logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')


class RecursoComputo:
    """Clase que simula la gestión de recursos computacionales"""

    def __init__(self, nombre, capacidad_maxima):
        """Constructor que inicializa el recurso"""
        self.nombre = nombre
        self.capacidad_maxima = capacidad_maxima
        self.uso_actual = 0
        logging.info(f"Recurso {nombre} inicializado")

    def asignar(self, cantidad):
        """Asigna recursos"""
        if self.uso_actual + cantidad <= self.capacidad_maxima:
            self.uso_actual += cantidad
            logging.info(f"Asignados {cantidad} de {self.nombre}")
            return True
        logging.warning(f"No se pueden asignar {cantidad} de {self.nombre}")
        return False

    def liberar(self, cantidad):
        """Libera recursos"""
        self.uso_actual = max(0, self.uso_actual - cantidad)
        logging.info(f"Liberados {cantidad} de {self.nombre}")

    def __del__(self):
        """Destructor que libera recursos"""
        logging.info(f"Recurso {self.nombre} completamente liberado")


class GestorRecursos:
    """Administrador de múltiples recursos"""

    def __init__(self):
        """Inicializa diferentes tipos de recursos"""
        # Usar valores seguros en lugar de cálculos directos
        self.cpu = RecursoComputo("CPU", 100)  # Porcentaje de uso
        self.memoria = RecursoComputo("Memoria", 8192)  # MB

    def __del__(self):
        """Limpieza final de recursos"""
        logging.info("Gestor de recursos finalizado")


def main():
    # Demostración de uso de recursos
    gestor = GestorRecursos()

    # Simular asignación y uso de recursos
    gestor.cpu.asignar(50)
    gestor.memoria.asignar(500)

    # Los destructores se llamarán automáticamente
    logging.info("Demostración completada")


if __name__ == "__main__":
    main()
