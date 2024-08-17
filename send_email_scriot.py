import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys

# Email credentials
smtp_server = 'smtp.example.com'  # Replace with your SMTP server
smtp_port = 587  # Replace with your SMTP port (587 for TLS)
smtp_user = 'your_email@example.com'  # Replace with your email address
smtp_password = 'your_password'  # Replace with your email password

# Email details
sender_email = smtp_user  # Sender's email address
recipient_email = 'recipient@example.com'  # Replace with recipient's email address
subject = 'New PDF Files Detected'  # Subject line for the email

# Create the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject

# Body of the email
body = 'Please find the attached PDF files that were recently detected in the folder.'
msg.attach(MIMEText(body, 'plain'))

# Attach files to the email
for file_path in sys.argv[1:]:
    attachment = MIMEBase('application', 'octet-stream')
    with open(file_path, 'rb') as file:
        attachment.set_payload(file.read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
    msg.attach(attachment)

# Send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)
    server.quit()
    print('Email sent successfully!')
except Exception as e:
    print(f'Failed to send email: {e}')
