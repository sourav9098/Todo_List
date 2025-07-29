from flask import Flask, render_template, request, redirect, jsonify
from db_config import get_connection

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    content = request.form['content']
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (content) VALUES (%s)", (content,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    new_content = request.form['new_content']
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET content = %s WHERE id = %s", (new_content, id))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)