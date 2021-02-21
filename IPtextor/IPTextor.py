import requests
import logging
import os
import datetime
import time
import logging.handlers as handlers 
from twilio.rest import Client

def sendmessage(ip):
    #Change this
    sid = ''
    auth_token = ''
    client =  Client(sid, auth_token)
    message = client.messages.create(
    #Change this
    from_='',
    to='',
    body="My home IP is: " + ip)

# Start of exception and HTTP logging
loggers = {}
formatter = logging.Formatter('%(asctime)s : %(message)s', datefmt='%d/%m/%y %H:%M:%S %p' )
# logger = logging.basicConfig(filename='HTTPandERROR.log', level=logging.DEBUG,
#             format='%(asctime)s : %(message)s', datefmt='%d/%m/%y %H:%M:%S %p' )

logger = logging.getLogger("log")
logger.setLevel(logging.INFO)
handler = handlers.RotatingFileHandler("ERROR.log", maxBytes=5*1024*1024, backupCount=3)
handler.setFormatter(formatter)
logger.addHandler(handler)

#Create the referanced IP file
def makeipfile(IP):
    f = open("IP.txt", "w+")
    f.write(IP)
    f.close()

#Create the IP address log file
def writetoIPlog(IP):
    with open("IP.log", "a+") as fp:
        fp.write(str(datetime.datetime.now()) + " : " + IP + '\n')

def __main__():

    # Attempt to obtain your Public IP
    try:
        URL = 'https://api.ipify.org'  
        ip = requests.get(URL).text
    except Exception as e:
        logger.error("Exception occured", exc_info=True)
        print("The IP API server could not be reached.\nPlease ensure you and it are online")
        print("The URL is: " + URL )
        exit()


    writetoIPlog(ip)


    IPthere = os.path.exists("IP.txt")
    if IPthere:
        print("file is there")
        ipcheck = open("IP.txt", "r")
        Knownip = ipcheck.read()
        if Knownip == ip:
            print("We know about this one, no need to message")
        else:
            print("We got a new one!!")
            print("Sending message")
            makeipfile(ip)
            try:
                sendmessage(ip)
            except Exception as e:
                logger.error("Exception occured", exc_info=True)
                print("Unable to send the message.\nCheck the ERROR.log for more detail")
    else:
        print("You haven't done this before")
        print("Sending SMS")
        makeipfile(ip)
        try:
            sendmessage(ip)
        except Exception as e:
            logger.error("Exception occured", exc_info=True)
            print("Unable to send the message.\nCheck the HTTPandERROR.log for more detail")
while True:
    __main__()
    time.sleep(600)
