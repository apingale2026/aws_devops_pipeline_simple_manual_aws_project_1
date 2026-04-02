from flask import Flask, request, jsonify, Response
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

# ---------------- API ROUTES ----------------

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = load_tasks()
    return jsonify([{"id": i+1, "task": t} for i, t in enumerate(tasks)])

@app.route("/tasks", methods=["POST"])
def add_task():
    task = request.json.get("task")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    return jsonify([{"id": i+1, "task": t} for i, t in enumerate(tasks)])

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks()
    index = task_id - 1   # adjust for 1-based IDs
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        return jsonify([{"id": i+1, "task": t} for i, t in enumerate(tasks)])
    return jsonify({"error": "Invalid task id"}), 404

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    new_task = request.json.get("task")
    tasks = load_tasks()
    index = task_id - 1
    if 0 <= index < len(tasks):
        tasks[index] = new_task
        save_tasks(tasks)
        return jsonify([{"id": i+1, "task": t} for i, t in enumerate(tasks)])
    return jsonify({"error": "Invalid task id"}), 404

@app.route("/tasks/<int:task_id>/done", methods=["PATCH"])
def mark_done(task_id):
    tasks = load_tasks()
    index = task_id - 1
    if 0 <= index < len(tasks):
        tasks[index] = tasks[index] + " ✅"
        save_tasks(tasks)
        return jsonify([{"id": i+1, "task": t} for i, t in enumerate(tasks)])
    return jsonify({"error": "Invalid task id"}), 404

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

# ---------------- FRONTEND ----------------

@app.route("/")
def index():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>My To‑Do App</title>
      <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 5px 0; }
        button { margin-left: 10px; }
      </style>
    </head>
    <body>
      <h1>My Tasks</h1>
      <ul id="taskList"></ul>

      <h2>Add Task</h2>
      <input type="text" id="newTask" placeholder="Enter task">
      <button onclick="addTask()">Add</button>

      <script>
        async function loadTasks() {
          const res = await fetch("/tasks");
          const tasks = await res.json();
          const list = document.getElementById("taskList");
          list.innerHTML = "";
          tasks.forEach((item) => {
            const li = document.createElement("li");
            li.textContent = item.id + ". " + item.task;
            const delBtn = document.createElement("button");
            delBtn.textContent = "Delete";
            delBtn.onclick = () => deleteTask(item.id);
            const updBtn = document.createElement("button");
            updBtn.textContent = "Update";
            updBtn.onclick = () => updateTask(item.id);
            const doneBtn = document.createElement("button");
            doneBtn.textContent = "Done";
            doneBtn.onclick = () => markDone(item.id);
            li.appendChild(delBtn);
            li.appendChild(updBtn);
            li.appendChild(doneBtn);
            list.appendChild(li);
          });
        }

        async function addTask() {
          const task = document.getElementById("newTask").value;
          if (!task) return;
          await fetch("/tasks", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ task })
          });
          document.getElementById("newTask").value = "";
          loadTasks();
        }

        async function deleteTask(id) {
          await fetch("/tasks/" + id, { method: "DELETE" });
          loadTasks();
        }

        async function updateTask(id) {
          const newTask = prompt("Enter new task text:");
          if (newTask) {
            await fetch("/tasks/" + id, {
              method: "PUT",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ task: newTask })
            });
            loadTasks();
          }
        }

        async function markDone(id) {
          await fetch("/tasks/" + id + "/done", { method: "PATCH" });
          loadTasks();
        }

        loadTasks();
      </script>
    </body>
    </html>
    """
    return Response(html, mimetype="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
