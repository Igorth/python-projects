import sys
import socket
import threading
import time
from datetime import datetime
from threading import Lock
from concurrent.futures import ThreadPoolExecutor

# Simple color codes
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# Lock used to prevent multiple threads from printing at the same time.
# Without this, the output from different threads would overlap and become unreadable.
print_lock = Lock()

def print_safe(message):
    with print_lock:
        print(message)

# Function to scan a port
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port)) # Error indicator - if 0 port is open
        if result == 0:
            print_safe(f"{GREEN}[OPEN]{RESET} TCP Port {port}")
        s.close()
    except socket.error as e:
        print(f"Socket error on port {port}: {e}")
    except Exception as e:
        print(f"Unexpected error on port {port}: {e}")

# Main function - argument validation and target definition
def main():
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        print("Invalid number of arguments.")
        print("Usage: python.exe scanner.py <target_ip>")
        sys.exit(1)
    
    # Resolve the target hostname to an IP address
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Error: Unable to resolve hostname {target}")
        sys.exit(1)

    # Add a banner
    print("-" * 60)
    print(f"Scanning target: {target_ip}")
    print(f"Scan Start: {datetime.now()}")
    print("-" * 60)

    start_time = time.time()

    # # Define the maximum number of threads that can run simultaneously.
    max_threads = 500
    ports = range(1, 65536)

    # Create a thread pool to execute port scans concurrently.
    # The ThreadPoolExecutor automatically manages thread creation and cleanup.
    with ThreadPoolExecutor(max_threads) as executor:
        for port in ports:
            executor.submit(scan_port, target_ip, port)
    
    end_time = time.time()
    duration = round(end_time - start_time, 2)

    print("\n" + "-" * 60)
    print(f"Scanning completed in {duration} seconds")
    print(f"Total Ports Scanned: {len(ports)} TCP")
    print("-" * 60)


if __name__ == "__main__":
    main()