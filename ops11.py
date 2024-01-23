# Python

# Script Name:                  Network Security Tool with Scapy Part 1 of 3
# Author:                       Kevin Hoang
# Date of latest revision:      1/22/2024
# Purpose:                      Script that creates a TCP Port Range Scanner that tests whether a TCP port is open or closed
# Execution:                    ops11.py
# Resources:                    https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-06/challenges/DEMO.md
#                               https://scapy.readthedocs.io/en/latest/introduction.html#
#                               https://scapy.readthedocs.io/en/latest/extending.html

# Import the Scapy library
import scapy.all as scapy

# Define a function to perform TCP port scanning
def tcp_port_scanner(target_ip, port_range):
    # Lists to store open, closed, and filtered ports
    open_ports = []
    closed_ports = []
    filtered_ports = []

    # Loop through each port in the specified range
    for port in port_range:
        # Send a SYN packet to the target IP and specified port
        response = scapy.sr1(scapy.IP(dst=target_ip) / scapy.TCP(dport=port, flags="S"), timeout=1, verbose=0)

        # Check if there is a response and if it contains TCP layer
        if response and scapy.TCP in response:
            # If SYN-ACK flag (0x12) received, send a RST packet to close the connection gracefully
            if response[scapy.TCP].flags == 0x12:
                scapy.send(scapy.IP(dst=target_ip) / scapy.TCP(dport=port, flags="R"), verbose=0)
                open_ports.append(port)
                print(f"Port {port} is open.")
            # If RST flag (0x14) received, notify that the port is closed
            elif response[scapy.TCP].flags == 0x14:
                closed_ports.append(port)
                print(f"Port {port} is closed.")
            # If no flag is received, notify that the port is filtered and silently dropped
            else:
                filtered_ports.append(port)
                print(f"Port {port} is filtered and silently dropped.")

    # Return the lists of open, closed, and filtered ports
    return open_ports, closed_ports, filtered_ports

# Entry point of the script
if __name__ == "__main__":
    # Replace with the target IP and port range
    target_ip = "127.0.0.1"
    port_range = range(1, 1025)

    # Call the TCP port scanner function
    open_ports, closed_ports, filtered_ports = tcp_port_scanner(target_ip, port_range)

    # Print the scan results
    print("\nScan Results:")
    print(f"Open Ports: {open_ports}")
    print(f"Closed Ports: {closed_ports}")
    print(f"Filtered Ports: {filtered_ports}")

