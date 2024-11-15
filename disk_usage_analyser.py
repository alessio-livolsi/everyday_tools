# python
import os
from datetime import datetime


def get_file_size(path):
    """
    Return the size of a file in bytes.
    If the file is inaccessible, return 0.
    """
    try:
        return os.path.getsize(path)
    except OSError:
        return 0


def get_folder_size(path):
    """
    Recursively calculate the total size of a folder.
    This includes the sizes of all files and subdirectories.
    """
    total_size = 0
    # walk through the directory tree
    for dirpath, _, filenames in os.walk(path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            # add the size of each file
            total_size += get_file_size(file_path)
    return total_size


def display_size(size):
    """
    Convert a size in bytes to a human-readable format (KB, MB, GB, etc.).
    """
    # loop through units of measurement
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"


def analyze_disk_usage(directory="."):
    """
    Analyze the disk usage for a specified directory.
    If no directory is provided, it defaults to the current directory.
    """
    print(f"Analyzing disk usage for: {os.path.abspath(directory)}")
    print("=" * 50)

    try:
        # list all files and subdirectories in the specified directory
        items = os.listdir(directory)
    except PermissionError:
        # handle cases where permission is denied
        print(f"Permission denied: {directory}")
        return
    except FileNotFoundError:
        # handle cases where the directory does not exist
        print(f"Directory not found: {directory}")
        return

    total_size = 0
    folder_sizes = []

    # loop through all items in the directory
    for item in items:
        item_path = os.path.join(directory, item)
        # check if the item is a directory or a file and get its size
        if os.path.isdir(item_path):
            # calculate folder size
            size = get_folder_size(item_path)
        else:
            # get file size
            size = get_file_size(item_path)

        # append the item and its size to the list
        folder_sizes.append((item, size))
        # add to the total size
        total_size += size

    # sort items by size in descending order
    folder_sizes.sort(key=lambda x: x[1], reverse=True)

    # print each item's size in a human-readable format
    for item, size in folder_sizes:
        print(f"{display_size(size):>10}  {item}")

    print("=" * 50)
    print(f"Total size: {display_size(total_size)}")
    print(f"Analysis completed on {datetime.now()}")


def main():
    """
    Main function to prompt the user for input and analyze disk usage.
    """
    print("Enter the directory to analyze (press Enter for current directory):")
    # get user input for directory
    directory = input("> ").strip()
    # ff no input is given, default to the current directory
    if not directory:
        directory = "."
        # run the analysis
    analyze_disk_usage(directory)


if __name__ == "__main__":
    main()
