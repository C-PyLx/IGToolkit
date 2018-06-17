#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#------------------------------------
#Install the IGToolkit on your system
#Follow me on github:
#https://github.com/C-PyLx
#Report bugs to:
#https://t.me/Ac3ess
#------------------------------------
#You can use IGToolkit anywhere with command:
#IGToolkit in your terminal
#Thanks for using IGToolkit

green='\e[0;32m'
cyan='\e[0;36m'
end='\e[0;37m'

clear

echo -e $green '''___           _        _ _
|_ _|_ __  ___| |_ __ _| | |
 | || ._ \/ __| __/ _. | | |
 | || | | \__ \ || (_| | | |
|___|_| |_|___/\__\__._|_|_| .....
'''$end

echo -e $cyan '[+] Writing IGToolkit in your system...'$end
echo

sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install whois

mkdir /opt/IGToolkit
cp readme.txt /opt/IGToolkit/
cp version.txt /opt/IGToolkit/
cp install.sh /opt/IGToolkit/
cp uninstall.sh /opt/IGToolkit/
cp IGToolkit.py /opt/IGToolkit/

cp IGToolkit.py /usr/bin/IGToolkit
cp install.sh /usr/bin/IGToolkit-install
cp uninstall.sh /usr/bin/IGToolkit-uninstall

echo
echo -e $green '[✔] IGToolkit installed successfully in: /usr/bin/IGToolkit'$end
echo
echo -e $cyan '[+] You can use IGToolkit anywhere with command: IGToolkit in terminal.'$end
echo
