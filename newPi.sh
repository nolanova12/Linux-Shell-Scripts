#!/bin/bash
#Shell Script for updating a new Pi image
cd ~
pwd
echo "running update/upgrade"
sudo apt update 
sudo apt upgrade -y
sudo systemctl enable ssh
sudo systemctl start ssh 
echo "-----------"
echo "Checking SSH Status"
echo "---------------"
sudo systemctl status ssh|grep "Active