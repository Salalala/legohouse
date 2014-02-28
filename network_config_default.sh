#!/bin/bash
echo "Changing interfaces config to default."
sudo cp /etc/network/interfacesbackup /etc/network/interfaces
sudo service networking restart
