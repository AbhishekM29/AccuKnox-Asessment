import psutil
import logging
from datetime import datetime


CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
PROCESS_THRESHOLD = 200

LOG_FILE = "path/system_health.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

def log_alert(message):
    print(message)
    logging.info(message)

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"High CPU usage detected: {cpu_usage}%")

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_alert(f"High memory usage detected: {memory_usage}%")

def check_disk_usage():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        log_alert(f"High disk space usage detected: {disk_usage}%")

def check_process_count():
    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        log_alert(f"High number of running processes detected: {process_count}")

def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_process_count()

if __name__ == "__main__":
    main()
