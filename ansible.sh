#! /bin/bash
#
# ansible.#!/bin/sh
#
# Prepare bare Ubuntu server to run as Ansible control

sudo apt update

sudo apt install -y python-pip

pip install boto3 botocore

mkdir ~/.ssh 2> /dev/null

sudo hostname Ansible-Ctrl

sudo sed -i '1a127.0.1.1 Ansible-Ctrl' /etc/hosts

sudo timedatectl set-timezone Australia/Sydney

echo
echo upload PEM file to ~/.ssh and chmod to 0600
