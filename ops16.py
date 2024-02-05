#!/usr/bin/env python3 

# Script Name:                  Ops Challenge: Automated Brute Force Wordlist Attack Tool Part 1 of 3
# Author:                       Kevin Hoang
# Date of latest revision:      1/29/2024
# Purpose:                      Script that creates a  a custom tool that performs brute force attacks to better 
#                               understand the types of automation employed by adversaries.
# Execution:                    ops16.py
# Resources:                    https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-16/challenges/DEMO.md
#                               https://www.geeksforgeeks.org/iterate-over-a-set-in-python/
#                               https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-16/challenges/main.py


# Imports time module for handling operations that deal with time and ssl module for SSL/TLS support
import time  # Importing the time module for time-related operations
import ssl   # Importing the ssl module for SSL/TLS support

# Function to perform Mode 1: Offensive; Dictionary Iterator
def offensive_mode(file_path):
   delay = float(input("Enter the delay between words (in seconds): "))  # Prompting the user to input delay between words, converting it to float
   max_lines = int(input("Enter the maximum number of lines to display: "))  # Prompting the user to input the maximum number of lines to display, converting it to integer
   line_count = 0  # Initializing a variable to count lines

   try:  # Starting a try block for handling file-related operations
        with open(file_path, 'r') as file:  # Opening the file in read mode and assigning it to the variable 'file'
           while True:  # Starting a loop to iterate through lines in the file
                word = file.readline().strip()  # Reading a line from the file and stripping whitespace characters
                if not word:  # Checking if the word is empty
                    break  # Exiting the loop if the word is empty
                print(word)  # Printing the word
                line_count += 1  # Incrementing the line count
                if line_count >= max_lines:  # Checking if the line count exceeds the maximum lines to display
                    break  # Exiting the loop if the maximum lines to display is reached
                time.sleep(delay)  # Pausing execution for the specified delay
   except FileNotFoundError:  # Handling the case where the file is not found
        print("File not found.")

# Function to perform Mode 2: Defensive; Password Recognized
def defensive_mode(file_path):
    user_input = input("Enter a word to search: ")  # Prompting the user to input a word
    try:  # Starting a try block for handling file-related operations
        with open(file_path, 'r', errors='ignore') as file:  # Opening the file in read mode, ignoring decoding errors
            while True:  # Starting a loop to iterate through lines in the file
                line = file.readline()  # Reading a line from the file
                if not line:  # Checking if the line is empty
                    break  # Exiting the loop if the line is empty
                word = line.strip()  # Stripping whitespace characters from the line
                if user_input == word:  # Checking if the user input matches the word from the file
                    print("The word is in the word list.")  # Printing a message indicating the word is found
                    return  # Exiting the function
            print("The word is not in the word list.")  # Printing a message indicating the word is not found
    except FileNotFoundError:  # Handling the case where the file is not found
        print("File not found.")

if __name__ == "__main__":  # Checking if the script is run directly
   mode = input("Select a mode (1 for Offensive, 2 for Defensive): ")  # Prompting the user to select a mode
   file_path = "smaller_rockyou.txt"  # Setting the file path to a smaller wordlist file

   if mode == '1':  # Checking if the selected mode is 1 (Offensive mode)
        offensive_mode(file_path)  # Calling the offensive_mode function
   elif mode == '2':  # Checking if the selected mode is 2 (Defensive mode)
        defensive_mode(file_path)  # Calling the defensive_mode function
   else:  # Handling the case of an invalid mode selection
        print("Invalid mode selection. Please choose 1 or 2.")  # Printing a message indicating an invalid mode selection
