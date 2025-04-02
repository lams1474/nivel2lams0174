import tkinter as tk
from tkinter import messagebox, ttk


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x400")

        # Configurar el estilo
        self.style = ttk.Style()
        self.style.configure("Completed.TLabel", foreground="gray", font=('Arial', 10, 'overstrike'))
        self.style.configure("Pending.TLabel", foreground="black", font=('Arial', 10))

        # Crear widgets
        self.create_widgets()

        # Configurar atajos de teclado
        self.setup_keyboard_shortcuts()

        # Lista de tareas
        self.tasks = []

    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Campo de entrada para nuevas tareas
        self.task_entry = ttk.Entry(main_frame, width=40)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5, sticky=tk.EW)
        self.task_entry.focus()

        # Botón para añadir tarea
        add_button = ttk.Button(main_frame, text="Añadir (Enter)", command=self.add_task)
        add_button.grid(row=0, column=1, padx=5, pady=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(main_frame, height=15, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.NSEW)

        # Scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        scrollbar.grid(row=1, column=2, sticky=tk.NS)
        self.task_listbox.config(yscrollcommand=scrollbar.set)

        # Frame para botones de acción
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=3, pady=10)

        # Botón para marcar como completada
        complete_button = ttk.Button(button_frame, text="Completar (C)", command=self.mark_completed)
        complete_button.pack(side=tk.LEFT, padx=5)

        # Botón para eliminar tarea
        delete_button = ttk.Button(button_frame, text="Eliminar (D)", command=self.delete_task)
        delete_button.pack(side=tk.LEFT, padx=5)

        # Configurar pesos para el grid
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)

    def setup_keyboard_shortcuts(self):
        # Añadir tarea con Enter
        self.root.bind('<Return>', lambda event: self.add_task())

        # Marcar como completada con C
        self.root.bind('<c>', lambda event: self.mark_completed())
        self.root.bind('<C>', lambda event: self.mark_completed())

        # Eliminar tarea con D o Delete
        self.root.bind('<d>', lambda event: self.delete_task())
        self.root.bind('<D>', lambda event: self.delete_task())
        self.root.bind('<Delete>', lambda event: self.delete_task())

        # Cerrar aplicación con Escape
        self.root.bind('<Escape>', lambda event: self.root.destroy())

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "completed": False})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea válida.")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_task_list()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_text = task["text"]
            if task["completed"]:
                self.task_listbox.insert(tk.END, task_text)
                self.task_listbox.itemconfig(tk.END, {'fg': 'gray'})
            else:
                self.task_listbox.insert(tk.END, task_text)
                self.task_listbox.itemconfig(tk.END, {'fg': 'black'})


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()