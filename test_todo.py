from todo import TodoList

def test_add_task():
    todo = TodoList()
    todo.add("Comprar leche")
    assert "Comprar leche" in todo.tasks

def test_remove_task():
    todo = TodoList()
    todo.add("Lavar ropa")
    todo.remove("Lavar ropa")
    assert "Lavar ropa" not in todo.tasks
