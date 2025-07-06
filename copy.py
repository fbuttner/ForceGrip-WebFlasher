import os
import shutil


def get_platformio_core_dir():
    """
    Finds the PlatformIO core directory.

    It checks the PLATFORMIO_CORE_DIR environment variable first,
    then tries to get it from `pio settings get core_dir` command,
    and finally falls back to the default '~/.platformio'.

    Returns:
        str: The path to the PlatformIO core directory, or None if not found.
    """
    # 1. Check environment variable
    core_dir = os.environ.get("PLATFORMIO_CORE_DIR")
    if core_dir and os.path.isdir(core_dir):
        print(f"Found PlatformIO core directory from environment variable: {core_dir}")
        return core_dir

    # 2. Try `pio` command
    try:
        # Find the `platformio` or `pio` executable in the system's PATH
        pio_executable = shutil.which("platformio") or shutil.which("pio")
        if pio_executable:
            result = subprocess.run(
                [pio_executable, 'settings', 'get', 'core_dir'],
                capture_output=True, text=True, check=True, timeout=10
            )
            core_dir = result.stdout.strip()
            if os.path.isdir(core_dir):
                print(f"Found PlatformIO core directory via '{pio_executable}' command: {core_dir}")
                return core_dir
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        # Command failed, not found, or timed out, so we'll proceed to the fallback
        pass

    # 3. Fallback to the default user-home location
    default_core_dir = os.path.expanduser("~/.platformio")
    if os.path.isdir(default_core_dir):
        print(f"Using default PlatformIO core directory: {default_core_dir}")
        return default_core_dir

    print("Error: Could not find the PlatformIO core directory.")
    return None

def copy_file(source_path, source_file, destination_path, destination_file):
    """
    Copies a file from the source path to the destination path.

    Args:
        source_path (str): The path to the source file.
        source_file (str): The name of the source file.
        destination_path (str): The path to the destination file.
        destination_file (str): The name of the destination file.
    """
    source_path = os.path.join(source_path, source_file)
    destination_path = os.path.join(destination_path, destination_file)
    try:
        shutil.copy2(source_path, destination_path)
        print(f"File copied from {source_path} to {destination_path}")
    except FileNotFoundError:
        print(f"Error: Source file not found at {source_path}")
    except PermissionError:
        print(f"Error: Permission denied when copying to {destination_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    project_folder = os.getcwd()
    project_source_folder = os.path.join(project_folder, "..", "ForceGrip")
    pio_core_folder = get_platformio_core_dir()

    binaries_folder = os.path.join(project_source_folder, ".pio", "build", "lolin_c3_mini")
    boot_folder = os.path.join(pio_core_folder, "packages", "framework-arduinoespressif32", "tools", "partitions")
    
    copy_file(binaries_folder, "bootloader.bin", project_folder, "bootloader.bin")
    copy_file(binaries_folder, "partitions.bin", project_folder, "partitions.bin")
    copy_file(boot_folder, "boot_app0.bin", project_folder, "boot_app0.bin")
    copy_file(binaries_folder, "firmware.bin", project_folder, "firmware.bin")
    copy_file(binaries_folder, "spiffs.bin", project_folder, "spiffs.bin")
