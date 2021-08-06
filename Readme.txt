*********** Installation of fritzconnection python module on Raspberrypi ***********

fritzconnection python api needs to be installed on Raspberrypi beforehand.
As fritzconnection only supports Python 3.6.0 or higher, the module need to be installed via pip3 e.g.
$ pip3 install fritzconnection

*********** Download of Python Scripts from Github *********************************

Download files like python scripts from Github:
cd into the correct folder e.g. cd /home/pi/Scripts/
wget [url from RAW-File]: wget https://raw.githubusercontent.com/speedswimmer/linux/main/Readme.txt

*********** To get Mail.py working *************************************************

Set environment variables in linux for email-address and email passwort for example:
$ export VAR1="myemail@t-online.de"
$ export VAR2="Password for EMail"
Get environment variable values in python:
$ import os
$ os.environ.get('VAR1')
