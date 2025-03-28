import tkinter as tk
from tkinter import messagebox

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Lista para almacenar las tareas
        self.tareas = []

        # Componentes de la interfaz
        self.entrada_tarea = tk.Entry(root, width=40)
        self.entrada_tarea.grid(row=0, column=0, padx=10, pady=10)
        self.entrada_tarea.bind("<Return>", self.agregar_tarea)  # Añadir tarea con Enter

        self.boton_agregar = tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea)
        self.boton_agregar.grid(row=0, column=1, padx=5, pady=10)

        self.lista_tareas = tk.Listbox(root, width=50)
        self.lista_tareas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.lista_tareas.bind("<Double-Button-1>", self.marcar_completada_doble_click) # Opcional

        self.boton_completada = tk.Button(root, text="Marcar como Completada", command=self.marcar_completada)
        self.boton_completada.grid(row=2, column=0, padx=5, pady=5)

        self.boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.grid(row=2, column=1, padx=5, pady=5)

        self.actualizar_lista()

    def agregar_tarea(self, event=None):
        """Añade una nueva tarea a la lista."""
        tarea = self.entrada_tarea.get()
        if tarea:
            self.tareas.append({"tarea": tarea, "completada": False})
            self.entrada_tarea.delete(0, tk.END)
            self.actualizar_lista()

    def marcar_completada(self):
        """Marca la tarea seleccionada como completada."""
        try:
            indice_seleccionado = self.lista_tareas.curselection()[0]
            self.tareas[indice_seleccionado]["completada"] = not self.tareas[indice_seleccionado]["completada"]
            self.actualizar_lista()
        except IndexError:
            messagebox.warning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    def marcar_completada_doble_click(self, event):
        """Marca la tarea seleccionada como completada con doble clic (opcional)."""
        self.marcar_completada()

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada de la lista."""
        try:
            indice_seleccionado = self.lista_tareas.curselection()[0]
            del self.tareas[indice_seleccionado]
            self.actualizar_lista()
        except IndexError:
            messagebox.warning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

    def actualizar_lista(self):
        """Actualiza la visualización de la lista de tareas."""
        self.lista_tareas.delete(0, tk.END)
        for tarea_info in self.tareas:
            tarea_texto = tarea_info["tarea"]
            if tarea_info["completada"]:
                tarea_texto = f"[Completada] {tarea_texto}"
            self.lista_tareas.insert(tk.END, tarea_texto)
            if tarea_info["completada"]:
                self.lista_tareas.itemconfig(self.lista_tareas.index(tk.END) - 1, {'fg': 'gray'}) # Opcional: texto gris para completadas
            else:
                self.lista_tareas.itemconfig(self.lista_tareas.index(tk.END) - 1, {'fg': 'black'})

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()