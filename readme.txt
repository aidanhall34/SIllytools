##################################
# How to use this script program #
##################################

I ran this from a raspberry pi 4 and it ran great inside of a docker container.
I was unable to get it working as well as I would like as cronjob

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

After updating the python script, point the docker file "workdir" entry to the directory that contains the script and requirements.txt


After you have updated the python script and docker make file, create the docker image by running:
sudo docker build -t IPtextor .

View the image with:
sudo docker images

Run the container with:
sudo docker run -it IPtextor 

create a bash shell in the container using the following:
docker exec -it <container name> /bin/bash
