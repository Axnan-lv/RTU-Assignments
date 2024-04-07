# Step 1: Display the Menu
#     Menu 1: Add Task
#     Menu 2: View Tasks
#     Menu 3: Mark as Done
#     Menu 4: Exit
# Step 2: Let the User Input the Choice from the Menu
# Step 3: if User Choose from 1-4 goto step 5 else goto step 4
# Step 4: Display: Invalid Choice. go back to step 1
# Step 5: if user select 1 goto step 6 
#         else if user select 2 goto step 9 
#         else if user select 3 goto step 10
#         else if user select 4 goto step 12
# Step 6: Let the User Enter the Task Details
# Step 7: Let the User Enter the Task due date if required
# Step 8: Display: Task Added Successfully. goto step 1
# Step 9: Diplay the Added Tasks.
#         if no tasks are added Display: No Tasks Found. goto step 1
# Step 10: Display the Tasks Added And Let the user select from the list.
#          if no tasks are added Display: No Tasks Found
# Step 11: If user selected from the list Diplay: Marked as Done Successfully 
#          else Display: Invalid Selection. goto step 1
# Step 12: Display: Exiting Application
# Step 13: Display: Summary of Completed and Pending Tasks
# END

tasks = []
def menu():
    print("Main Menu:\n1. Add Task\n2. View Tasks\n3. Mark as Done\n4. Exit")

def add_task():
    task_desc = input("Enter the task: ")
    due_date = input("Enter due date (optional): ")
    task = {"description": task_desc, "due_date": due_date, "completed": False}
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    print("Task List:")
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. Description: {task['description']}, Due Date: {task['due_date']}, Completed: {task['completed']}")

def mark_as_done():
    view_tasks()
    task_index = int(input("Enter the task No to mark as done: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print("Task marked as done successfully!")
    else:
        print("Invalid Selection.")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_as_done()
        elif choice == "4":
            print("Exiting Application.")
            completed = sum(1 for task in tasks if task['completed'])
            pending = len(tasks) - completed
            print(f"Summary: Completed tasks: {completed}, Pending tasks: {pending}")
            break
        else:
            print("Invalid choice. Please try again.")