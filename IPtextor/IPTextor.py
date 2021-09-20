import requests
import logging
import os
import datetime
import time
import logging.handlers as handlers 
from twilio.rest import Client

# CHANGE THESE
# TWILIO ACCOUNT SID SEE THE READ ME FOR DETAILS
account_sid = ''
# TWILIO AUTHENTICATION TOKEN. SEE THE READ ME FOR DETAILS
auth_token = ''
# TWILIO messaging service SID.
messaging_service_sid=''
# CHANGE THIS TO THE PHONE NUMBER YOU WANT TO RECEIVE THE TEXT MESSAGES
# MAKE SURE IT IS IN E.164 FORMAT
# https://www.twilio.com/docs/glossary/what-e164
Phonenumber = '+'

def sendmessage(ip):
    # Connecting to Twilio
    client =  Client(account_sid, auth_token)
    # Sending the message
    client.messages.create(
    messaging_service_sid=messaging_service_sid,
    to=Phonenumber,
    body="My home IP is: " + ip)

# Start of exception and HTTP logging
loggers = {}
formatter = logging.Formatter('%(asctime)s : %(message)s', datefmt='%d/%m/%y %H:%M:%S %p' )

logger = logging.getLogger("log")
logger.setLevel(logging.INFO)
handler = handlers.RotatingFileHandler("ERROR.log", maxBytes=5*1024*1024, backupCount=3)
handler.setFormatter(formatter)
logger.addHandler(handler)

#Create the IP log file
def makeipfile(IP):
    f = open("IP.txt", "w+")
    f.write(IP)
    f.close()

#Format for the IP address log file
def writetoIPlog(IP):
    with open("IP.log", "a+") as fp:
        fp.write(str(datetime.datetime.now()) + " : " + IP + '\n')

def __main__():
    # Attempt to obtain your Public IP
    try:
        URL = 'https://api.ipify.org'  
        ip = requests.get(URL).text
    except Exception as e:
        logger.error("Exception occurred", exc_info=True)
        exit()
    writetoIPlog(ip)
    # Check for the IP file
    IPthere = os.path.exists("IP.txt")
    if IPthere:
        ipcheck = open("IP.txt", "r")
        Knownip = ipcheck.read()
        # If this is a new IP address, log it and send a message
        if Knownip != ip:
            makeipfile(ip)
            try:
                sendmessage(ip)
            except Exception as e:
                logger.error("Exception occurred", exc_info=True)
    # If the IP file doesn't exist, make a new one and send a message.
    else:
        makeipfile(ip)
        try:
            sendmessage(ip)
        except Exception as e:
            logger.error("Exception occurred", exc_info=True)
while True:
    __main__()
    time.sleep(600)
