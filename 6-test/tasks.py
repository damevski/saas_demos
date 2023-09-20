import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPDigestAuth


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tasks.sqlite')
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'UNguessable'
auth = HTTPDigestAuth()

USERS = {
    "rodney": "go_rams"
}

@auth.get_password
def get_pw(username):
    if username in USERS:
        return USERS.get(username)
    return None

# Task Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)

# Endpoint 1: Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    task_list = [{"id": task.id, "title": task.title, "done": task.done} for task in tasks]
    return jsonify({"tasks": task_list})

# Endpoint 2: Get a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    if task:
        return jsonify({"task": {"id": task.id, "title": task.title, "done": task.done}})
    else:
        return jsonify({"error": "Task not found"}), 404

# Endpoint 3: Create a new task
@app.route('/tasks', methods=['POST'])
@auth.login_required
def create_task():
    data = request.json
    if "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    new_task = Task(title=data['title'], done=False)
    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message": "Task created", "task": {"id": new_task.id, "title": new_task.title, "done": new_task.done}}), 201

if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)
