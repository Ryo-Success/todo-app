# todo.py
tasks = []

def add_task():
    tasks.append(task)

def show_tasks():
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

if __name__ == "main":
    add_task("Git学習を始める")
    add_task("ToDoアプリを作る")
    show_tasks