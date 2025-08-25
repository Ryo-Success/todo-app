# todo.py
tasks = []

def add_task(task, done=False):
    tasks.append({"task": task, "done": done})
    print(f"Added task: {task}")
    return tasks

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def show_tasks():
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. {task['task']} [{status}]")
    print("=== Message from main branch! ===")
    # 追加メッセージの修正
    print("=== hello from feature branch! ===")
    # ↓hotfixでは不要なので削除又は修正
    print("=== hotfix: 修正済メッセージ ===")
    # show_tasksにウェルカムメッセージを追加
    print("=== Welcome to ToDo App! ===")

if __name__ == "__main__":
    add_task("Git学習を始める")
    add_task("ToDoアプリを作る", done=True)
    show_tasks()
    delete_task(0)
    show_tasks()