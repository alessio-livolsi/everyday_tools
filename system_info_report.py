# python
import os
import platform
import socket
import shutil


def get_system_info():
    """
    Display general system information, such as hostname, OS, and architecture.
    """
    print("\nSYSTEM INFORMATION")
    # get the system's hostname
    print(f"Hostname: {socket.gethostname()}")

    # get information about the operating system
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"OS Version: {platform.version()}")

    # get the system architecture (e.g., x86_64)
    print(f"Architecture: {platform.machine()}")

    # get the processor information (CPU model)
    print(f"Processor: {platform.processor()}")

    # display the system boot time
    print(f"Boot Time: {get_boot_time()}")

    # calculate and display system uptime
    print(f"Uptime: {get_uptime()}")


def get_boot_time():
    """
    Get the system boot time using the 'who -b' command (available on Unix systems).
    Returns the boot time as a string or 'N/A' if not available.
    """
    try:
        # execute the shell command to get the last boot time
        boot_time = os.popen("who -b").read().strip()
        # extract and return the boot time from the command output
        return boot_time.split()[-2] + " " + boot_time.split()[-1]
    except IndexError:
        # return 'N/A' if the command fails
        return "N/A"


def get_uptime():
    """
    Calculate system uptime using the 'uptime -p' command (available on Unix systems).
    Returns the uptime as a string or 'N/A' if not available.
    """
    try:
        # execute the shell command to get the system uptime
        uptime_output = os.popen("uptime -p").read().strip()
        return uptime_output if uptime_output else "N/A"
    except Exception:
        return "N/A"


def get_cpu_info():
    """
    Display basic CPU information, such as processor model and system load average.
    """
    print("\nCPU INFORMATION")
    # display the CPU model
    print(f"Processor: {platform.processor()}")

    # get and display system load averages (only available on Unix systems)
    try:
        load_avg = os.getloadavg()
        print(
            f"Load Average (1, 5, 15 min): {load_avg[0]}, {load_avg[1]}, {load_avg[2]}"
        )
    except AttributeError:
        # if not supported (e.g., on Windows), display 'N/A'
        print("Load Average: N/A (Windows does not support this)")


def get_memory_info():
    """
    Display basic memory usage information using system commands.
    Uses 'vm_stat' on macOS and 'free' on Linux.
    """
    print("\nMEMORY INFORMATION")
    if platform.system() == "Darwin":
        # macOS: Use the 'vm_stat' command to get memory statistics
        vm_stat = os.popen("vm_stat").read()
        print(vm_stat)
    elif platform.system() == "Linux":
        # linux: Use the 'free -h' command to display memory usage
        mem_info = os.popen("free -h").read()
        print(mem_info)
    else:
        # if the system is neither macOS nor Linux, display 'N/A'
        print("Memory Info: Not available on this system")


def get_disk_info():
    """
    Display disk usage information using the shutil module.
    """
    print("\nDISK INFORMATION")
    # get the disk usage for the root partition ('/')
    total, used, free = shutil.disk_usage("/")

    # display the total, used, and free disk space in a human-readable format
    print(f"Total: {get_size(total)}")
    print(f"Used: {get_size(used)}")
    print(f"Free: {get_size(free)}")


def get_network_info():
    """
    Display basic network information, such as the local IP address.
    """
    print("\nNETWORK INFORMATION")
    # get the system's hostname
    hostname = socket.gethostname()

    # get the local IP address associated with the hostname
    ip_address = socket.gethostbyname(hostname)

    # display the hostname and local IP address
    print(f"Hostname: {hostname}")
    print(f"Local IP Address: {ip_address}")


def get_size(bytes, suffix="B"):
    """
    Convert bytes to a human-readable format (e.g., KB, MB, GB).
    - bytes: The number of bytes to convert.
    - suffix: The unit suffix (default is 'B' for bytes).
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        # if the size is less than the factor (1024), return the formatted size
        if bytes < factor:
            return f"{bytes:.2f} {unit}{suffix}"
        bytes /= factor


def main():
    """
    Main function to display all system information reports.
    Calls individual functions to display system, CPU, memory, disk, and network info.
    """
    print("System Information Report")

    # call the functions to gather and display system information
    get_system_info()
    get_cpu_info()
    get_memory_info()
    get_disk_info()
    get_network_info()


if __name__ == "__main__":
    main()
