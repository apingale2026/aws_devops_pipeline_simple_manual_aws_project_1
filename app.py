import os 

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return [line.strip() for line in f.readlines() ]

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
          for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
         print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}.{task}")

def main ():
    tasks = load_tasks()
    while True:
          print("\nOptions: [1] Add [2] View [3] Done [4] Delete [5] Exit ")
          choice = input("Choose: ")

          if choice == "1":
              task = input("Enter task: ")
              tasks.append(task)
              save_tasks(tasks)
          elif choice == "2":
              show_tasks(tasks)
          elif choice == "3":
              show_tasks(tasks)
              idx = int(input("Which task no to mark as done: ")) - 1
              if 0 <= idx < len(tasks):
                  tasks[idx]+= "✅"
                  save_tasks(tasks)
          elif choice == "4":
              show_tasks(tasks)
              idx = int(input("Which task no to mark as done: ")) - 1
              if 0 <= idx < len(tasks):
                  tasks.pop(idx)
                  save_tasks(tasks)
          elif choice == "5":
               break
          else:
              print("Invalid Choice")
if __name__ == "__main__":
    main()      
          
                
                
