## How to use IPtextor

This docker container finds your public IP and lets you know when it changes via text message. Set this up and leave it running on a device on your home network to always know your public IP.

### Setup:
You will need to install Docker:
<a href='https://docs.docker.com/get-docker/'>Install Docker</a>

You will also need a Twilio account. You can set up a trial here:
<a href='https://www.twilio.com/try-twilio'>Create a Twilio account</a> 

<p>
Use your text editor of choice to add your authentication keys and phone numbers to IPtextor.py, this is done at the top of the file. For further information, check out this Twilio doc:</p>
<a href='https://www.twilio.com/docs/sms/quickstart/python?code-sample=code-use-the-twilio-cli-to-send-an-sms&code-language=twilio-cli&code-sdk-version=1.x'>Twilio documentation</a>

##### Phone number:
You phone number must be in E.164 format. You can find more information here:
<a href='https://www.twilio.com/docs/glossary/what-e164'>What is E.164</a>


### Docker commands 
Create the docker image by running:
```bash
sudo docker build -t iptextor .
```
Run the container with:
```bash
sudo docker run -t --name="IPTextor" -d -e TZ=Australia/Sydney iptextor
```
The logs can be found in the root directory of the container.
Create a bash shell in the container using the following:
```bash
sudo docker exec -it IPTextor /bin/bash
```

Run this to make sure the container comes starts again after your device restarts:
```bash
sudo docker update --restart unless-stopped IPTextor
```
