import os
import time
import smtplib
from email.message import EmailMessage


def send_mail():
    #grap environment variables where data is stored
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    receipient = "***"
    today = (time.strftime("%d-%m-%y"))
    daily_logfile = ("/home/pi/Scripts/" + today + "-log.txt")

# defining Email body
    msg = EmailMessage()
    msg['Subject'] = 'FritzBox! HU Status-Update'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = receipient
    msg.set_content('Image attached...\n\nCU, SecureGuard')

    with open(daily_logfile, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    #msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

send_mail()
