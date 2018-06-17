#Uninstall IGToolkit

red='\e[0;31m'
green='\e[0;32m'
end='\e[0;37m'

echo -e $red '[+] UnInstalling IGToolkit from system...'$end

rm /opt/IGToolkit/*
rmdir /opt/IGToolkit

rm /usr/bin/IGToolkit
rm /usr/bin/IGToolkit-install
rm /usr/bin/IGToolkit-uninstall

sleep 1

echo
echo -e $green '[✔] IGToolkit uninstalled successfully.'$end
echo