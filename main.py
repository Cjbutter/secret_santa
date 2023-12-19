#!/usr/bin/env python3
import random
import os
from mailjet_rest import Client
import time

class SecretSanta:
    def __init__(self):
        self.participants = {}
        # Load the HTML content from the file
        with open('/home/cjbutter/santa_project/email_template.html', 'r') as file:
            self.html_template = file.read()
        

    def get_info(self):
        # Hardcoded testing participants
        testing_participants = {
            "Svetlana1": "cjbutter@gmail.com",
            "Svetlana2": "svetlanalysikova271@gmail.com",
            "Svetlana3": "arrowphoto11611253svetlana@gmail.com",
            "Joao": "jopaamcx@hotmail.com",
    }

    # Use hardcoded participants for testing
        self.participants = testing_participants

    def assign(self, delay_seconds=8):
        names = list(self.participants.keys())
        random.shuffle(names)
        pairs = list(zip(names, names[1:] + [names[0]]))
         
        for giver, receiver in pairs:
            print(f"Sending email to {giver} who is the Secret Santa for {receiver}")
            self.send_email(giver, receiver)
            time.sleep(delay_seconds)

    def send_email(self, giver, receiver):
        giver_email = self.participants[giver]
        # Replace {receiver} placeholder with the actual name in the HTML content
        html_content = self.html_template.replace("{receiver}", receiver)
        email_data = {
            'Messages': [
                {
                    "From": {
                        "Email": "cjbutter@gmail.com",
                        "Name": "Pai Natal"
                    },
                    "To": [
                        {
                            "Email": giver_email,
                            "Name": giver
                        }
                    ],
                    "Subject": "Message from Pai Natal",
                    "TextPart": f"You are the Secret Santa for {receiver}",
                    "HTMLPart": html_content
                }
            ]
        }
       
        api_key = os.environ['MJ_APIKEY_PUBLIC']
        api_secret = os.environ['MJ_APIKEY_PRIVATE']
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        
        
        result = mailjet.send.create(data=email_data)

        if result.status_code == 200:
            print(f"Email sent successfully to {receiver}")
        else:
            print(f"Failed to send email to {receiver}. Status code: {result.status_code}")
        
    

if __name__ == "__main__":
    santa = SecretSanta()
    santa.get_info()
    santa.assign()

    
    
        
        
    