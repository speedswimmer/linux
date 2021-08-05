import time, sys, os
from Mail import send_mail
from fritzconnection import FritzConnection
from fritzconnection.core.exceptions import ActionError, FritzConnectionException, FritzServiceError
from fritzconnection.lib.fritzhosts import FritzHosts
from fritzconnection.lib.fritzstatus import FritzStatus

try:
    fc = FritzConnection(address='192.168.178.1', password='MultiSyncV554Q', use_tls=True)
except FritzConnectionException:
    print("Can't connect to FritzBox!")
    sys.exit(0)
    
if os.path.exists("Fritzbox/log.txt") == True:
    f=open("Fritzbox/log.txt", "a")
    f.write(time.strftime("\n%d.%m.%y - %H:%M:%S\n"))
else:
    f=open("Fritzbox/log.txt", "x")
    f.write(time.strftime("%d.%m.%y - %H:%M:%S\n"))

def getFritzStatus():
    fs = FritzStatus(fc)
    # monitor = fs.get_monitor_data()
    # print(monitor)
    print("*************** Status FritzBox! ********************\n")
    f.write("*************** Status FritzBox! ********************\n")
    print("FritzBox Model: %s" % (fs.modelname))
    f.write("FritzBox Model: %s" % (fs.modelname))
    print("FritzBox is linked: ",fs.is_linked)
    f.write("FritzBox is linked: ",fs.is_linked)
    print("FritzBox is connected:", fs.is_connected)
    f.write("FritzBox is connected:", fs.is_connected)
    print("FritzBox uptime:", fs.str_uptime)
    f.write("FritzBox uptime:", fs.str_uptime)
    print("FritzBox external IP4: %s\n" %(fs.external_ip))
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
    print("**********************************\n")
    f.write("**********************************\n")
    print("Übersicht der bekannten Hosts:")
    print("Es sind %s Hosts bekannt!\n" %(len(hosts)))
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
getHostStatus()
f.close()
send_mail()