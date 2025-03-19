import tkinter as tk
from tkinter import ttk, messagebox
import calendar
from tkcalendar import Calendar
import datetime

class AgendaApp:
    def __init__(self, root):
        """
        Inicializa la aplicación de Agenda.

        Args:
            root (tk.Tk): La ventana principal de la aplicación.
        """
        self.root = root
        self.root.title("Mi Agenda Personal")

        # Variables para almacenar los datos del evento
        self.fecha_seleccionada = tk.StringVar()
        self.hora_ingresada = tk.StringVar()
        self.descripcion_ingresada = tk.StringVar()

        # Diseño de la Interfaz
        self.create_widgets()

    def create_widgets(self):
        """
        Crea y posiciona los widgets en la ventana, utilizando Frames para organizar la interfaz.
        """

        # Frame para la Visualización de Eventos (TreeView)
        frame_eventos = ttk.Frame(self.root, padding="10")
        frame_eventos.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame_eventos, text="Eventos Programados:").pack()

        self.treeview = ttk.Treeview(frame_eventos, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.treeview.heading("Fecha", text="Fecha")
        self.treeview.heading("Hora", text="Hora")
        self.treeview.heading("Descripción", text="Descripción")
        self.treeview.pack(fill=tk.BOTH, expand=True)

        # Frame para la Entrada de Datos
        frame_entrada = ttk.Frame(self.root, padding="10")
        frame_entrada.pack(fill=tk.X)

        ttk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, sticky=tk.W)

        # DatePicker
        self.date_button = ttk.Button(frame_entrada, text="Seleccionar Fecha", command=self.open_calendar)
        self.date_button.grid(row=0, column=1, sticky=tk.W, padx=5)
        self.fecha_label = ttk.Label(frame_entrada, textvariable=self.fecha_seleccionada)
        self.fecha_label.grid(row=0, column=2, sticky=tk.W, padx=5)


        ttk.Label(frame_entrada, text="Hora:").grid(row=1, column=0, sticky=tk.W)
        ttk.Entry(frame_entrada, textvariable=self.hora_ingresada).grid(row=1, column=1, sticky=tk.W)

        ttk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, sticky=tk.W)
        ttk.Entry(frame_entrada, textvariable=self.descripcion_ingresada, width=40).grid(row=2, column=1, sticky=tk.W)

        # Frame para los Botones de Acción
        frame_botones = ttk.Frame(self.root, padding="10")
        frame_botones.pack(fill=tk.X)

        ttk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Salir", command=self.root.destroy).pack(side=tk.RIGHT, padx=5)


    def open_calendar(self):
        """Abre la ventana del calendario para seleccionar una fecha."""
        def set_date():
            """Obtiene la fecha seleccionada del calendario y actualiza la etiqueta."""
            self.fecha_seleccionada.set(cal.selection_get().strftime("%Y-%m-%d"))  # Formatea la fecha
            top.destroy()

        top = tk.Toplevel(self.root)
        cal = Calendar(top, font="Arial 10", selectmode='day', cursor="hand1")
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="Seleccionar", command=set_date).pack()


    def agregar_evento(self):
        """Agrega un nuevo evento a la Treeview con la información ingresada por el usuario."""
        fecha = self.fecha_seleccionada.get()
        hora = self.hora_ingresada.get()
        descripcion = self.descripcion_ingresada.get()

        # Validar que todos los campos estén completos
        if not (fecha and hora and descripcion):
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        self.treeview.insert("", tk.END, values=(fecha, hora, descripcion))

        # Limpiar los campos después de agregar el evento
        self.fecha_seleccionada.set("")
        self.hora_ingresada.set("")
        self.descripcion_ingresada.set("")

    def eliminar_evento(self):
        """Elimina el evento seleccionado en la Treeview, con confirmación del usuario."""
        seleccion = self.treeview.selection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor, seleccione un evento para eliminar.")
            return

        # Diálogo de confirmación
        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este evento?"):
            self.treeview.delete(seleccion)


# Función principal para ejecutar la aplicación
def main():
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()