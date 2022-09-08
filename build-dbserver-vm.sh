#!/bin/bash

# Update Ubuntu software packages.
apt-get update
      
# Create a shell variable MYSQL_PWD that contains the MySQL root password
export MYSQL_PWD='insecure_mysqlroot_pw'

# Setting a root password on mysql in silent mode in ubuntu
echo "mysql-server mysql-server/root_password password $MYSQL_PWD" | debconf-set-selections 
echo "mysql-server mysql-server/root_password_again password $MYSQL_PWD" | debconf-set-selections

# Install the MySQL database server.
apt-get -y install mysql-server

# Start the MySQL server.
service mysql start

# Create a database.
echo "CREATE DATABASE fvision;" | mysql

# Create a database user "webuser" with the given password.
echo "CREATE USER 'webuser'@'%' IDENTIFIED BY 'insecure_db_pw';" | mysql

# Grant all permissions of the "fvision" database to its user "webuser" 
echo "GRANT ALL PRIVILEGES ON fvision.* TO 'webuser'@'%'" | mysql

# Set the MYSQL_PWD shell variable that the mysql command will
# try to use as the database password ...
export MYSQL_PWD='insecure_db_pw'

# Allow remote connection to MySQL server by changing its connection configuration.
# Change from only local network "127.0.0.1" to "0.0.0.0" to accept connections from any network interface.
sed -i'' -e '/bind-address/s/127.0.0.1/0.0.0.0/' /etc/mysql/mysql.conf.d/mysqld.cnf

# Restart MySQL server
service mysql restart
