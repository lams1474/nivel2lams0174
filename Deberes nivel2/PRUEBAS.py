class DatabaseConnection:
    """
    Clase que simula la gestión de una conexión a una base de datos utilizando constructores y destructores.
    """

    def __init__(self, db_name):
        """
        Constructor de la clase. Inicializa los atributos y simula la apertura de una conexión a la base de datos.
        :param db_name: Nombre de la base de datos a la que se conecta.
        """
        self.db_name = db_name
        self.connected = False
        print(f"Inicializando conexión para la base de datos: {self.db_name}")
        self.connect()

    def connect(self):
        """
        Método para simular la conexión a la base de datos.
        """
        if not self.connected:
            self.connected = True
            print(f"Conexión establecida con la base de datos: {self.db_name}")

    def disconnect(self):
        """
        Método para simular la desconexión de la base de datos.
        """
        if self.connected:
            self.connected = False
            print(f"Conexión cerrada con la base de datos: {self.db_name}")

    def __del__(self):
        """
        Destructor de la clase. Se asegura de cerrar la conexión cuando el objeto es eliminado.
        """
        print(f"Destruyendo objeto DatabaseConnection para: {self.db_name}")
        self.disconnect()


# Bloque principal para demostrar el uso de constructores y destructores.
if __name__ == "__main__":
    # Crear un objeto de la clase DatabaseConnection
    db_connection = DatabaseConnection("BaseDeDatos_Ejemplo")

    # Realizar operaciones (simuladas) con la base de datos
    print("Realizando operaciones con la base de datos...")

    # Eliminar manualmente el objeto para llamar al destructor
    del db_connection

    print("Fin del programa.")
