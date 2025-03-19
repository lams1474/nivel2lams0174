import tkinter as tk

def agregar_item():
    """Agrega el texto del campo de texto a la lista."""
    item = entrada.get()
    if item:  # Verifica que el campo de texto no esté vacío
        lista.insert(tk.END, item)
        entrada.delete(0, tk.END)  # Limpia el campo de texto

def limpiar_lista():
    """Limpia todos los elementos de la lista."""
    lista.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Mi Aplicación GUI")

# Componentes GUI
etiqueta = tk.Label(ventana, text="Ingrese información:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_item)
boton_agregar.pack()

lista = tk.Listbox(ventana)
lista.pack()

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
