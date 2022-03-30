# -*- coding: utf-8 -*-
"""Automatic email.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IzA6Dw_6poGc51A0AjJtnPQFbjlaKEwO
"""

import os 
#provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc. 

import random 
#Random integer values can be generated with the randint() function. This function takes two arguments: the start and the end of the range for the generated integer values. Random integers are generated within and including the start and end of range values, specifically in the interval [start, end]

import smtplib 
#used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.


def automatic_email():
    user = input("Enter Your Name >>: ")
    email = input("Enter Your Email >>: ")
    message = (f"Dear {user}, This is a test mail")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("Your Gmail Account", "Your App Password") #personalize you details here (add your email and pass)
    s.sendmail('&&&&&&&&&&&', email, message)
    print("Email Sent!")
    
automatic_email()
