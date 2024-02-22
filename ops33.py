#!/usr/bin/env python3
# Script Name:                  Ops Challenge: Singnature-based malware Detection Part 3 of 3
# Author:                       Kevin Hoang
# Date of latest revision:      02/21/2024
# Resource:                     Juan Cano
# Purpose: 
'''The script is designed for signature-based malware detection. It allows users to search for specific files within directories, 
    computes their MD5 hash, and optionally checks the hash against the VirusTotal database. It provides a menu-driven interface allowing users to search for files, 
    list available directories, or exit the program.'''
import os
import hashlib
import requests  # Ensure the 'requests' library is installed for fallback or additional HTTP requests

def hash_file(filename):
    """This function returns the MD5 hash of the file passed into it."""
    h = hashlib.md5()
    try:
        with open(filename, 'rb') as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
                h.update(chunk)
    except IOError as e:
        print(f"\033[91mError opening file: {e}\033[0m")
        return None
    return h.hexdigest()

def check_virustotal(file_hash):
    """Checks the given hash against the VirusTotal database using the external script."""
    apikey = os.getenv('API_KEY_VIRUSTOTAL')
    if not apikey:
        print("\033[91mAPI key for VirusTotal is not set. Please set the API_KEY_VIRUSTOTAL environment variable.\033[0m")
        return
    # Construct the command to call the external script
    query = f'python3 virustotal-search.py -k {apikey} -m {file_hash}'
    # Execute the constructed command
    os.system(query)

def search_file(file_name, directory):
    hits = 0
    files_searched = 0

    if not os.path.isdir(directory):
        print("\033[91mError: Invalid directory path.\033[0m")
        return 0, 0

    print(f"\033[96mSearching for '{file_name}' in '{directory}'...\033[0m")

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == file_name:
                hits += 1
                file_path = os.path.join(root, file)
                print(f"\033[92mFound: {file_path}\033[0m")
                file_hash = hash_file(file_path)
                if file_hash and input("\033[93mCheck this file hash with VirusTotal? (y/n): \033[0m").strip().lower() == 'y':
                    check_virustotal(file_hash)
            files_searched += 1
            print_progress(files_searched)

    return hits, files_searched

def print_progress(files_searched):
    print(f"\033[95mFiles searched: {files_searched}\033[0m", end='\r')

def list_directories():
    current_directory = os.getcwd()
    print("\033[96mAvailable directories:\033[0m")
    for item in os.listdir("/"):
        item_path = os.path.join("/", item)
        if os.path.isdir(item_path):
            if item_path == current_directory:
                print(f"\033[94m- {item_path} (Current Directory)\033[0m")
            else:
                print(f"\033[94m- {item_path}\033[0m")
    print()

def search_files():
    file_name = input("\033[93mEnter the file name to search for: \033[0m").strip()
    directory = input("\033[93mEnter the directory to search in or type 'list' to see available directories: \033[0m").strip()

    if directory.lower() == "list":
        list_directories()
        return

    if not file_name:
        print("\033[91mError: Please provide a file name.\033[0m")
        return

    if not directory:
        print("\033[91mError: Please provide a directory.\033[0m")
        return

    if not os.path.exists(directory):
        print("\033[91mError: Directory does not exist.\033[0m")
        return

    hits, files_searched = search_file(file_name, directory)

    if hits == 0 and files_searched == 0:
        print("\n\033[91mNo files searched due to directory error.\033[0m")
    else:
        print(f"\n\033[96mTotal files searched: {files_searched}\033[0m")
        print(f"\033[92mTotal hits found: {hits}\033[0m")

def main():
    while True:
        print("\n\033[95mMenu:\033[0m")
        print("\033[96m1. Search for files\033[0m")
        print("\033[96m2. List available directories\033[0m")
        print("\033[96m3. Exit\033[0m")

        choice = input("\033[95mEnter your choice: \033[0m").strip()

        if choice == "1":
            search_files()
        elif choice == "2":
            list_directories()
        elif choice == "3":
            print("\033[92mExiting...\033[0m")
            break
        else:
            print("\033[91mInvalid choice. Please enter 1, 2, or 3.\033[0m")

if __name__ == "__main__":
    main()
