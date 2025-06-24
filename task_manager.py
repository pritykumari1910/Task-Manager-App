from db import init_db
from task_operations import (
    add_task,
    view_tasks,
    update_task,
    delete_task,
    mark_task_completed,
    search_tasks,
    filter_tasks_by_status
)

def menu():
    while True:
        print("\n===== Task Manager Menu =====")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        print("7. 🔍 Search Task by Title")
        print("8. 📋 Filter Tasks by Status")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)

        elif choice == '2':
            view_tasks()

        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            new_title = input("New title: ")
            new_description = input("New description: ")
            new_due_date = input("New due date (YYYY-MM-DD): ")
            update_task(task_id, new_title, new_description, new_due_date)

        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)

        elif choice == '5':
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_task_completed(task_id)

        elif choice == '6':
            print("👋 Exiting Task Manager. Goodbye!")
            break

        elif choice == '7':
            keyword = input("Enter keyword to search in task titles: ")
            search_tasks(keyword)

        elif choice == '8':
            status = input("Enter status to filter by (Pending/Completed): ").capitalize()
            if status in ["Pending", "Completed"]:
                filter_tasks_by_status(status)
            else:
                print("❌ Invalid status entered!")

        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    init_db()
    menu()
