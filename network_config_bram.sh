#!/bin/bash
echo "Changing interfaces config to fit for Bram's home."
sudo cp /etc/network/interfacesbackup_bram /etc/network/interfaces
sudo service networking restart
