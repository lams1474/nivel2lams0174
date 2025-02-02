class TaskQueue:
    """
    Clase que gestiona una cola de tareas.
    """

    def __init__(self):
        """
        Constructor que inicializa una lista vacía para las tareas.
        """
        self.tasks = []
        print("Cola de tareas creada.")

    def add_task(self, task):
        """
        Método para agregar una tarea a la cola.
        :param task: Descripción de la tarea.
        """
        self.tasks.append(task)
        print(f"Tarea agregada: {task}")

    def process_tasks(self):
        """
        Método para procesar todas las tareas de la cola.
        """
        print("Procesando tareas...")
        while self.tasks:
            task = self.tasks.pop(0)
            print(f"Tarea completada: {task}")
        print("Todas las tareas han sido procesadas.")

    def __del__(self):
        """
        Destructor que procesa automáticamente las tareas restantes antes de eliminar el objeto.
        """
        if self.tasks:
            print("Procesando tareas pendientes antes de eliminar el objeto...")
            self.process_tasks()
        print("Cola de tareas destruida.")


# Bloque principal
if __name__ == "__main__":
    # Crear y gestionar una cola de tareas
    task_queue = TaskQueue()
    task_queue.add_task("Tarea 1: Configurar servidor.")
    task_queue.add_task("Tarea 2: Realizar pruebas.")
    task_queue.add_task("Tarea 3: Generar reporte.")

    # Eliminar manualmente el objeto
    del task_queue
    print("Fin del programa.")
