from flask import Flask, render_template, request, redirect, url_for, flash
from task_operations import (
    add_task, update_task, delete_task, mark_task_completed,
    search_tasks, filter_tasks_by_status
)
from db import connect
from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generates a new key each time the app runs  # Required for flash messages

# Function to fetch all tasks from the database
def get_all_tasks():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# Home route to show all tasks
@app.route('/')
def index():
    tasks = get_all_tasks()
    return render_template('index.html', tasks=tasks)

# Add new task
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        add_task(title, description, due_date)
        flash(' Task added successfully!')
        return redirect(url_for('index'))
    return render_template('add_task.html')

# Delete a task
@app.route('/delete/<int:task_id>')
def delete(task_id):
    delete_task(task_id)
    flash(' Task deleted successfully!')
    return redirect(url_for('index'))

# Mark task as completed
@app.route('/complete/<int:task_id>')
def complete(task_id):
    mark_task_completed(task_id)
    flash(' Task marked as completed!')
    return redirect(url_for('index'))

# Search tasks
@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    results = search_tasks(keyword)
    return render_template('index.html', tasks=results)

# Filter tasks by status (Pending / Completed)
@app.route('/filter/<status>')
def filter_status(status):
    tasks = filter_tasks_by_status(status)
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
