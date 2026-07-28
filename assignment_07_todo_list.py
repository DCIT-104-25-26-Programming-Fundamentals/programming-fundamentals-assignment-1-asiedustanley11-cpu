# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def show_menu():
    """
    Print the main menu.
    """
    print("============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")
 
 
def add_task(tasks):
    """
    Prompt the user for a task description and add it to the tasks list.
    Modifies the list in place.
    """
    description = input("Enter task: ").strip()
 
    if description == "":
        print("Task cannot be empty. Nothing was added.")
        return
 
    tasks.append(description)
    print(f'Task added: "{description}"')
 
 
def view_tasks(tasks):
    """
    Display all tasks, numbered starting at 1. If there are no tasks,
    print a friendly message instead.
    """
    if not tasks:
        print("Your task list is empty. Add a task to get started!")
        return
 
    print("Your Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
 
 
def delete_task(tasks):
    """
    Show the current tasks, ask which one to delete by number, and
    remove it. Prints an error message if the number is invalid.
    """
    if not tasks:
        print("Your task list is empty. Nothing to delete.")
        return
 
    view_tasks(tasks)
    choice = input("Enter task number to delete: ").strip()
 
    try:
        task_number = int(choice)
    except ValueError:
        print("Please enter a valid task number.")
        return
 
    # Task numbers shown to the user start at 1, but list positions
    # (indices) start at 0, so we subtract 1 to find the right item.
    index = task_number - 1
 
    if index < 0 or index >= len(tasks):
        print("Error: that task number does not exist.")
        return
 
    removed_task = tasks.pop(index)
    print(f'Task "{removed_task}" has been removed.')
 
 
def main():
    tasks = []  # the list that stores all task descriptions
 
    # Keep showing the menu until the user chooses to quit.
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()
 
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break  # exits the while loop, ending the program
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
 
        print()  # blank line for readability before the menu repeats
 
 
if __name__ == "__main__":
    main()