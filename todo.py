class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, task)
        """Agrega una tarea al listado"""
        self.tasks.append(task)
        return True

    def remove(self, task):
        """Elimina una tarea del listado"""
        if task in self.tasks:
            self.tasks.remove(task)
            return True
        return False

    def list_tasks(self):
        """Muestra todas las tareas"""
        return self.tasks


if __name__ == "__main__":
    todo = TodoList()
    while True:
        print("\n=== To-Do List ===")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Ver tareas")
        print("4. Salir")
        option = input("Selecciona una opción: ")

        if option == "1":
            t = input("Nueva tarea: ")
            todo.add(t)
        elif option == "2":
            t = input("Tarea a eliminar: ")
            todo.remove(t)
        elif option == "3":
            print("Tareas actuales:", todo.list_tasks())
        elif option == "4":
            break
        else:
            print("Opción inválida.")
