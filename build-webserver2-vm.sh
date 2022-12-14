#!/bin/bash
# Check for update
apt-get update
# install apache
apt-get install -y apache2

# Install tmux 
sudo apt install -y tmux
# install python and its package manager.
sudo apt install -y python3.11
sudo apt install -y python3-pip

# install python packages
sudo python3 -m pip install streamlit
sudo pip install jinja2 --upgrade
sudo python3 -m pip install streamlit-option-menu
sudo python3 -m	pip install cryptography
sudo python3 -m pip install sqlalchemy
sudo python3 -m pip install pymysql
sudo python3 -m pip install plotly

# Activate apache following mods to reseverse proxy.
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo a2enmod proxy_wstunnel
sudo a2enmod headers
# Restart apache to ensure that it runs properly.
sudo systemctl restart apache2
# Copy and paste the test-webapp1 to the apache's list of availabile sites.
cp /vagrant/web-app2.conf /etc/apache2/sites-available/
# install our website configuration and disable the default
a2ensite web-app2
a2dissite 000-default
sudo systemctl reload apache2

