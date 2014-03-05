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
#pip install psycopg2
