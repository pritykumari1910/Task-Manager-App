# # db.py

# import sqlite3

# def connect():
#     return sqlite3.connect('tasks.db')

# def init_db():
#     conn = connect()
#     cursor = conn.cursor()

#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS tasks (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             title TEXT NOT NULL,
#             description TEXT,
#             due_date TEXT,
#             status TEXT DEFAULT 'Pending'
#         )
#     ''')

#     conn.commit()
#     conn.close()



import sqlite3

def connect():
    conn = sqlite3.connect('tasks.db')
    return conn

def init_db():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT,
                        due_date TEXT,
                        status TEXT DEFAULT 'Pending'
                    )''')
    conn.commit()
    conn.close()
