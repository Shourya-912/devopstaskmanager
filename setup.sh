#!/bin/bash
 
echo "==== Updating packages ===="
sudo dnf update -y
 
echo "==== Installing Docker ===="
sudo dnf install -y docker
 
echo "==== Starting Docker ===="
sudo systemctl start docker
sudo systemctl enable docker
docker --version

echo "==== Installing Docker Compose ===="
sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.4/docker-compose-linux-x86_64" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
 
echo "==== Installing Git ===="
sudo dnf install -y git
git --version
 
echo "==== Cloning your repo ===="
git clone https://github.com/Shourya-912/devopstaskmanager.git
 
echo "==== Running Docker Compose ===="
cd devopstask manager

echo "==== Adding user to Docker group ===="
sudo usermod -aG docker ec2-user
exit

echo "=======git pull if changes done========"
git pull
docker-compose down -v
docker image prune -a -f
docker-compose up --build

