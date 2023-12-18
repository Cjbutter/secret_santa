#!/usr/bin/env python3
import random
import smtplib
import ssl
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SecretSanta:
    def __init__(self):
        self.participants = {}

    def get_info(self):
        # Hardcoded testing participants
        testing_participants = {
            "Svetlana1": "svetlana1@example.com",
            "Svetlana2": "svetlana2@example.com",
            "Svetlana3": "svetlana3@example.com",
            "Joao": "joao@example.com",
    }

    # Use hardcoded participants for testing
        self.participants = testing_participants

    def assign(self, delay_seconds=10):
        names = list(self.participants.keys())
        random.shuffle(names)

        pairs = list(zip(names, names[1:] + [names[0]]))

        for giver, receiver in pairs:
            print(f"{giver} is the Secret Santa for {receiver}")
            self.send_email(giver, receiver)
            time.sleep(delay_seconds)

    def send_email(self, sender, receiver):
        # Set up the MIME
        message = MIMEMultipart()
        message["From"] = "cjbutter@gmail.com"
        message["To"] = self.participants[receiver]
        message["Subject"] = "Secret Santa Assignment"

        # Attach the body to the email
        body = f"You are the Secret Santa for {receiver}"
        message.attach(MIMEText(body, "plain"))

        # Set up the SMTP server
        smtp_server = "smtp.gmail.com"
        port = 465

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Log in to the SMTP server with the app password
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(self.participants[sender], "dqxe tadf shuk vuoh")

            print(f"Sending email from: {self.participants[sender]} to: {self.participants[receiver]}")
            # Send the email
            server.sendmail(self.participants[sender], self.participants[receiver], message.as_string())
        
        
    

if __name__ == "__main__":
    santa = SecretSanta()
    santa.get_info()
    santa.assign()

    
    
        
        
    