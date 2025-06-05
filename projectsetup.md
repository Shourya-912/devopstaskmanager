### Title: DevOps Task Manager – EC2 Deployment Setup Instructions

---
## ✅ Prerequisites
  - EC2 instance with Amazon Linux 2023 or compatible OS
  - .pem key pair downloaded (e.g., dev task.pem)
  - Docker & Docker Compose installed
  - Dynatrace account (optional for monitoring)
  - GitHub repository: https://github.com/Shourya-932/devopstaskmanager
    
---

## 🖥️ Step-by-Step Setup

1. **Login to EC2 Instance**
Open your local terminal and connect to your EC2 instance:
```
ssh -i "C:\Users\SHCHOURA\Downloads\<key_pair_file_name>.pem" ec2-user@<ec2_public_ip_address>
```

2. **Install Git & Clone Repository**
```
sudo dnf install git -y
git version  # (to verify installation)
git clone https://github.com/Shourya-912/devopstaskmanager.git
cd devopstaskmanager
```

3. **Run Docker Setup**
Make the script executable and run it:
```
chmod +x docker_setup.sh
./docker_setup.sh
```
If you face a Docker permission error, add the current user to the Docker group:
```
sudo usermod -aG docker ec2-user
exit  # Logout and re-login to apply changes
```
4.**Run Docker Containers**
Log in again and run:
```
docker-compose up -d  # Runs containers in background
docker ps             # Check running containers
```

To stop and clean up containers/images:
```
docker-compose down
docker image prune -a -f
```
5. **Edit Security Group (AWS Console)**
In your EC2 instance’s security group, add inbound rules:

| Type      | Description           | Auth Required |
|----------------|-------------|---------------------------------------------|
|SSH    | 22| Anywhere (0.0.0.0/0) or <your_ip>|
|custom TCP | 5000| Anywhere (0.0.0.0/0)|
|custom TCP | 3000| Anywhere (0.0.0.0/0)|
| HTTP | 80| Anywhere (0.0.0.0/0) |
| HTTPS | 443 |Anywhere (0.0.0.0/0)|


6. **NGINX Setup**
Run the NGINX setup script:
```
chmod +x nginx_setup.sh
./nginx_setup.sh
sudo systemctl status nginx  # Check if NGINX is running
```

To exit status screen: press q.
7. **Configure NGINX for Reverse Proxy**
Edit main config:
```
sudo nano /etc/nginx/nginx.conf
```

Inside the http section, add:
```
server {
    listen 80;
 
    location /api/ {
proxy_pass http://localhost:5000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
 
    location /task/ {
proxy_pass http://localhost:3000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

Also add this block in:
```
sudo nano /etc/nginx/conf.d/default.conf
```

8. **Test and Restart NGINX**
```   
sudo nginx -t  # Test config
sudo systemctl restart nginx
```

9. **API URLs for Testing**
Once everything is running, test APIs using:

`http://<your-ec2-public-ip>/api/...` → Flask API
`http://<your-ec2-public-ip>/task/...` → Node.js Task API

Refer to the project README.md for actual endpoint routes.

10. **(Optional) Enable Dynatrace Monitoring**
    
Go to Dynatrace > Deployment Status > Add Host.
Choose Linux and generate a new token.
Copy the installer command.
Run it on EC2 instance:
```
sudo /bin/sh Dynatrace-OneAgent-Linux.sh
```
(Your actual installer command will be provided by Dynatrace UI.)
Once installed, monitor the host from Dynatrace and create custom dashboards.

## ✅ You're Done!
Your DevOps project is now:
Cloned and running with Docker
Exposed via NGINX reverse proxy
Optionally monitored with Dynatrace
