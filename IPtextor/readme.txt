##################################
# How to use this script program #
##################################

This script finds your public IP and lets you know when it changes via text message. Set this up and leave it running on a device on your home network to always know your public IP! :)

I ran this from a raspberry pi 4 (2gb RAM version) and it ran great inside of a docker container.

Setup:
You will need to install docker use one of the following:
Install docker with:
sudo apt install docker
OR
sudo snap install docker (Ubuntu Server)
OR
install docker from another soruce


Use your favioute text editor to add the auth keys and phone numbers to the python script. This is done at the top of the file. For futher information, check out this Twilio doc:
https://www.twilio.com/docs/sms/quickstart/python?code-sample=code-use-the-twilio-cli-to-send-an-sms&code-language=twilio-cli&code-sdk-version=1.x

After updating the python script, point the docker file "workdir" to the directory that contains the script and requirements.txt


After you have updated the python script and dockerfile, create the docker image by running:
sudo docker build -t iptextor .

View the image with:
sudo docker images

Run the container with:
sudo docker run -d -e TZ=Australia/Sydney iptextor .

View the container name with
sudo docker ps

create a bash shell in the container using the following:
docker exec -it <container name> /bin/bash

Use this to check the logs / make sure everything is happy
