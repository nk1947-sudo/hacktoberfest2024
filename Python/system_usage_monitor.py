import psutil
import time

def display_system_usage():
    while True:
        # Get CPU usage percentage
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # Get RAM usage
        memory_info = psutil.virtual_memory()
        total_memory = memory_info.total / (1024 ** 3)  # Convert from bytes to GB
        used_memory = memory_info.used / (1024 ** 3)    # Convert from bytes to GB
        memory_usage_percent = memory_info.percent

        # Display the information
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Total Memory: {total_memory:.2f} GB")
        print(f"Used Memory: {used_memory:.2f} GB ({memory_usage_percent}%)")
        print("-" * 30)
        
        time.sleep(2)  # Update every 2 seconds

if __name__ == "__main__":
    display_system_usage()
