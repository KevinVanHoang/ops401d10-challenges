#!/usr/bin/env python3
# Script Name:                  Ops Challenge: Singnature-based malware Detection Part 2 of 3
# Author:                       Kevin Hoang 
# Date of latest revision:      02/20/2024
# Purpose:                      Basic antivirus tool in Python with a secondary Hash Validation feature 
# Resource:                     Juan Cano


'''This code allows users to search for specific files within a specified directory and its subdirectories. 
Then, it offers the option to calculate and display the SHA-1 hash of any found files. The purpose is to help verify the integrity of files, 
ensuring they have not been altered or corrupted, and to facilitate locating files within complex directory structures.'''

import os
import hashlib

def hash_file(filename):
    """This function returns the SHA-1 hash of the file passed into it"""
    h = hashlib.sha1()  # Create a SHA-1 hash object
    with open(filename, 'rb') as file:  # Open the file in binary mode
        chunk = 0
        while chunk != b'':  # Continue reading chunks until end of file
            chunk = file.read(1024)  # Read a chunk of 1024 bytes
            h.update(chunk)  # Update the hash object with the chunk data
    return h.hexdigest()  # Return the hexadecimal digest of the hash

def search_file(file_name, directory):
    hits = 0  # Counter for found files
    files_searched = 0  # Counter for files searched

    if not os.path.isdir(directory):  # Check if the directory exists
        print("Error: Invalid directory path.")
        return 0, 0  # Return 0 hits and 0 files searched if directory is invalid

    print(f"Searching for '{file_name}' in '{directory}'...")

    for root, dirs, files in os.walk(directory):  # Iterate over the directory tree
        for file in files:  # Iterate over files in each directory
            if file == file_name:  # Check if the filename matches the target
                hits += 1  # Increment hit count
                file_path = os.path.join(root, file)  # Get the full path of the found file
                print("\033[93mFound:", file_path, "\033[0m")  # Print the found file path
                if input("Calculate SHA-1 hash of this file? (y/n): ").strip().lower() == 'y':  # Ask user to calculate hash
                    print("SHA-1:", hash_file(file_path))  # Calculate and print SHA-1 hash
            files_searched += 1  # Increment files searched counter
            print_progress(files_searched)  # Print progress

    return hits, files_searched  # Return total hits and files searched

def print_progress(files_searched):
    print(f"Files searched: {files_searched}", end='\r')  # Print files searched with carriage return

def list_directories():
    current_directory = os.getcwd()  # Get current working directory
    print("Available directories:")
    for item in os.listdir("/"):  # Iterate over items in root directory
        item_path = os.path.join("/", item)  # Get full path of item
        if os.path.isdir(item_path):  # Check if item is a directory
            if item_path == current_directory:  # Check if item is current directory
                print("\033[95m- ", item_path, "(Current Directory)\033[0m")  # Print item path in magenta as current directory
            else:
                print("\033[95m- ", item_path, "\033[0m")  # Print item path in magenta
    print()

def search_files():
    file_name = input("Enter the file name to search for: ").strip()  # Prompt user for file name
    directory = input("Enter the directory to search in or type 'list' to see available directories: ").strip()  # Prompt user for directory

    if directory.lower() == "list":  # If user wants to list directories
        list_directories()  # Call list_directories function
        return

    if not file_name:  # Check if file name is provided
        print("Error: Please provide a file name.")
        return

    if not directory:  # Check if directory is provided
        print("Error: Please provide a directory.")
        return

    if not os.path.exists(directory):  # Check if directory exists
        print("Error: Directory does not exist.")
        return

    hits, files_searched = search_file(file_name, directory)  # Call search_file function

    if hits == 0 and files_searched == 0:  # If no files were searched due to directory error
        print("\nNo files searched due to directory error.")
    else:
        print("\nTotal files searched:", files_searched)  # Print total files searched
        print(f"\033[93mTotal hits found: {hits}\033[0m")  # Print total hits found in yellow

def main():
    while True:  # Loop to display menu until user chooses to exit
        print("\033[32m\nMenu:\033[0m")
       
