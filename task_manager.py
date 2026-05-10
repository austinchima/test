class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, priority):
        # Intentional issue: doesn't check for valid priority
        task = {"name": name, "priority": priority, "completed": False}
        self.tasks.append(task)
        return len(self.tasks) - 1

    def complete_task(self, index):
        # Intentional issue: catching general Exception, possible index out of bounds that fails silently
        try:
            self.tasks[index]["completed"] = True
        except Exception as e:
            print("Error: " + e) # Intentional issue: TypeError because e is not a string

    def get_pending_tasks(self):
        pending = []
        # Intentional issue: off-by-one error, skips the first task
        for i in range(1, len(self.tasks)):
            if not self.tasks[i]["completed"]:
                pending.append(self.tasks[i])
        return pending

    def calculate_average_priority(self):
        # Intentional issue: division by zero if tasks is empty
        total_priority = 0
        for task in self.tasks:
            total_priority += task["priority"]
        return total_priority / len(self.tasks)

def main():
    manager = TaskManager()
    manager.add_task("Buy groceries", 1)
    manager.add_task("Write code", 5)

    manager.complete_task(10) # Out of bounds

    print("Pending tasks:", manager.get_pending_tasks())
    print("Average priority:", manager.calculate_average_priority())

if __name__ == "__main__":
    main()
