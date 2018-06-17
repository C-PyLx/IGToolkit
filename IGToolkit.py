#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------------------------
#Information gathering toolkit
#IGToolkit
#Version: 1.0.1
#Coded by: Learning :~#
#Follow me on github:
#https://github.com/C-PyLx
#Report bugs to:
#https://t.me/Ac3ess

import os
import sys
import time
import socket
import requests
from urllib.error import URLError
from urllib.request import urlopen

#Terminal colors code:
green = '\033[0;32m'
blue = '\033[0;34m'
red = '\033[0;31m'
cyan = '\033[0;96m'
yellow = '\033[0;33m'
pink = '\033[38;5;197m'
italic = '\033[0;3m'
end = '\033[0;37m'

def IGToolkit():
    '''IGToolkit > Information Gathering Toolkit\n
    There are many scripts for information gathering ;)'''
    try:

        menu = """1)   Port scanner powerful [with types]
2)   Website dos scanner
3)   Whois website informations
4)   Find robots.txt on target
5)   SQL vulnerability scanner
6)   MySQL vulnerability scanner
7)   What is my username?
8)   What is my platform?
9)   What is my ip address?
0)   Show my status

00)  Exit from ( IGToolkit )!
    """
        logo()
        print (italic + menu, end)

        choice = input (cyan + '''┌─[IGToolkit] > [menu]
└──────►  ''' + end)

        try:
            if choice  ==  '1':
                port_scanner()
            elif choice == '2':
                dos_scan()
            elif choice == '3':
                who_is()
            elif choice == '4':
                find_robots()
            elif choice == '5':
                sql_scan()
            elif choice == '6':
                mysql_scan()
            elif choice == '7':
                local_username()
            elif choice == '8':
                operating_sys()
            elif choice == '9':
                local_ip()
            elif choice == '0':
                net_status()
            elif choice in ('\r', '\n', '\t', ' '):
                IGToolkit()
            elif choice == 'exit':
                exit_app()
            elif choice == '00':
                exit_app()
            else:
                IGToolkit()

        except KeyboardInterrupt:
            IGToolkit()
    except KeyboardInterrupt:
        exit_app()

def port_scanner():
    'Fast & Poweful port scanner'
    try:
        os.system('clear')
        server = input ('[-] Enter server IP or address: ')
        min_port = int(input ('[-] Enter minimum port number: '))
        max_port = int(input ('[-] Enter maximum port number(max=65539): '))
        start_time = time.time()

        if min_port > max_port:
            print (red + '\n[!] Minimum port must be smaller than maximum port !', end)
            time.sleep(5)
            IGToolkit()

        print (blue + '\n[+] Program started at: %s' %time.strftime('%H:%M:%S'))
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_ip = socket.gethostbyname(server)
        print (yellow + '[*] Host IP address: %s\n' %server_ip)
        print (pink + '[+] Scanning ports range {%s ~> %s}\n' %(min_port, max_port), end)

        for port in range(min_port, max_port+1):
            result = connection.connect_ex((server_ip, port))

            if result == 0 and port == 20:
                print (green + '[✔] port:20 /open [FTP/D]', end)
            elif result == 0 and port == 21:
                print (green + '[✔] port:21 /open [FTP/C]', end)
            elif result == 0 and port == 22:
                print (green + '[✔] port:22 /open [SSH]', end)
            elif result == 0 and port == 23:
                print (green + '[✔] port:23 /open [Telnet]', end)
            elif result == 0 and port == 25:
                print (green + '[✔] port:25 /open [SMTP]', end)
            elif result == 0 and port == 53:
                print (green + '[✔] port:53 /open [DNS]', end)
            elif result == 0 and port == 80:
                print (green + '[✔] port:80 /open [HTTP]', end)
            elif result == 0 and port == 110:
                print (green + '[✔] port:110 /open [PoP3]', end)
            elif result == 0 and port == 119:
                print (green + '[✔] port:119 /open [NNTP]', end)
            elif result == 0 and port == 123:
                print (green + '[✔] port:123 /open [NTP]', end)
            elif result == 0 and port == 143:
                print (green + '[✔] port:143 /open [IMAP]', end)
            elif result == 0 and port == 161:
                print (green + '[✔] port:161 /open [SNMP]', end)
            elif result == 0 and port == 194:
                print (green + '[✔] port:194 /open [IRC]', end)
            elif result == 0 and port == 443:
                print (green + '[✔] port:443 /open [HTTPS/TLS/SSL]', end)
            else:
                if result == 0:
                    print (green + '\n[✔] port:%s /open [Unknown type]!' %port, end)
                else:
                    pass

        end_time = time.time()
        lapse = round(end_time-start_time, 2)

        print (cyan + '\n[+] Scanned %s port numbers in %s seconds.' %(max_port-min_port, lapse), end)

    except socket.error:
        print (red + '\n[x] Check your internet connection !', end)
        time.sleep(4)
        IGToolkit()
    except socket.gaierror:
        print (red + '\n[x] Host or service not known !', end)
        time.sleep(4)
        IGToolkit()
    except ValueError:
        print (red + '\n[x] Error in value entry !', end)
        time.sleep(4)
        IGToolkit()
    input ('\n[-] Press <Enter> for back:')
    IGToolkit()

