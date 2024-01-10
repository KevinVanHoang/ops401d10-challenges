# Python

# Script Name:                  Ops Challenge: Uptime Sensor Tool Part 1 of 2
# Author:                       Kevin Hoang
# Date of latest revision:      1/9/2024
# Purpose:                      Monitor the status of hosts using ICMP packets
# Execution:                    ops2.py
# Resources:                    https://www.tutorialspoint.com/How-to-print-current-date-and-time-using-Python
#                               https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-03/challenges/ops_challenge_2.py
#                               https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-02/challenges/class_demo.py

import time
from ping3 import ping

# Function to get the target IP from user input or default to "8.8.8.8"
def get_ip():
    ip = input("Please enter the target IP: ")
    if not ip:
        ip = "8.8.8.8"
    return ip

# Function to monitor network uptime for a given target IP
def monitor_uptime(target_ip, interval_seconds=2):
    while True:
        try:
            # Ping the target IP with a timeout of 1 second
            response = ping(target_ip, timeout=1)

            # Determine the network status based on the response
            status = "Network Active" if response is not None else "Network Inactive"

            # Get the current timestamp
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

            # Print the timestamp, network status, and target IP
            print(f"{timestamp} {status} to {target_ip}")

        except Exception as error:
            # Print an error message if an exception occurs
            print(f"Error: {error}")

        # Pause for the specified interval before the next iteration
        time.sleep(interval_seconds)

# If this script is executed directly, run the monitor_uptime function
if __name__ == "__main__":
    target_ip = get_ip()
    monitor_uptime(target_ip)
