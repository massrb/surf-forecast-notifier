import os
import smtplib
from email.message import EmailMessage

def send_email(subject, body, to_email):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    gmail_user = os.environ.get("GMAIL_USER")
    gmail_pass = os.environ.get("GMAIL_APP_PASSWORD")

    if not gmail_user or not gmail_pass:
        raise Exception("GMAIL_USER and GMAIL_APP_PASSWORD must be set in env")

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = gmail_user
    msg["To"] = to_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(gmail_user, gmail_pass)
        server.send_message(msg)
