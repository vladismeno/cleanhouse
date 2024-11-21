#!/bin/bash

set -e  # Останавливаем скрипт при ошибке

echo "Updating system..."
sudo apt update && sudo apt upgrade -y

echo "Installing 'make'..."
sudo apt-get install -y make

echo "Setting up Docker keyrings..."
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo "Adding Docker repository..."
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

echo "Updating package list..."
sudo apt update

echo "Installing Docker components..."
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

echo "Installation complete."
