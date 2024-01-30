#!/usr/bin/env python3 

# Script Name:                  Network Security Tool with Scapy Part 2 of 3
# Author:                       Kevin Hoang
# Date of latest revision:      1/22/2024
# Purpose:                      Script that creates a TCP Port Range Scanner that tests whether a TCP port is open or closed
# Execution:                    ops11.py
# Resources:                    https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-06/challenges/DEMO.md
#                               https://scapy.readthedocs.io/en/latest/introduction.html#
#                               https://scapy.readthedocs.io/en/latest/extending.html

# Import the Scapy library
import scapy.all as scapy
import ipaddress

# Function to perform ICMP Ping Sweep
def icmp_ping_sweep(target_network):
    # Convert the target network into a list of individual IP addresses
    ip_list = list(ipaddress.IPv4Network(target_network).hosts())
    # Initialize an empty list to store online hosts
    online_hosts = []

    # Loop through each IP address in the list
    for host in ip_list:
        # Skip network and broadcast addresses as they are not individual hosts
        if host == ipaddress.IPv4Network(target_network).network_address or host == ipaddress.IPv4Network(target_network).broadcast_address:
            continue

        # Print a message indicating that the script is pinging a host
        print("Pinging", str(host), "- please wait...")
        # Send an ICMP packet to the current host and wait for a response
        response = scapy.sr1(
            scapy.IP(dst=str(host))/scapy.ICMP(),
            timeout=2,
            verbose=0
        )
        
        # Check if there is a response
        if response:
            # Check if the response indicates the host is actively blocking ICMP traffic
            if response[scapy.ICMP].type == 3 and response[scapy.ICMP].code in {1, 2, 3, 9, 10, 13}:
                # Print a message indicating that the host is actively blocking ICMP traffic
                print(f"Host {str(host)} is actively blocking ICMP traffic.")
            else:
                # Print a message indicating that the host is responding
                print(f"Host {str(host)} is responding.")
                # Add the host to the list of online hosts
                online_hosts.append(str(host))
        else:
            # Print a message indicating that the host is down or unresponsive
            print(f"Host {str(host)} is down or unresponsive.")

    # Print a message indicating that the ping sweep is complete
    print("\nPing Sweep complete.")
    # Print the number of online hosts
    print(f"Number of online hosts: {len(online_hosts)}")
    # Return the list of online hosts
    return online_hosts

# Function to display the user menu
def display_menu():
    # Print the user menu
    print("\nMenu:")
    print("1. ICMP Ping Sweep")
    print("2. TCP Port Range Scanner")
    # Prompt the user for their choice
    choice = input("Enter your choice (1 or 2): ")
    # Return the user's choice
    return choice

# Entry point of the script
if __name__ == "__main__":
    # Get the user's choice from the menu
    user_choice = display_menu()

    # Check the user's choice
    if user_choice == "1":
        # ICMP Ping Sweep mode
        # Prompt the user for the target network
        target_network = input("Enter the target network (CIDR format, e.g., 192.168.1.0/24): ")
        # Perform the ICMP Ping Sweep and get the list of online hosts
        online_hosts = icmp_ping_sweep(target_network)

        # Print the list of online hosts
        print("\nOnline Hosts:")
        for host in online_hosts:
            print(host)
    elif user_choice == "2":
        # TCP Port Range Scanner mode
        # Prompt the user for the target IP address
        target_ip = input("Enter the target IP address: ")
        # Prompt the user for the port range
        port_range = range(int(input("Enter the starting port: ")), int(input("Enter the ending port: ")) + 1)
        # Perform the TCP Port Range Scanner and get the scan results
        open_ports, closed_ports, filtered_ports = tcp_port_scanner(target_ip, port_range)

        # Print the scan results
        print("\nScan Results:")
        print(f"Open Ports: {open_ports}")
        print(f"Closed Ports: {closed_ports}")
        print(f"Filtered Ports: {filtered_ports}")
    else:
        # Print a message indicating an invalid choice
        print("Invalid choice. Please enter 1 or 2.")
