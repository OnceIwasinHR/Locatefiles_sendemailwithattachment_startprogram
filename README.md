# task_schaduler.py
Written in .py - Primary functuion: 1. Start Outlook or any other program that is needed at a designated time every day if server/machine is on, 2. Locate a file if placed on designated folder, add the file as attachment, send a email to designated parties using the file, handle errors if found and append as needed.
 a. Ensure all env variables are installed including python 3.10 minimum.
  b.Goal was to elimnate need for schadule task windows, and ensure the files are collected and sent to designated parties, at a frequency when they are available in the work folder.
   c.Ensure to test update the string values in script paths, 3 scripts needed to work side by side. If no need for another seconedary program to start in a loop, only 2nd .py LocateFiles_CallEmail.py can work with 3rd script: send_email.py
