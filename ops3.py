# Python

# Script Name:                  Ops Challenge: Uptime Sensor Tool Part 2 of 2
# Author:                       Kevin Hoang
# Date of latest revision:      1/10/2024
# Purpose:                      Monitor the status of hosts using ICMP packets
# Execution:                    ops3.py


# For time-related functions
import time  

# For working with date and time
from datetime import datetime  

# For working with the operating system (path, file operations)
import os  

# Third-party library for ICMP ping operations
from ping3 import ping  

# This is a module for sending emails
import smtplib

# This allows the creation of email content
from email.mime.text import MIMEText

# This is the email configuration
# This is an email that will receive the notification 
# Change it to an email you have access to for verification.
recipient_email = 'myers776@gmail.com'  # testers need to use a different email.

# This checks if IP can be pinged 
def check_host_status(target_ip):
    response = ping(target_ip, timeout=1)
    return response is not None

# This logs an event to a text file
def log_event(target_ip, target_hostname, timestamp, status):
    # This formats the log entry
    log_entry = f"{timestamp} - Host {target_ip} ({target_hostname} is {'up' if status else 'down'})"

    # This creates a log file in the Documents folder with a timestamped name
    log_filename = os.path.join(os.path.expanduser("~"), "Documents", "event_log.txt")
    with open(log_filename, 'a') as log_file:
        log_file.write(log_entry + '\n')
    
    # Print the log entry
    print(log_entry)

# This sends an email notification using a localhost SMTP server
def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'stacymyers2000@gmail.com'
    msg['To'] = recipient_email

    # This is the App password for the Gmail email
    app_password = 'znsr eqhg rtid orxh'
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('stacymyers2000@gmail.com', app_password)
        server.sendmail('stacymyers2000@gmail.com', [recipient_email], msg.as_string())

def main():
    # Welcome message for the user
    print("Welcome to the Uptime Sensor Tool. This script will evaluate if a host is up or down on the Local Area Network (LAN).")
    print("The sensor tool will ping continuously. If you want to exit the tool, please press ctrl + c.")
    
    # Accept user input for the target IP address and hostname
    target_ip = input("Please enter an IP address of a host on the LAN: ")
    target_hostname = input("Please enter the hostname associated with the IP address you entered:  ")
   
    # This loop is used to ping the target every two seconds
    while True:
        # Check the status of the host
        status = check_host_status(target_ip)

        # Check if the previous status exists and has changed
        if hasattr(main, "previous_status") and main.previous_status != status:
            # Get the current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Log the event
            log_event(target_ip, target_hostname, timestamp, status)

            # Create an email subject
            subject = f"Host Status Changed: {target_ip} ({target_hostname})"
            
            # Create the email body
            body = f"Host status changed at {timestamp}\n\nPrevious Status: {'Up' if main.previous_status else 'Down'}\nCurrent Status: {'Up' if status else 'Down'}"
            
            # Send the email notification
            send_email(subject, body)
        
        # Set the current status as the previous status for the next iteration
        main.previous_status = status
        
        # Sleep for 2 seconds before the next iteration
        time.sleep(2)

if __name__ == "__main__":
    # Run the main function when the script is executed
    main()

