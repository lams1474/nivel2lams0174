import tkinter as tk
from tkinter import ttk

class SimpleApp:
    def __init__(self, root):
        """
        Inicializa la aplicación GUI.

        Args:
            root (tk.Tk): La ventana principal de la aplicación.
        """
        self.root = root
        self.root.title("Mi Simple Aplicación GUI")  # Establece el título de la ventana

        # Variables para almacenar datos
        self.data = []
        self.text_input = tk.StringVar()

        # Diseño de la Interfaz
        self.create_widgets()

    def create_widgets(self):
        """
        Crea y posiciona los widgets en la ventana.
        """
        # Etiqueta para el campo de entrada
        ttk.Label(self.root, text="Ingresa texto:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        # Campo de texto
        self.entry = ttk.Entry(self.root, textvariable=self.text_input, width=30)
        self.entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.E)

        # Botón "Agregar"
        ttk.Button(self.root, text="Agregar", command=self.add_item).grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        # Lista/Tabla para mostrar datos
        self.listbox = tk.Listbox(self.root, width=40, height=10)
        self.listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Botón "Limpiar"
        ttk.Button(self.root, text="Limpiar", command=self.clear_list).grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def add_item(self):
        """
        Agrega el texto del campo de entrada a la lista y actualiza la Listbox.
        """
        text = self.text_input.get()  # Obtiene el texto del campo de entrada
        if text:  # Verifica que el texto no esté vacío
            self.data.append(text)  # Agrega el texto a la lista de datos
            self.listbox.insert(tk.END, text)  # Inserta el texto en la Listbox
            self.text_input.set("")  # Limpia el campo de entrada

    def clear_list(self):
        """
        Limpia la Listbox y la lista de datos.
        """
        self.listbox.delete(0, tk.END)  # Elimina todos los elementos de la Listbox
        self.data = []  # Limpia la lista de datos


# Función principal para ejecutar la aplicación
def main():
    root = tk.Tk()  # Crea la ventana principal
    app = SimpleApp(root)  # Crea una instancia de la clase SimpleApp
    root.mainloop()  # Inicia el bucle principal de la aplicación


if __name__ == "__main__":
    main()