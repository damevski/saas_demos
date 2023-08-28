from flask import Flask, jsonify, request
app = Flask(__name__)

# Sample data
tasks = [
    {"id": 1, "title": "wash car", "done": False},
    {"id": 2, "title": "clean desk", "done": True},
    {"id": 3, "title": "eat snack", "done": False}
]

# Endpoint 1: Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

# Endpoint 2: Get a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        return jsonify({"task": task})
    else:
        return jsonify({"error": "Task not found"}), 404

# Endpoint 3: Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = {
        "id": len(tasks) + 1,
        "title": request.json.get('title'),
        "done": False
    }
    tasks.append(new_task)
    return jsonify({"message": "Task created", "task": new_task}), 201

if __name__ == '__main__':
    app.run(debug=True)
