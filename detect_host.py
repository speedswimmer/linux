import time, sys, os
from Mail import send_mail
from fritzconnection import FritzConnection
from fritzconnection.core.exceptions import ActionError, FritzConnectionException, FritzServiceError
from fritzconnection.lib.fritzhosts import FritzHosts
from fritzconnection.lib.fritzstatus import FritzStatus

print("Program started, please wait...")

try:
    fc = FritzConnection(address='192.168.178.1', password='Sprosse2102', use_tls=True)
except FritzConnectionException:
    print("Can't connect to FritzBox!")
    sys.exit(0)

today = (time.strftime("%d-%m-%y"))
time_stamp = (time.strftime("%H:%M:%S"))
daily_logfile = ('hostlog.txt')

global status_suspect_was
status_suspect_was = False

def getHostStatus():   
    fh = FritzHosts(fc)
    activehosts = fh.get_active_hosts()

    global status_suspect_now
    status_suspect_now = False

    host_entry = []

    for i in range(0, len(activehosts)-1):
        hostname = activehosts[i]["name"]
        ipaddress = activehosts[i]["ip"]
        hoststatus = activehosts[i]["status"]
        hostmac = activehosts[i]["mac"]
        host_entry.append(hostname)
        
        if 'iPh-HartmannM' in host_entry:
            status_suspect_now = True
        else:
            status_suspect_now = False
        
    return status_suspect_now

while True:
    
    if os.path.exists(daily_logfile) == True:
        f = open(daily_logfile, "a")
#        f.write("\n-----------------------------------\n")
#        f.write(time.strftime("\n%d.%m.%y - %H:%M:%S\n"))
    else:
        f = open(daily_logfile, "w")
        f.write("-------------------------------------------")
        f.write(time.strftime("\n%d.%m.%y - %H:%M:%S\n"))
    
    getHostStatus()
    
    print("Matthias prescence now:", status_suspect_now)
    
    if status_suspect_now != status_suspect_was:
        print("Status changed! - Presence={}, {}!\n".format(status_suspect_now, time_stamp))
        f.write("Status changed! - Presence={}, {}!\n".format(status_suspect_now, time_stamp))
    status_suspect_was = status_suspect_now
    time.sleep(15)
#send_mail()