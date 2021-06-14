#python 3
import threading
import time
from queue import Queue
import socket

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
    print(
    '''
            What is a port scanner?
    A port scanner is a tool used to scan and
    identify open ports the software on machines
              TYPE "help" FOR HELP
    '''
    )
    while True:
        line = input('port scanner> ')
        if line == 'help':
            print(
            '''
            COMMANDS:
            help: lists available commands
            quit: closes program
            portscan: starts the process of a port scan
            '''
            )
        if line == 'quit':
            break

        if line == 'portscan':
            print_lock = threading.Lock()

            target = input('Enter Target Host: ')

            startingPort = input('Starting Port Range: ')

            endingPort = input('Ending Port Range: ')

            threadCount = input('How Many Threads To Scan With: ')

            def portscan(port):
                start = time.time()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    con = s.connect((target,port))
                    with print_lock:
                        if port == (80):
                            print('Port 80 | HTTP')
                        elif port == (443):
                            print('Port 443 | HTTPS')
                        elif port == (21):
                            print('Port 21 | FTP')
                        elif port == (22):
                            print('Port 22 | FTPS / SSH')
                        elif port == (110):
                            print('Port 110 | POP3')
                        elif port == (995):
                            print('Port 995 | POP3 SSL')
                        elif port == (143):
                            print('Port 143 | IMAP')
                        elif port == (993):
                            print('Port 993 | IMAP SSL')
                        elif port == (25):
                            print('Port 25 | SMTP')
                        elif port == (26):
                            print('Port 26 | SMTP')
                        elif port == (587):
                            print('Port 587 | SMTP SSL')
                        elif port == (3306):
                            print('Port 3306 | MySQL')
                        elif port == (2082):
                            print('Port 2082 | cPanel')
                        elif port == (2083):
                            print('Port 2083 | cPanel')
                        elif port == (2086):
                            print('Port 2086 | WHM')
                        elif port == (2087):
                            print('Port 2087 | WHM SSL')
                        elif port == (2095):
                            print('Port 2095 | Webmail')
                        elif port == (2096):
                            print('Port 2096 | Webmail SSL')
                        elif port == (2077):
                            print('Port 2077 | WebDav / WebDisk')
                        elif port == (2078):
                            print('Port 2078 | WebDAV / WebDisk SSL')
                        else:
                            print('port', port)
                    con.close()
                except:
                    pass

            def threader():
                while True:
                    worker = q.get()
                    portscan(worker)
                    q.task_done()

            q = Queue()

            for x in range(int(threadCount)):
                 t = threading.Thread(target=threader)
                 t.daemon = True
                 t.start()
            start = time.time()

            for worker in range(int(startingPort), int(endingPort) +1):
                q.put(worker)

            q.join()
            end = time.time()
            print('That Scan Took', end-start, 'Seconds')


askLogin()
