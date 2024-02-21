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
    h = hashlib.sha1()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()

def search_file(file_name, directory):
    hits = 0
    files_searched = 0

    if not os.path.isdir(directory):
        print("Error: Invalid directory path.")
        return 0, 0

    print(f"Searching for '{file_name}' in '{directory}'...")

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == file_name:
                hits += 1
                file_path = os.path.join(root, file)
                print("\033[93mFound:", file_path, "\033[0m")
                if input("Calculate SHA-1 hash of this file? (y/n): ").strip().lower() == 'y':
                    print("SHA-1:", hash_file(file_path))
            files_searched += 1
            print_progress(files_searched)

    return hits, files_searched

def print_progress(files_searched):
    print(f"Files searched: {files_searched}", end='\r')

def list_directories():
    current_directory = os.getcwd()
    print("Available directories:")
    for item in os.listdir("/"):
        item_path = os.path.join("/", item)
        if os.path.isdir(item_path):
            if item_path == current_directory:
                print("\033[95m- ", item_path, "(Current Directory)\033[0m")
            else:
                print("\033[95m- ", item_path, "\033[0m")
    print()

def search_files():
    file_name = input("Enter the file name to search for: ").strip()
    directory = input("Enter the directory to search in or type 'list' to see available directories: ").strip()

    if directory.lower() == "list":
        list_directories()
        return

    if not file_name:
        print("Error: Please provide a file name.")
        return

    if not directory:
        print("Error: Please provide a directory.")
        return

    if not os.path.exists(directory):
        print("Error: Directory does not exist.")
        return

    hits, files_searched = search_file(file_name, directory)

    if hits == 0 and files_searched == 0:
        print("\nNo files searched due to directory error.")
    else:
        print("\nTotal files searched:", files_searched)
        print(f"\033[93mTotal hits found: {hits}\033[0m")

def main():
    while True:
        print("\033[32m\nMenu:\033[0m")
        print("1. Search for files")
        print("2. List available directories")
        print("3. Exit")

        choice = input("\033[32mEnter your choice: \033[0m").strip()

        if choice == "1":
            search_files()
        elif choice == "2":
            list_directories()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()