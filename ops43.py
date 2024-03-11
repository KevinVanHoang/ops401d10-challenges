#!/usr/bin/python3
# Script Name:                  Ops Challenge: Create a Port Scanner
# Author:                       Kevin Hoang
# Date of latest revision:      02/21/2024
# Resource:                     https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-42/challenges/DEMO.md
# Purpose:                      The purpose of this script is to determine if a target port is open or closed, using strictly Python 3 commands. 
#                               To do so, we’ll be importing the socket module, a low-level networking interface for Python.

import socket

def port_scanner(host, port_range):
    # Convert hostname to IPv4 address
    try:
        target_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        return

    print(f"Scanning target {target_ip}")

    for port in port_range:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed or filtered")
            s.close()

if __name__ == "__main__":
    # Define your target and port range here
    scan_target = "scanme.nmap.org"  # Change this to the host you want to scan
    target_ports = range(22, 444)  # Define the range of ports to scan

    port_scanner(scan_target, target_ports)
