import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_html_email(subject: str, html_body: str) -> None:
    """Send an HTML email via Gmail SMTP using App Password auth."""
    sender = os.environ['GMAIL_SENDER']
    recipient = os.environ['GMAIL_RECIPIENT']
    password = os.environ['GMAIL_APP_PASSWORD']

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    msg.attach(MIMEText(html_body, 'html'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())
