#!/usr/bin/env python3
import random
import os
from mailjet_rest import Client
import time

class SecretSanta:
    """
    A class to represent a Secret Santa game.

    Attributes:
    -----------
    participants : dict
        A dictionary mapping participant names to their email addresses.
    html_template : str
        The HTML template for the email to be sent to participants.

    Methods:
    --------
    assign(delay_seconds=8):
        Assigns Secret Santa pairs and sends emails to each giver with their receiver's name.
    send_email(giver, receiver):
        Sends an email to the giver with details about their Secret Santa receiver.
    """
    def __init__(self, participants):
        self.participants = participants
        # Load the HTML content from the file
        with open('/home/cjbutter/santa_project/email_template.html', 'r') as file:
            self.html_template = file.read()

    def assign(self, delay_seconds=8):
        """
        Assigns Secret Santa pairs and sends emails to each giver with their receiver's name.

        Parameters:
         -----------
        delay_seconds : int, optional
        The delay in seconds between sending each email (default is 8 seconds).

        Description:
        ------------
        This method shuffles the participants, pairs them up for the Secret Santa game,
        and sends an email to each participant (giver) with the name of their assigned receiver.
        """
        names = list(self.participants.keys())
        random.shuffle(names)
        pairs = list(zip(names, names[1:] + [names[0]]))
         
        for giver, receiver in pairs:
            self.send_email(giver, receiver)
            time.sleep(delay_seconds)

    def send_email(self, giver, receiver):
        """
        Sends an email to the giver with details about their Secret Santa receiver.

        Parameters:
        -----------
        giver : str
        The name of the person giving the gift.
        receiver : str
        The name of the person receiving the gift from the giver.

        Description:
        ------------
        Constructs an email with the details of the Secret Santa assignment and sends it to the giver.
        Utilizes the Mailjet API for sending emails.
        """
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
            print(f"Email successfully sent to {giver}")
        else:
            print(f"Failed to send email to {giver}. Status code: {result.status_code}")


def get_participants():
    """
    Collects participant information for the Secret Santa game.

    Returns:
    --------
    dict
        A dictionary containing participant names and their corresponding email addresses.

    Description:
    ------------
    Prompts the user to input participant names and email addresses. Continues to prompt
    until the user indicates completion by typing 'done'. Returns a dictionary of the collected
    information.
    """
    participants = {}
    while True:
        name = input("Enter participant's name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        email = input(f"Enter {name}'s email address: ")
        participants[name] = email
    return participants

if __name__ == "__main__":
    participants = get_participants()
    santa = SecretSanta(participants)
    santa.assign()
    
    
        
        
    