import os, sys, time
#import logging
from fritzconnection import FritzConnection
from fritzconnection.core.exceptions import FritzConnectionException
from fritzconnection.lib.fritzhosts import FritzHosts

def hostlog(content):
    with open('hostlog.txt','a') as y:
        y.write(content +'\n')

def getactiveHosts():
    try:
        fc = FritzConnection(address="192.168.178.1", password="Sprosse2102", use_tls=True)
    except FritzConnectionException:
#        logging.error("Can't connect to FritzBox!")
        sys.exit()
    
    fh = FritzHosts(fc)
    activehosts = fh.get_active_hosts()
    global status_suspect_now

    host_entry = []

    for i in range(0, len(activehosts)-1):
        hostname = activehosts[i]["name"]
        host_entry.append(hostname)
    
    if 'iPh-HartmannM' in host_entry:
        status_suspect_now = True
    else:
        status_suspect_now = False

    return status_suspect_now   

#logging.basicConfig(filename='hostdetect.log', filemode='a', level=logging.DEBUG, style="{" ,format = "{asctime} [{levelname:8}] {message}", datefmt="%d.%m.%Y, %H:%M:%S")
#logging.info('Program started...')

status_suspect_now = getactiveHosts()

global status_suspect_was
status_suspect_was = False 

print('----- File configuration ------')
path = os.getcwd()
file_liste = os.listdir(path)
if 'hosts.txt' in file_liste:
    print(os.path.abspath(path + '\hosts.txt'))
    datei = os.path.abspath(path + '\hosts.txt')
    with open(datei, 'r') as f:
        content = f.read().strip()
        if content == 'False':
            status_suspect_was = False
        if content == 'True':
            status_suspect_was = True

else:
#    logging.info('File hosts.txt created!')
    with open(datei, 'w') as f:
        f.write('False')

# update storage file
if status_suspect_now == True:
    with open(datei, 'w') as g:
        g.write('True')
        print('Schreibe neuen Wert True in die Datei...')
if status_suspect_now == False:
    with open(datei, 'w') as h:
        h.write('False')
        print('Schreibe neuen Wert False in die Datei!')

if status_suspect_now == status_suspect_was:
    print("No change!")
else:
    time_stamp = time.strftime('%d.%m.%Y - %H:%M:%S')
    print("Alert - presence changed! Now supect is in building:", status_suspect_now)
    if status_suspect_now == True:
        presence = 'On Site'
    if status_suspect_now == False:
        presence = 'Off Site'
    message = (time_stamp + ' [Alert] - presence changed! ' + presence)
    hostlog(message)
#  logging.info('Alert - presence changed!')



    


