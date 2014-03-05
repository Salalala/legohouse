#!/bin/bash

echo "Update our list of installed software"
sudo apt-get update
echo "Installing python libraries"
sudo apt-get install python-dev
sudo apt-get install python-rpi.gpio
echo "Installing depencies"
sudo apt-get build-dep python-psycopg2
echo "Installing pip"
sudo apt-get install python-pip
echo "Installing psycopg2"
sudo apt-get install python-psycopg2
echo "Installing matrix_keypad depencies"
sudo pip install matrix_keypad
