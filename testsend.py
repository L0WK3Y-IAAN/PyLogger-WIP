#!/usr/bin/env python3
import smtplib
import mimetypes
from email.message import EmailMessage
# Create message and set text content
msg = EmailMessage()
msg['Subject'] = 'This email contains an attachment'
msg['From'] = 'anonymous@anon.org'
msg['To'] = 'l0wk3yiaan@protonmail.com'
# Set text content
msg.set_content('Please see attached file')
def attach_file_to_email(email, filename):
    """Attach a file identified by filename, to an email message"""
    with open(filename, 'rb') as fp:
        file_data = fp.read()
        maintype, _, subtype = (mimetypes.guess_type(filename)[0] or 'application/octet-stream').partition("/")
        email.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=filename)
# Attach files
attach_file_to_email(msg, "log.txt")
def send_mail_smtp(mail, host, username, password):
    s = smtplib.SMTP(host)
    s.starttls()
    s.login(username, password)
    s.send_message(msg)
    s.quit()
send_mail_smtp(msg, 'smtp.mailgun.org', 'l0wk3yiaan@protonmail.com', 'sae7ooka0S')