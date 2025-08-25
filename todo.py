# todo.py
tasks = []

def add_task(task, done=False):
    tasks.append({"task": task, "done": done})

def delete_task(index):
    if 0 <= index < len(tasks):        
        tasks.pop(index)

def show_tasks():
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. {task['task']} [{status}]")
    print(f"=== 合計 {len(tasks)} 件のタスクがあります ===")

if __name__ == "__main__":
    add_task("Git学習を始める")
    add_task("ToDoアプリを作る", done=True)
    delete_task(0)
    show_tasks()
