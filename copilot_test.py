import os
import platform
import subprocess

def get_uptime():
    system = platform.system()
    if system == "Windows":
        # Windows: Use 'net stats srv' and parse the result
        output = subprocess.check_output("net stats srv", shell=True, text=True)
        for line in output.splitlines():
            if "Statistics since" in line:
                print("System Uptime (since):", line.split("since")[1].strip())
                return
        print("Could not determine uptime on Windows.")
    elif system == "Linux":
        # Linux: Use uptime command
        output = subprocess.check_output("uptime -p", shell=True, text=True)
        print("System Uptime:", output.strip())
    elif system == "Darwin":
        # macOS: Use uptime command
        output = subprocess.check_output("uptime", shell=True, text=True)
        print("System Uptime:", output.strip())
    else:
        print("Unsupported OS:", system)

if __name__ == "__main__":
    get_uptime()
