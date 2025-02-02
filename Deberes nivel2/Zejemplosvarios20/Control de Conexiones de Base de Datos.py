import sqlite3
import logging
import os

# Configurar logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')


class ConexionBD:
    """Gestiona conexiones a base de datos"""

    def __init__(self, nombre_bd):
        """
        Constructor que establece conexión a base de datos

        Args:
            nombre_bd (str): Nombre del archivo de base de datos
        """
        try:
            # Asegurar directorio de base de datos
            directorio = os.path.dirname(nombre_bd)
            if directorio:
                os.makedirs(directorio, exist_ok=True)

            self.conexion = sqlite3.connect(nombre_bd)
            self.cursor = self.conexion.cursor()
            logging.info(f"Conexión establecida a {nombre_bd}")
        except sqlite3.Error as e:
            logging.error(f"Error al conectar: {e}")
            raise

    def ejecutar_consulta(self, consulta, parametros=None):
        """Ejecuta una consulta en la base de datos"""
        try:
            if parametros:
                self.cursor.execute(consulta, parametros)
            else:
                self.cursor.execute(consulta)
            self.conexion.commit()
            logging.info("Consulta ejecutada exitosamente")
        except sqlite3.Error as e:
            logging.error(f"Error en consulta: {e}")
            self.conexion.rollback()

    def __del__(self):
        """Destructor que cierra la conexión"""
        try:
            if hasattr(self, 'conexion'):
                self.conexion.close()
                logging.info("Conexión a base de datos cerrada")
        except Exception as e:
            logging.error(f"Error al cerrar conexión: {e}")


def main():
    # Crear y usar conexión
    try:
        # Usar un path temporal para la base de datos
        ruta_bd = 'temp/ejemplo.db'
        bd = ConexionBD(ruta_bd)

        # Crear tabla de ejemplo
        bd.ejecutar_consulta('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                email TEXT
            )
        ''')

        # Insertar datos
        bd.ejecutar_consulta(
            'INSERT INTO usuarios (nombre, email) VALUES (?, ?)',
            ('Juan Pérez', 'juan@example.com')
        )

    except Exception as e:
        logging.error(f"Ocurrió un error: {e}")


if __name__ == "__main__":
    main()