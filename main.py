#!/usr/bin/env python3
from privacy import sender
from privacy import password
import random
import smtplib

class SecretSanta:
    def __init__(self):
        self.info = dict()
        self.selection = dict()
        self.participants = 0
    
    def get_info(self):
        self.participants = input("How many people are paricipating?: ")
        self.budget = int(input("What is the budget?: "))
        
        for i in range(1, self.participants+1):
            name = input(f"Name of partcipant {i}?: ")
            email = input("What is their email?: ")
            self.info[name] = [email]
    
    def assign(self):
        pass
    
    def send_email(self):
        pass
    
    def start(self):
        pass
    
if __name__ == "__main__"
    
    
        
        
    