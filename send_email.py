import os
import time
import hashlib
import subprocess

# Folder path to monitor
folder_path = r'C:\Users\test\Documents\Test'

# Path to the second script (send_email.py)
send_email_script_path = r'C:\Users\test\Documents\Scripts\send_email.py'

# Set to keep track of file hashes to avoid duplicates
sent_files_hashes = set()

# Function to calculate the hash of a file
def calculate_file_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()

# Function to find new PDF files
def find_new_files():
    new_files = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(folder_path, file_name)
            file_hash = calculate_file_hash(file_path)
            if file_hash not in sent_files_hashes:
                new_files.append(file_path)
                sent_files_hashes.add(file_hash)
    return new_files

# Main loop to run every 10 minutes
while True:
    new_files = find_new_files()
    if new_files:
        # Call the second script to send an email with the new files
        subprocess.call(['python', send_email_script_path] + new_files)
    
    # Wait for 10 minutes before checking again
    time.sleep(600)
