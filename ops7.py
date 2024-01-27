#!/usr/bin/env python3

# Script Name:                  File Encryption Part 2
# Author:                       Kevin Hoang
# Date of latest revision:      1/17/2024
# Purpose:                      Script that encrypts a single file
# Execution:                    
# Resources:                    https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-06/challenges/DEMO.md
#                               https://pypi.org/project/cryptography/
#                               https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python

# Imports Fernet from cryptography.fernet and it imports OS for handling file operations and checking file existence.
from cryptography.fernet import Fernet
import os
import time

# Function to generate and write an encryption key to a file
def writekey():
    enckey = Fernet.generate_key()  # Generate an encryption key
    with open("enckey.key", "wb") as keyfile:  # Open a file to write the key
        keyfile.write(enckey)  # Write the key to the file

# Function to load the encryption key from a file
def loadkey():
    return open("enckey.key", "rb").read()  # Open the file containing the key and read its contents

# Write the encryption key to a file
writekey()
# Load the encryption key from the file
key = loadkey()
# Create a Fernet cipher object using the loaded key
f = Fernet(key)

# Function to encrypt files using the provided key
def encryptfiles(filename, key):
    key = key  # Assign the provided key
    with open(filename, "rb") as file:  # Open the file to be encrypted
        filedata = file.read()  # Read the file data
    encdata = f.encrypt(filedata)  # Encrypt the file data
    with open(filename, "wb") as file:  # Write the encrypted data back to the file
        file.write(encdata)

# Function to decrypt files using the provided key
def decryptfiles(filename, key):
    key = key  # Assign the provided key
    with open(filename, 'rb') as file:  # Open the encrypted file
        encdata = file.read()  # Read the encrypted data
    decdata = f.decrypt(encdata)  # Decrypt the data
    with open(filename, "wb") as file:  # Write the decrypted data back to the file
        file.write(decdata)

print("We are going to do some recursive encryption/decription")
time.sleep(3)  # Pause for 3 seconds

while True:  # Infinite loop
    choice = str(input("Do you want to recursively encrypt[e] or decrypt[d]? \nPick d or e: "))  # Prompt for encryption or decryption choice
    firstdir = str(input("What is the root path to encrypt or decrypt? "))  # Prompt for the root path

    try:
        if choice == str("e"):  # If encryption is chosen
            topdown = '.'  # Start from the top directory
            for path, dirs, files in os.walk(firstdir):  # Walk through the directory tree
                for file in files:  # For each file in the directory
                    filepath = os.path.join(path, file)  # Get the full file path
                    encryptfiles(filepath, key)  # Encrypt the file
                    print("Successfully recursively encrypted from the provided path\n")  # Print success message
                    time.sleep(2)  # Pause for 2 seconds

        elif choice == str("d"):  # If decryption is chosen
            topdown = '.'  # Start from the top directory
            for path, dirs, files in os.walk(firstdir):  # Walk through the directory tree
                for file in files:  # For each file in the directory
                    filepath = os.path.join(path, file)  # Get the full file path
                    if os.path.exists(filepath):  # Check if the file exists
                        decryptfiles(filepath, key)  # Decrypt the file
                        print("Successfully recursively decrypted from the provided path\n")  # Print success message
                        time.sleep(2)  # Pause for 2 seconds
                    else:
                        print(f'{filepath} not found')  # Print message if file not found
                        time.sleep(2)  # Pause for 2 seconds

    except ValueError:
        raise ValueError("Choose either d or e")  # Raise an error if invalid choice is made
