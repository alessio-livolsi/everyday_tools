# python
import subprocess
import sys


def speak_mac(text):
    """Use macOS built-in 'say' command to convert text to speech."""
    subprocess.run(["say", text])


def speak_windows(text):
    """Use Windows PowerShell to convert text to speech."""
    command = f"""
    Add-Type –AssemblyName System.speech;
    $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer;
    $speak.Speak('{text}');
    """
    subprocess.run(["powershell", "-Command", command], shell=True)


def speak_linux(text):
    """Use Linux 'espeak' command to convert text to speech."""
    subprocess.run(["espeak", text])


def text_to_speech(text):
    """Select the appropriate text-to-speech method based on the OS."""
    # macOS
    if sys.platform == "darwin":
        speak_mac(text)
        # windows
    elif sys.platform == "win32":
        speak_windows(text)
        # linux
    elif sys.platform.startswith("linux"):
        speak_linux(text)
    else:
        print("Unsupported OS")


def main():
    """Main function to get user input and convert it to speech."""
    print("Enter the text you want to convert to speech (or type 'exit' to quit):")
    while True:
        text = input("> ")
        if text.lower() == "exit":
            print("Exiting...")
            break
        if text.strip():
            text_to_speech(text)
        else:
            print("Please enter some text.")


if __name__ == "__main__":
    main()
