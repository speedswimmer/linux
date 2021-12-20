import os, sys, time
from fritzconnection import FritzConnection
from fritzconnection.core.exceptions import FritzConnectionException
from fritzconnection.lib.fritzhosts import FritzHosts
from messaging import send_email

def hostlog(content):
    with open('/home/jarvis/Scripts/hostlog.txt','a') as y:
        y.write(content +'\n')

def getactiveHosts():
    try:
        fc = FritzConnection(address="192.168.178.1", password="", use_tls=True)
    except FritzConnectionException:
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

status_suspect_now = getactiveHosts()

global status_suspect_was
status_suspect_was = False 

#print('----- File configuration ------')
path = os.getcwd()
file_liste = os.listdir('/home/pi/Scripts')
if 'hosts.txt' in file_liste:
    datei = '/home/pi/Scripts/hosts.txt'
    with open(datei, 'r') as f:
        content = f.read().strip()
        if content == 'False':
            status_suspect_was = False
        if content == 'True':
            status_suspect_was = True

else:
    datei = '/home/pi/Scripts/hosts.txt'
    with open(datei, 'w') as f:
        f.write('False')

# update storage file
if status_suspect_now == True:
    with open(datei, 'w') as g:
        g.write('True')
if status_suspect_now == False:
    with open(datei, 'w') as h:
        h.write('False')

if status_suspect_now == status_suspect_was:
#    print("No change!")
    pass
else:
    time_stamp = time.strftime('%d.%m.%Y - %H:%M:%S')
#    print("Alert - presence changed! Now supect is in building:", status_suspect_now)
    if status_suspect_now == True:
        presence = 'On Site'
        send_email('Person has entered the building! {}'.format(time_stamp))
    if status_suspect_now == False:
        presence = 'Off Site'
        send_email('Person has left the building! {}'.format(time_stamp))
    message = (time_stamp + ' [Alert] - presence changed! ' + presence)
    hostlog(message)



    


