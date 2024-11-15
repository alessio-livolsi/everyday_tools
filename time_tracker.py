# python
import os
from datetime import datetime

# generate a timestamped log file in the user's specified directory
LOG_FILE = os.path.expanduser(
    f"~/Desktop/time_log_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.txt"
)


def start_task():
    """
    Prompt the user to enter a task name and record the start time.
    Returns:
        - task_name (str): The name of the task entered by the user.
        - start_time (datetime): The timestamp when the task started.
    """
    # prompt the user for the task name
    task_name = input("Enter the task name: ").strip()

    # Eensure the task name is not empty
    if not task_name:
        print("Task name cannot be empty.")
        return None, None

    # record the current time as the start time
    start_time = datetime.now()
    print(f"Task '{task_name}' started at {start_time.strftime('%d-%m-%Y %H:%M:%S')}")
    return task_name, start_time


def stop_task(task_name, start_time):
    """
    Stop the current task, calculate the duration, and log it to the file.
    Args:
        - task_name (str): The name of the task being tracked.
        - start_time (datetime): The timestamp when the task started.
    Returns:
        - duration (timedelta): The time spent on the task.
    """
    # capture the current time as the end time
    end_time = datetime.now()

    # calculate the duration of the task
    duration = end_time - start_time

    # format the duration to exclude microseconds
    duration_str = format_duration(duration)

    # log the task details to the file
    log_task(task_name, start_time, end_time, duration_str)
    print(f"Task '{task_name}' completed. Duration: {duration_str}")
    return duration


def format_duration(duration):
    """
    Format the duration to show hours, minutes, and seconds only.
    """
    hours, remainder = divmod(duration.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"


def log_task(task_name, start_time, end_time, duration):
    """
    Log the task details (task name, start time, end time, duration) to a text file.
    Args:
        - task_name (str): The name of the task.
        - start_time (datetime): The timestamp when the task started.
        - end_time (datetime): The timestamp when the task ended.
        - duration (str): The formatted duration string.
    """
    with open(LOG_FILE, "a") as file:
        file.write(f"Task: {task_name}\n")
        file.write(f"Start Time: {start_time.strftime('%d-%m-%Y %H:%M:%S')}\n")
        file.write(f"End Time: {end_time.strftime('%d-%m-%Y %H:%M:%S')}\n")
        file.write(f"Duration: {duration}\n")
        file.write("=" * 40 + "\n")
    print("Task logged successfully!")


def view_log():
    """
    Display the contents of the current time log file.
    """
    if not os.path.exists(LOG_FILE):
        print("No log file found.")
        return

    with open(LOG_FILE, "r") as file:
        content = file.read()

        if content:
            print("\n--- Time Log ---\n")
            print(content)
        else:
            print("No entries found in the log.")


def main():
    """
    Main function that handles the user menu and task management.
    """
    while True:
        print("\nOptions:")
        print("1. Start a new task")
        print("2. View time log")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            task_name, start_time = start_task()
            if task_name and start_time:
                input("Press Enter to stop the task...")
                stop_task(task_name, start_time)
        elif choice == "2":
            view_log()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
