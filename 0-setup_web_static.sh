#!/usr/bin/env bash
# set up the NGINX config for web_static
# install nginx
sudo apt-get -y update
sudo apt-get -y install nginx

# Make required directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Add simple content to the test index.html file
echo "Testing my nginx configuration" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '/listen 80 default_server;/a \ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Allow Nginx through the firewall
sudo ufw allow "Nginx HTTP"

# Restart Nginx to apply the changes
sudo service nginx restart

# Exit successfully
exit 0