def dos_scan():
    'Dos attacks vulnerability scanner'
    try:
        os.system('clear')
        target = input ('[-] Enter target address: ')
        start_time = time.time()
        print (blue + '\n[+] Program started at: %s\n' %time.strftime('%H:%M:%S'), end)

        connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        port = 80

        if connection.connect((target, port)):
            end_time = time.time()
            lapse = round(end_time-start_time, 2)
            print (green + '[✔] Target: %s is vulnerable to dos attacks.' %target, end)
            print (cyan + '\n[*] Time elapsed: %s' %lapse, end)

        else:
            print (red + '\n[!] Target is not vulnerable !', end)

    except socket.error:
        print (red + '\n[x] Check your connection !', end)
        time.sleep(4)
        IGToolkit()
    except socket.gaierror:
        print (red + '\n[x] Host or service: %s not known !' %target, end)
        time.sleep(4)
        IGToolkit()
    input ('\n[-] Press <Enter> for back:')
    IGToolkit()

def who_is():
    'Whois from website domain'
    os.system('clear')
    target = input ('[-] Enter target address: ')
    start_time = time.time()
    print (blue + '\n[+] Program started at: %s\n' %time.strftime('%H:%M:%S'), end)

    os.system('whois %s' %target)
    end_time = time.time()
    lapse = round(end_time-start_time, 2)

    print (cyan + '\n[*] Time elapsed: %s' %lapse, end)
    input ('\n[-] Press <Enter> for back:')
    IGToolkit()

def find_robots():
    'Find robots.txt in websites'
    try:
        os.system('clear')
        target = input ('[-] Enter target address: ')
        start_time = time.time()
        print (blue + '\n[+] Program started at: %s\n' %time.strftime('%H:%M:%S'), end)

        robot_addr = 'robots.txt'
        robot_url = 'http://' + target + '/' + robot_addr

        data = urlopen(robot_url)
        if data:
            end_time = time.time()
            lapse = round(end_time-start_time, 2)
            print (green + '[✔] Target: %s have robots.txt.' %target, end)
            print (cyan + '\n[*] Time elapsed: %s' %lapse, end)

        else:
            print (red + '[x] Can not find robots.txt on target: %s' %target, end)
            time.sleep(4)
            IGToolkit()

    except requests.HTTPError:
        print (red + '\n[x] Can not connect to target !', end)
        time.sleep(4)
        IGToolkit()
    except URLError as Error:
        print (red + '\n[x] Error: %s' %Error, end)
        time.sleep(4)
        IGToolkit()
    input ('\n[-] Press <Enter> for back:')
    IGToolkit()

def sql_scan():
    'SQL vulnerability scanner'
    try:
        os.system('clear')
        target = input ('[-] Enter target address(ex: http://example.com): ')
        start_time = time.time()
        print (blue + '\n[+] Program started at %s\n' %time.strftime('%H:%M:%S'), end)

        data = requests.get(target, "'").text
        text = 'You have an error in SQL syntax'

        if text in data:
            end_time = time.time()
            lapse = round(end_time-start_time, 2)
            print (green + '[✔] Detect SQL vulnerability. Target: %s' %target, end)
            print (cyan + '\n[*] Time elapsed: %s' %lapse, end)

        else:
            print (red + '[x] Target: %s not vulnerable !' %target, end)

    except requests.HTTPError:
        print (red + '\n[x] Can not connect to target !', end)
        time.sleep(4)
        IGToolkit()
    input ('\n[-] Press <Enter> for back:')
    IGToolkit()

def mysql_scan():
    'MySQL vulnerability scanner'
    try:
        os.system('clear')
        target = input ('[-] Enter target address: ')
        start_time = time.time()
        print (blue + '\n[+] Program started at: %s\n' %time.strftime('%H:%M:%S'), end)

        text = 'MySQL'
        data = requests.get(target, "'").text

        if text in data:
            end_time = time.time()
            lapse = round(end_time-start_time, 2)
            print (green + '[✔] Found MySQL vulnerability. Target: %s' %target, end)
            print (cyan + '\n[*] Time elapsed: %s' %lapse, end)

        else:
            print (red + '[x] Target: %s not vulnerable !' %target, end)

    except requests.HTTPError:
        print (red + '\n[x] Can not connect to target ', end)
        time.sleep(4)
        IGToolkit()
    input ('\n[-] Press <Enter> for back:')
    IGToolkit()

def local_username():
    'Show my local username'
    os.system('clear')
    name = socket.gethostname()
    print (green + '\n[+] Your local username: %s' %name, end)
    input ('\n[-] Press <Enter> for back:')
    IGToolkit()

def operating_sys():
    'My operating system'
    os.system('clear')
    print (green + '\n[+] You operating system: %s' %sys.platform, end)
    input ('\n[-] Press <Enter> for back:')
    IGToolkit()

def local_ip():
    'Show my IP address'
    os.system('clear')
    name = socket.gethostname()
    addr = socket.gethostbyname(name)
    print (green + '\n[+] Your IP address: %s' %addr, end)
    input ('\n[-] Press <Enter> for back:')
    IGToolkit()

def net_status():
    'Check my network status'
    os.system('clear')
    os.system('ifconfig')
    input ('\n[-] Press <Enter> for back:')
    IGToolkit()

def logo():
    try:
        os.system('clear')
    except: 
        os.system('cls')

    igt = """ ___        _____                          
|_ _|  ____|__†__|           _ _  _   __ _    _
 | | // ____|| | ____  ____ | | || | /-/(_) _| |_
 | ||| ||__ || || -- || -- || | || |/-/ |-||__†__|
 | |||   -- || || -- || -- || | || |\-\ | |  | |
|___||______||_||____||____||_|_||_| \_\|_|  |_|
           {G}[Coded by: Learning :~#]{E}
            {R}   [Version: 1.0.1]{e}
{C}     [https://github.com/C-PyLx/IGToolkit]{e1}
{A}------------------------------------------------{e2}
    """.format(G=green, E=end, R=red, e=end, C=cyan, e1=end, A=pink, e2=end)
        
    print (pink + igt, end)

def exit_app():
    'Exit from IGToolkit'
    sys.exit('')

#Run Program:
IGToolkit()
