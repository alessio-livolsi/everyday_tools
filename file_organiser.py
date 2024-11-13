# python
import os
import shutil

# define file extensions and their corresponding folder names
EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Scripts": [".py", ".sh", ".js", ".html", ".css"],
    "Books": [".epub"],
}


def organize_files(directory: str) -> None:
    """Organize files in the specified directory based on their extensions."""
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    # get all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # get the file extension
        _, file_extension = os.path.splitext(filename)

        # determine the folder name based on the file extension
        folder_name = None
        for category, extensions in EXTENSION_MAP.items():
            if file_extension.lower() in extensions:
                folder_name = category
                break

        # if no matching folder is found, skip the file
        if not folder_name:
            continue

        # create the target folder if it doesn't exist
        target_folder = os.path.join(directory, folder_name)
        os.makedirs(target_folder, exist_ok=True)

        # move the file to the target folder
        try:
            shutil.move(file_path, target_folder)
            print(f"Moved: {filename} -> {target_folder}")
        except shutil.Error as e:
            print(f"Error moving {filename}: {e}")


def main():
    print("File Organizer Script")
    target_directory = input(
        "Enter the directory to organize (leave blank for current directory): "
    )
    if not target_directory:
        target_directory = os.getcwd()

    organize_files(target_directory)


if __name__ == "__main__":
    main()
