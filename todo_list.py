# python
import csv
import datetime
import os

TODO_FILE = "todo_list.csv"


def load_tasks():
    """Load tasks from the CSV file if it exists."""
    tasks = []
    # check if the CSV file exists
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            # read each row from the CSV file and append to the tasks list
            for row in reader:
                tasks.append(row)
    return tasks


def save_tasks(tasks):
    """Save the current list of tasks to the CSV file."""
    with open(TODO_FILE, mode="w", newline="") as file:
        # define the columns for the CSV file
        fieldnames = [
            "ID",
            "Description",
            "Priority",
            "Due Date",
            "Start Time",
            "End Time",
            "Status",
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # write the header and all tasks to the CSV file
        writer.writeheader()
        writer.writerows(tasks)


def add_task(tasks):
    """Add a new task with user input."""
    # assign a unique ID to the new task
    task_id = str(len(tasks) + 1)
    description = input("Enter task description: ")
    priority = input("Enter priority (Low, Medium, High): ").capitalize()

    # prompt the user to enter the due date in either format
    due_date = input("Enter due date (DD-MM-YYYY or DD/MM/YYYY): ")
    if due_date:
        # allow both DD-MM-YYYY and DD/MM/YYYY formats by replacing slashes with hyphens
        due_date = due_date.replace("/", "-")
        try:
            # validate the date format
            datetime.datetime.strptime(due_date, "%d-%m-%Y")
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY or DD/MM/YYYY.")
            return

    # prompt the user to enter start and end times in HH:MM format
    start_time = input("Enter start time (HH:MM): ")
    end_time = input("Enter end time (HH:MM): ")

    # validate the start and end times
    if not validate_time(start_time) or not validate_time(end_time):
        print("Invalid time format. Please use HH:MM.")
        return

    # new tasks are marked as pending by default
    status = "Pending"

    # create a dictionary representing the new task
    task = {
        "ID": task_id,
        "Description": description,
        "Priority": priority,
        "Due Date": due_date,
        "Start Time": start_time,
        "End Time": end_time,
        "Status": status,
    }
    # add the new task to the tasks list
    tasks.append(task)
    print("Task added successfully!")


def validate_time(time_str):
    """Validate that a given string is in HH:MM format."""
    try:
        # use strptime to check if the time is valid
        datetime.datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False


def list_tasks(tasks):
    """Display all tasks in a table format."""
    if not tasks:
        print("No tasks found.")
        return

    # print table headers
    print("\nID | Description | Priority | Due Date | Start Time | End Time | Status")
    print("-" * 80)

    # print each task in a formatted manner
    for task in tasks:
        print(
            f"{task['ID']} | {task['Description']} | {task['Priority']} | {task['Due Date']} | "
            f"{task['Start Time']} | {task['End Time']} | {task['Status']}"
        )


def mark_task_completed(tasks):
    """Mark a specific task as completed."""
    task_id = input("Enter task ID to mark as completed: ")

    # find the task by ID and mark it as completed
    for task in tasks:
        if task["ID"] == task_id:
            if task["Status"] == "Completed":
                print("Task is already completed.")
            else:
                task["Status"] = "Completed"
                print("Task marked as completed.")
            return
    print("Task not found.")


def delete_task(tasks):
    """Delete a task by its ID."""
    task_id = input("Enter task ID to delete: ")

    # search for the task by ID and remove it if found
    for i, task in enumerate(tasks):
        if task["ID"] == task_id:
            tasks.pop(i)
            print("Task deleted successfully.")
            return
    print("Task not found.")


def main():
    """Main function to manage the interactive menu."""
    # load existing tasks from the CSV file
    tasks = load_tasks()

    while True:
        # display the menu options
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        # get the user's choice
        choice = input("Choose an option (1-5): ")

        # call the appropriate function based on the user's choice
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            # save tasks before exiting
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
