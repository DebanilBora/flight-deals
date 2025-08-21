import os
import smtplib
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
        self.email = os.getenv("MY_EMAIL")
        self.password = os.getenv("MY_PASSWORD")
        self.smtp_address = os.getenv("SMTP_ADDRESS")

    def send_sms(self, message):
        self.client.messages.create(
            body=message,
            from_=os.getenv("TWILIO_FROM"),
            to=os.getenv("TWILIO_TO")
        )

    def send_emails(self, emails, message):
        for email in emails:
            with smtplib.SMTP(self.smtp_address, port=587) as connection:
                connection.starttls()
                connection.login(user=self.email, password=self.password)
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Flight Deal!\n\n{message}".encode("utf-8")
                )
