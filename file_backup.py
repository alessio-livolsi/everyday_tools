# python
import os
import zipfile
import datetime


def backup_directory(source_dir, backup_dir):
    """
    Backs up the specified directory into a zip file in the backup directory.
    the zip file is named with the source directory name and current timestamp in day-month-year format.
    """
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"source directory '{source_dir}' does not exist.")
    if not os.path.isdir(source_dir):
        raise NotADirectoryError(f"'{source_dir}' is not a directory.")

    # get the base name of the directory being backed up
    dir_name = os.path.basename(os.path.normpath(source_dir))

    # create the backup directory if it doesn't exist
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # generate a timestamped zip file name in day-month-year format
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H%M%S")
    zip_filename = os.path.join(backup_dir, f"{dir_name}_backup_{timestamp}.zip")

    # create the zip file
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                # get the full path of the file
                file_path = os.path.join(root, file)
                # calculate the relative path for the zip file
                arcname = os.path.relpath(file_path, start=source_dir)
                # write the file to the zip archive
                zipf.write(file_path, arcname)

    print(f"backup completed: {zip_filename}")


if __name__ == "__main__":
    print("welcome to the simple backup tool!")
    source_dir = input("enter the full path of the directory to back up: ").strip()
    backup_dir = input("enter the full path of the backup destination: ").strip()

    try:
        backup_directory(source_dir, backup_dir)
    except Exception as e:
        print(f"error: {e}")
