# python
import os
import datetime as dt
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor

# define the Trash directory for deleted files
TRASH_DIR = os.path.expanduser("~/.Trash/")


def main():
    # prompt user for input and output directories
    input_dir = input(
        "Enter the path to the directory containing .flac files: "
    ).strip()
    output_dir = input(
        "Enter the path to the output directory for .wav files: "
    ).strip()

    # validate the input directory
    if not os.path.isdir(input_dir):
        print(f"Error: The input directory '{input_dir}' does not exist.")
        return

    # create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # process the files using a thread pool
    with ThreadPoolExecutor(max_workers=16) as executor:
        for original_filename in find_flacs(input_dir):
            executor.submit(convert, original_filename, output_dir)


def find_flacs(directory):
    """Find all .flac files in the specified directory and its subdirectories."""
    command = ["find", directory, "-type", "f", "-iname", "*.flac", "-print0"]
    names = subprocess.check_output(command, universal_newlines=True)
    for name in names.split("\0"):
        if name:
            yield name


def convert(original_filename, output_dir):
    """Convert a .flac file to .wav and move the original to Trash."""
    print(f"Converting: {original_filename}")
    base_name = os.path.basename(original_filename).rsplit(".", 1)[0]
    wav_filename = os.path.join(output_dir, base_name + ".wav")

    if os.path.exists(wav_filename):
        print(f"\t{wav_filename} already exists! Skipping...")
        return

    return_code = subprocess.call(
        [
            "ffmpeg",
            "-i",
            original_filename,
            "-acodec",
            "pcm_s16le",
            "-ar",
            "44100",
            wav_filename,
        ]
    )

    if return_code == 0:
        print(f"\tSuccessfully converted to {wav_filename}")
        trash_file(original_filename)
    else:
        print(f"\tError converting {original_filename}")


def trash_file(filename):
    """Move a file to the Trash directory."""
    base_filename = os.path.basename(filename)
    trash_filename = os.path.join(TRASH_DIR, base_filename)

    # append a timestamp if a file with the same name already exists in Trash
    if os.path.exists(trash_filename):
        name, ext = os.path.splitext(base_filename)
        date_bit = f" ({dt.datetime.now().isoformat()})"
        trash_filename = os.path.join(TRASH_DIR, name + date_bit + ext)

    shutil.move(filename, trash_filename)
    print(f"\tMoved {filename} to Trash")


if __name__ == "__main__":
    main()
