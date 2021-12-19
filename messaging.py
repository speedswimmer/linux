import smtplib
import os
from email.message import EmailMessage


EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

def send_email(message):
    msg = EmailMessage()
    msg['Subject'] = 'Presence change!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'hartmannmatthias7@googlemail.com'
    msg.set_content(message)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)