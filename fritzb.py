# Install fritzconnection with pip3 install fritzconnection on Rpi
import time, sys, os
from Mail import send_mail
from fritzconnection import FritzConnection
from fritzconnection.core.exceptions import ActionError, FritzConnectionException, FritzServiceError
from fritzconnection.lib.fritzhosts import FritzHosts
from fritzconnection.lib.fritzstatus import FritzStatus

try:
    fc = FritzConnection(address='192.168.178.1', password='****', use_tls=True)
except FritzConnectionException:
    print("Can't connect to FritzBox!")
    sys.exit(0)

today = (time.strftime("%d-%m-%y"))
daily_logfile = ("/home/pi/Scripts/" + today + "-log.txt")

if os.path.exists(daily_logfile) == True:
    f=open(daily_logfile, "a")
    f.write(time.strftime("\n%d.%m.%y - %H:%M:%S\n"))
else:
    f=open(daily_logfile, "w")
    f.write(time.strftime("%d.%m.%y - %H:%M:%S\n"))

def getFritzStatus():
    fs = FritzStatus(fc)
    print("*************** Status FritzBox! ********************\n")
    f.write("*************** Status FritzBox! ********************\n")
    print("*************** Status FritzBox! *****************\n")
    f.write("*************** Status FritzBox! ****************\n")
    print("FritzBox Model: %s" % (fs.modelname))
    f.write("FritzBox Model: %s\n" % (fs.modelname))
    print("FritzBox is linked: %s" %(fs.is_linked))
    f.write("FritzBox is linked: %s\n" %(fs.is_linked))
    print("FritzBox is connected: %s" %(fs.is_connected))
    f.write("FritzBox is connected: %s\n" %(fs.is_connected))
    print("FritzBox uptime: %s" %(fs.str_uptime))
    f.write("FritzBox uptime: %s\n" %(fs.str_uptime))
    print("FritzBox external IP4: %s" %(fs.external_ip))
    f.write("FritzBox external IP4: %s\n" %(fs.external_ip))

def getWLANstatus():
    action = 'GetInfo'
    status = []
    print("******************* WLAN Status FritzBOX! **************")
    for i in range (1,10):
        try:
            wlan_status = fc.call_action(f'WLANConfiguration{i}', action)
        except FritzServiceError:
            break
        #status.append(wlan_status["NewSSID"])
        print(wlan_status["NewSSID"] + ": " + wlan_status["NewStatus"])
        #status.append(wlan_status["NewStatus"])
        #print(wlan_status["NewStatus"])
    print("\n")

def getHostStatus():
    fh = FritzHosts(fc)
    hosts = fh.get_hosts_info()
    activehosts = fh.get_active_hosts()
    print("*****************************************\n")
    f.write("******************************************\n")
    print("Übersicht der bekannten Hosts:")
    print("Es sind %s Hosts bekannt!\n" %(len(hosts)))
    f.write("Es sind %s Hosts bekannt!\n" %(len(hosts)))
    print("Folgende %s Hosts sind aktive im Netzwerk:" %(len(activehosts)))
    f.write("Folgende %s Hosts sind aktive im Netzwerk:" %(len(activehosts))+"\n")
    print("IP-Address         Name                      Status")
    f.write("IP-Address         Name                      Status\n")
    print("---------------------------------------------------")
    f.write("---------------------------------------------------\n")

    for i in range(0, len(hosts)-1):
        if hosts[i]["status"] == True:
            ipaddress = hosts[i]["ip"]
            hostname = hosts[i]["name"]
            hoststatus = hosts[i]["status"]
            print(f"{ipaddress:18} {hostname:25} - {hoststatus}")
            f.write(f"{ipaddress:18} {hostname:25} - {hoststatus}\n")

#getWLANstatus()
getFritzStatus()
getHostStatus()
f.close()
#send_mail()
