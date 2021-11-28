import os, sys, time

from fritzconnection import FritzConnection
from fritzconnection.core.exceptions import FritzConnectionException
from fritzconnection.lib.fritzhosts import FritzHosts

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
file_liste = os.listdir('home/jarvis/Scripts')
if 'hosts.txt' in file_liste:
#    print(os.path.abspath(path + '\hosts.txt'))
#    datei = os.path.abspath(path + '\hosts.txt')
    datei = '/home/jarivs/Scripts/hosts.txt'
    with open(datei, 'r') as f:
        content = f.read().strip()
        if content == 'False':
            status_suspect_was = False
        if content == 'True':
            status_suspect_was = True

else:
#    datei = os.path.abspath(path + '\hosts.txt')
    datei = '/home/jarvis/Scripts/host.txt'
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
    if status_suspect_now == False:
        presence = 'Off Site'
    message = (time_stamp + ' [Alert] - presence changed! ' + presence)
    hostlog(message)



    


