class FileManager:
    """
    Clase que gestiona la apertura y cierre de archivos.
    """
    def __init__(self, file_name, mode):
        """
        Constructor que inicializa la clase y abre un archivo en el modo especificado.
        :param file_name: Nombre del archivo.
        :param mode: Modo en el que se abrirá el archivo (lectura, escritura, etc.).
        """
        self.file_name = file_name
        self.mode = mode
        self.file = None
        print(f"Abriendo archivo: {self.file_name} en modo '{self.mode}'")
        self.open_file()

    def open_file(self):
        """
        Método para abrir el archivo.
        """
        try:
            self.file = open(self.file_name, self.mode)
            print(f"Archivo '{self.file_name}' abierto exitosamente.")
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")

    def write(self, content):
        """
        Método para escribir contenido en el archivo (si está en modo escritura).
        :param content: Contenido a escribir en el archivo.
        """
        if self.file and not self.file.closed:
            self.file.write(content)
            print(f"Escrito en el archivo: {content}")
        else:
            print("El archivo no está abierto o no es editable.")

    def __del__(self):
        """
        Destructor que asegura el cierre del archivo.
        """
        if self.file and not self.file.closed:
            self.file.close()
            print(f"Archivo '{self.file_name}' cerrado correctamente.")


# Bloque principal
if __name__ == "__main__":
    # Crear y gestionar un archivo
    manager = FileManager("archivo_ejemplo.txt", "w")
    manager.write("Esto es una línea de ejemplo.\n")
    del manager
    print("Fin del programa.")
