import os
import time

# Define the PowerShell commands
stop_process = 'Stop-Process -Name "OUTLOOK"'
start_process = 'Start-Process -FilePath \'"C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"\' '

# Function to run a PowerShell command
def run_powershell_command(command):
    os.system(f'powershell.exe -Command {command}')

# Function to check if a process is running
def is_process_running(process_name):
    check_command = f'Get-Process -Name {process_name} -ErrorAction SilentlyContinue'
    result = os.system(f'powershell.exe -Command "{check_command}"')
    return result == 0

# Run this task in a loop with a 24-hour interval (86,400 seconds)
while True:
    # Check if Outlook is running
    if is_process_running("OUTLOOK"):
        # Stop Outlook if it is running
        run_powershell_command(stop_process)
    
    # Wait for 30 seconds
    time.sleep(30)
    
    # Start Outlook again
    run_powershell_command(start_process)
    
    # Wait for xxx min - use seconds x by minute then insert it time before running the task again
    time.sleep(60)
