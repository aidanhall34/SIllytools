#!/bin/python3
#This is meant to be run as a cron job.
#It will find you public IP address and send it to you in a text message
#If you enable port forwarding on some devices you can phone home without paying
#For a static IP :)
#You will need to set up a way to send a text, I will be using twilo
import time
import requests
import os
from twilio.rest import Client
from contextlib import redirect_stdout
import datetime 
import logging
from logging.handlers import RotatingFileHandler
def __main__():
#Defining the text message Function, change the number and auth stuff as needed
    ip = requests.get('https://api.ipify.org').text
    
    def sendmessage():
        #Change this
            sid = ''
            auth_token = ''
            client = Client(sid, auth_token)
        
            message = client.messages.create(
            from_="",
            to="",    
            body="My home IP is: " + ip
            )            
            return print(message.sid)
    #no changes from here
    log_format =logging.Formatter('%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
    logfile = 'log.log'
    my_handler = RotatingFileHandler(logfile, mode='a', maxBytes=5*1024*1024,
        backupCount=2, encoding=None, delay=0)
    my_handler.setFormatter(log_format)
    my_handler.setLevel(logging.INFO)
    app_log = logging.getLogger('root')
    app_log.setLevel(logging.INFO)

    app_log.addHandler(my_handler)

    def makeipfile():
        f = open("IP.txt", "w+")
        f.write(ip)
        f.close()

# Check if this has been done before
    IPthere = os.path.exists("IP.txt")


    def makeipfile():
        f = open("IP.txt", "w+")
        f.write(ip)
        f.close()
    app_log.info(ip)

    if IPthere:
        print("file is there")
        ipcheck = open("IP.txt", "r")
        Knownip = ipcheck.read()

        if Knownip == ip:
            print("We know about this one, no need to message")
        else:
            print("We got a new one!!")
            print("Sending message")
            makeipfile()
            sendmessage()

    else:
        print("You haven't done this before")
        print("Sending SMS")
        makeipfile()
        sendmessage()
while True:
    __main__()
    time.sleep(600)
    

