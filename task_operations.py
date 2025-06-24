# # task_operations.py

from db import connect

def add_task(title, description, due_date):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO tasks (title, description, due_date)
        VALUES (?, ?, ?)
    ''', (title, description, due_date))

    conn.commit()
    conn.close()
    print("Task added successfully!")

def view_tasks():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()

    if not tasks:
        print("No tasks found.")
    else:
        print("\nAll Tasks:")
        print("-" * 50)
        for task in tasks:
            print(f"ID       : {task[0]}")
            print(f"Title    : {task[1]}")
            print(f"Desc     : {task[2]}")
            print(f"Due Date : {task[3]}")
            print(f"Status   : {task[4]}")
            print("-" * 50)

    conn.close()








def update_task(task_id, new_title, new_description, new_due_date):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE tasks
        SET title = ?, description = ?, due_date = ?
        WHERE id = ?
    ''', (new_title, new_description, new_due_date, task_id))

    conn.commit()
    conn.close()
    print("Task updated successfully!")

def delete_task(task_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    print(" Task deleted successfully!")

def mark_task_completed(task_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE tasks
        SET status = 'Completed'
        WHERE id = ?
    ''', (task_id,))
    conn.commit()
    conn.close()
    print(" Task marked as completed!")



# def search_tasks(keyword):
#     conn = connect()
#     cursor = conn.cursor()

#     cursor.execute("SELECT * FROM tasks WHERE title LIKE ?", ('%' + keyword + '%',))
#     tasks = cursor.fetchall()
#     conn.close()

#     print("\n🔍 Search Results:")
#     if not tasks:
#         print("No tasks found.")
#     else:
#         for task in tasks:
#             print(f"ID: {task[0]} | Title: {task[1]} | Status: {task[4]}")

# def filter_tasks_by_status(status):
#     conn = connect()
#     cursor = conn.cursor()

#     cursor.execute("SELECT * FROM tasks WHERE status = ?", (status,))
#     tasks = cursor.fetchall()
#     conn.close()

#     print(f"\n📋 Tasks with status: {status}")
#     if not tasks:
#         print("No tasks found.")
#     else:
#         for task in tasks:
#             print(f"ID: {task[0]} | Title: {task[1]} | Status: {task[4]}")


# Inside task_operations.py

def search_tasks(keyword):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE title LIKE ?", ('%' + keyword + '%',))
    tasks = cursor.fetchall()
    conn.close()
    return tasks  # ✅ FIX: return the search results

def filter_tasks_by_status(status):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE status = ?", (status,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks  # ✅ FIX: return the filtered results
