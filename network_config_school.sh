#!/bin/bash
echo "Changing interfaces config to fit for school network."
sudo cp /etc/network/interfacesbackup_school /etc/network/interfaces
sudo service networking restart
