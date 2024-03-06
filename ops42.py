#!/usr/bin/env python3
# Script Name:                  Ops Challenge: Attack Tools Part 2 of 3
# Author:                       Kevin Hoang
# Date of latest revision:      02/21/2024
# Resource:                     https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-42/challenges/DEMO.md
# Purpose:                      Nmap is a highly popular security tool used for enumeration tasks. By importing Nmap into Python we can begin to develop our own enumeration/port scanner tool.
#                               Today you will use Python to develop a custom Nmap scanner that can later be combined with other Python scripts to create a pentester toolkit.


import nmap

# Initialize Nmap PortScanner object
scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

# Prompt user for IP address to scan
ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

# Prompt user to select scan type
resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3)              \n""")
print("You have selected option: ", resp)

# Default port range for scanning
range = '1-50'

# Check user's selected option and execute appropriate scan
if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    # Perform SYN ACK scan
    scanner.scan(ip_addr, range, '-v -sS')
    # Print scan information
    print(scanner.scaninfo())
    # Print IP address status
    print("Ip Status: ", scanner[ip_addr].state())
    # Print protocols detected
    print(scanner[ip_addr].all_protocols())
    # Print open TCP ports
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Please enter a valid option") # Inform user to add missing code block
elif resp == '3':
    print("Please enter a valid option") # Inform user to add missing code block
elif resp >= '4':
    print("Please enter a valid option") # Inform user if option is out of range

# 1. Import the nmap module, which provides functionality for interacting with the Nmap security scanner.
# 2. Initialize a PortScanner object from the nmap module to perform port scanning.
# 3. Display introductory messages to the user.
# 4. Prompt the user to input the IP address they want to scan.
# 5. Print the IP address entered by the user.
# 6. Prompt the user to select a scan type.
# 7. Execute a specific scan based on the user's input:
#     7.1. If the user selects option '1', perform a SYN ACK scan (-sS flag in Nmap) on the specified IP address.
#         7.1.1. Print Nmap version.
#         7.1.2. Perform the scan using the specified range of ports.
#         7.1.3. Print scan information.
#         7.1.4. Print IP address status.
#         7.1.5. Print detected protocols.
#         7.1.6. Print open TCP ports.
#     7.2. If the user selects option '2', inform the user to add the missing code block for UDP scan.
#     7.3. If the user selects option '3', inform the user to add the missing code block for the third scan type.
#     7.4. If the user selects an option greater than or equal to '4', inform the user to enter a valid option.

# This script is intended to be completed by the user by adding functionality for options '2' and '3' as specified in the TODO comments.
