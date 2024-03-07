#!/usr/bin/python3
# Script Name:                  Ops Challenge: Create a Port Scanner
# Author:                       Kevin Hoang
# Date of latest revision:      02/21/2024
# Resource:                     https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-42/challenges/DEMO.md
# Purpose:                      The purpose of this script is to determine if a target port is open or closed, using strictly Python 3 commands. 
#                               To do so, we’ll be importing the socket module, a low-level networking interface for Python.

import socket

# Create a socket object using IPv4 address family and TCP protocol
sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set a timeout value for socket operations
timeout = # TODO: Set a timeout value here.
sockmod.settimeout(timeout)

# Prompt user to input the target host IP address
hostip = # TODO: Collect a host IP from the user.

# Prompt user to input the target port number and convert it to an integer
portno = # TODO: Collect a port number from the user, then convert it to an integer data type.

# Define a function to perform port scanning
def portScanner(portno):
    # Check if the specified port is open or closed
    if sockmod.FUNCTION((hostip, portno)): # TODO: Replace "FUNCTION" with the appropriate socket.function call as found in the [socket docs](https://docs.python.org/3/library/socket.html)
        print("Port closed")
    else:
        print("Port open")

# Call the portScanner function with the specified port number
portScanner(port)
