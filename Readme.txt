To install PIP (please update repositories before: $sudo apt-get update):

PIP for python2: $sudo apt-get install python-pip
PIP for python3: $sudo apt-get install python3-pip

*********** Installation of fritzconnection python module on Raspberrypi ***********

fritzconnection python api needs to be installed on Raspberrypi beforehand.
As fritzconnection only supports Python 3.6.0 or higher, the module need to be installed via pip3 e.g.
$ pip3 install fritzconnection

*********** Download of Python Scripts from Github *********************************

Download python scripts from Github:
cd into the correct destination folder e.g. cd /home/pi/Scripts/
wget [url from RAW-File]: wget https://raw.githubusercontent.com/speedswimmer/linux/main/Readme.txt
wget https://raw.githubusercontent.com/speedswimmer/linux/main/Mail.py
wget https://raw.githubusercontent.com/speedswimmer/linux/main/fritzb.py
wget https://raw.githubusercontent.com/speedswimmer/linux/main/file.py
wget https://raw.githubusercontent.com/speedswimmer/linux/main/new_detect.py

*********** To get Mail.py working *************************************************

Set environment variables in Linux to store email-address and email-passwort for example:
$ export VAR1="myemail@t-online.de"
$ export VAR2="Password for Email-Account"
Get environment variable values in python:
$ import os
$ os.environ.get('VAR1')

************* Schedule regular execution of python scripts via crontab *************
crontab -e
0 */1 * * * python3 /home/pi/Scripts/fritzb.py
1 11,17,23 * * * python3 /home/pi/Scripts/Mail.py

sudo service cron reload / sudo service cron restart
