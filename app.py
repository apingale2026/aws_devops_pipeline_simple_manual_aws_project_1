from flask import Flask, request, jsonify
import os

app = Flask(__name__)
TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(load_tasks())

@app.route("/tasks", methods=["POST"])
def add_task():
    task = request.json.get("task")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    return jsonify({"message": "Task added", "tasks": tasks})

@app.route("/tasks/<int:idx>", methods=["DELETE"])
def delete_task(idx):
    tasks = load_tasks()
    if 0 <= idx < len(tasks):
        tasks.pop(idx)
        save_tasks(tasks)
        return jsonify({"message": "Task deleted", "tasks": tasks})
    return jsonify({"error": "Invalid index"}), 400

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
