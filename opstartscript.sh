#!/bin/bash

echo "Update our list of installed software"
sudo apt-get -y update
echo "Installing python libraries"
sudo apt-get -y install python-dev
sudo apt-get -y install python-rpi.gpio
echo "Installing depencies"
sudo apt-get -y build-dep python-psycopg2
echo "Installing pip"
sudo apt-get -y install python-pip
echo "Installing psycopg2"
sudo apt-get -y install python-psycopg2
echo "Installing matrix_keypad depencies"
sudo pip install matrix_keypad
echo "Fix Locale settings to disable perl warning when sending notification"
sudo locale-gen nl_BE nl_BE.UTF-8 be_BE be_BE.UTF-8
sudo export LC_ALL=""
sudo export LANGUAGE = nl_BE
sudo localedef -v -c -i nl_BE -f UTF-8 nl_BE.UTF-8
echo "Download mpg321 sound package"
sudo apt-get -y install mpg321
