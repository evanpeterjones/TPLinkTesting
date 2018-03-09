import os
import time
import json
import socket

jason = open("TPLight.json")
#packet = json.load(jason)
ip = "192.168.0.102"
portOut = 1040
portIn = 61000
data = jason.read(1024)
#    data = {"system" : {"get_sysinfo" : null},"emeter" : {"get_realtime" : null}}}
#    print(json.dumps(data))
def scan():
    #json.dumps(packet)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(data, ("", portOut))
    sock.close()
    newSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    newSock.bind(("", portIn))
    running = True
    while running:
        recieved, adr = newSock.recvfrom(1024)
        print(recieved)
        running = false
    newSock.close()


def On():
    print "light on"

def Off():
    print "light off"
