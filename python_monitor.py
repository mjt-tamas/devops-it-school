import time
import datetime
import platform
import psutil
import sys

SLEEP_INTERVAL = 5
BYTES_TO_GB = 1024 ** 3

def get_system_info():
    try:
        # --- Current Date and Time ---
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("==========================================================")
        print("Monitoring Data: {}".format(current_time))
        print("----------------------------------------------------------")

        # --- OS Information ---
        print("OS/Platform Info:")
        print("    System: {}".format(platform.system()))
        print("    Release: {}".format(platform.release()))
        print("    Python Version: {}".format(sys.version.split('\n')[0]))
        print("")

        # --- CPU Information ---
        cpu_percent = psutil.cpu_percent(interval=None) 
        cpu_count_logical = psutil.cpu_count(logical=True)
        print("CPU Information:")
        print("    Logical Cores: {}".format(cpu_count_logical))
        print("    Current Usage: {}%".format(cpu_percent))
        print("")

        # --- RAM Information ---
        mem = psutil.virtual_memory()
        
        total_gb = mem.total / BYTES_TO_GB
        used_gb = mem.used / BYTES_TO_GB
        available_gb = mem.available / BYTES_TO_GB
        
        print("RAM Usage:")
        print("    Total: {:.2f} GB".format(total_gb))
        print("    Used: {:.2f} GB".format(used_gb))
        print("    Available: {:.2f} GB".format(available_gb))
        print("    Usage Percentage: {}%".format(mem.percent))
        print("")

        # --- Disk Information (Root Partition) ---
        disk_usage = psutil.disk_usage('/')
        
        total_disk_gb = disk_usage.total / BYTES_TO_GB
        used_disk_gb = disk_usage.used / BYTES_TO_GB
        
        print("Disk Usage (Root '/'):")
        print("    Total: {:.2f} GB".format(total_disk_gb))
        print("    Used: {:.2f} GB".format(used_disk_gb))
        print("    Usage Percentage: {}%".format(disk_usage.percent))
        print("==========================================================")
        
    except Exception as e:
        print("ERROR during monitoring: {}".format(e))

print("Starting Python System Monitor (Interval: {}s)...".format(SLEEP_INTERVAL))

while True:
    get_system_info()
    time.sleep(SLEEP_INTERVAL)