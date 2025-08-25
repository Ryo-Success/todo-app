# todo.py
tasks = []

def add_task():
    tasks.append({"task":task, "done":done})

def delete_task():
    if 0 <= index < len(tasks):
        tasks.pop(index)

def show_tasks():
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. {task['task']} [{status}]")
    print("=== Message from main branch! ===")
    print("=== hello from feature branch! ===")

if __name__ == "main":
    add_task("Git学習を始める")
    add_task("ToDoアプリを作る", done=True)
    show_tasks
    delete_task(0)  # 最初のタスクを削除
    show_tasks()