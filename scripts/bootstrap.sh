#!/bin/bash

# install nettools
sudo apt install net-tools

# installing python and pip
# apt-get update 
apt-get install -y python
sudo apt-get install -y python3-pip

# docker installation 
sudo apt update

sudo apt install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"

apt-cache policy docker-ce

sudo apt-get install -y docker-ce

sudo systemctl status docker

# OPTIONAL - To run docker without sudo

# sudo usermod -aG docker ${USER}

# su - ${USER} 

# Prepare VM for Kubernetes installation
sudo apt-get update 

sudo apt-get install -y apt-transport-https ca-certificates curl

# Install Kubernetes

sudo mkdir -p -m 755 /etc/apt/keyrings

curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.29/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.29/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list

sudo apt update

sudo apt-get install -y kubeadm kubelet kubectl kubernetes-cni