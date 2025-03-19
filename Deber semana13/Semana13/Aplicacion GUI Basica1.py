import tkinter as tk
from tkinter import messagebox

# Función para agregar información a la lista
def agregar_info():
    info = entrada.get()
    if info:
        lista.insert(tk.END, info)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Campo Vacío", "Por favor, ingrese información antes de agregar.")

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)

# Creación de la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Creación de los componentes
etiqueta = tk.Label(ventana, text="Ingrese su información:")
entrada = tk.Entry(ventana, width=40)
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_info)
lista = tk.Listbox(ventana, width=50)
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)

# Disposición de los componentes en la ventana
etiqueta.pack(pady=10)
entrada.pack(pady=5)
boton_agregar.pack(pady=5)
lista.pack(pady=10)
boton_limpiar.pack(pady=5)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
