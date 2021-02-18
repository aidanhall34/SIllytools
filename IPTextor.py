#!/bin/python3
#This script requires a twilio account, you can set this up here
#https://www.twilio.com/try-twilio
#See the Twilio doc for obtaining auth tokens
#See the read me for general information about twilio
import time
import requests
import os
from twilio.rest import Client
from contextlib import redirect_stdout
import datetime 

def __main__():
#Defining the text message Function, change the number and auth stuff as needed
    ip = requests.get('https://api.ipify.org').text

    def sendmessage():
            #Change these
            sid = '' 
            auth_token = ''
            client = Client(sid, auth_token)
        
            message = client.messages.create(
            #Change these
            from_="",
            to="",    
            body="My home IP is: " + ip
            )            
            return print(message.sid)
#This bit of the scipt can be left untouched
    def makeipfile():
        f = open("IP.txt", "w+")
        f.write(ip)
        f.close()

# Check if this has been done before
    IPthere = os.path.exists("IP.txt")
    logthere = os.path.exists("log.txt")


    def makeipfile():
        f = open("IP.txt", "w+")
        f.write(ip)
        f.close()


    if logthere:
        f = open("log.txt", "a+")
        f.write(str(datetime.datetime.now()) + ": " + ip + "\n" )
        f.close()
    else:
        f = open("log.txt", "w+")
        f.write(str(datetime.datetime.now()) + ": " + ip + "\n")
        f.close()

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
    

