import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_html_email(subject: str, html_body: str) -> None:
    """Send an HTML email via Gmail SMTP using App Password auth."""
    sender = os.environ.get('GMAIL_SENDER')
    recipient = os.environ.get('GMAIL_RECIPIENT')
    password = os.environ.get('GMAIL_APP_PASSWORD')

    if not all([sender, recipient, password]):
        raise ValueError(
            "Missing required env vars: GMAIL_SENDER, GMAIL_RECIPIENT, GMAIL_APP_PASSWORD"
        )

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    msg.attach(MIMEText(html_body, 'html'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
    except smtplib.SMTPAuthenticationError:
        raise ValueError("Gmail authentication failed — check GMAIL_APP_PASSWORD")
    except smtplib.SMTPException as e:
        raise RuntimeError(f"Failed to send email: {e}")
