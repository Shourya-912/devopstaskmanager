
echo "==== Updating packages ===="
sudo yum update -y

echo "==== Installing nginx ===="
sudo dnf install nginx -y

echo "==== Starting nginx ===="
sudo systemctl start nginx
sudo systemctl enable nginx

# echo "======checking status======="
# sudo systemctl enable nginx
