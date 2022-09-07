# Streamlit-ToDo-WebApp
Using Vagrant to automate the process of deploying and hosting web app with a remote database and an admin panel.
- Using vagrant to deploy 3 local VMs.
  - 1 local VM for database server. 
  - 1 local VM for webserver to host a streamlit web app for the user. 
  - 1 local VMs for a webserver to host a streamlit admin panel for the admin.

## Vagrant's Configuration
- Using the Vagrant Shell provisioner to execute a shell script (bash) and do the following things :
  - Installing :
    - MySQL
    - Apache
    - tmux
    - Python
    - Python's package manager (pip)
    - All the necessary python packages.
 - Create database and configure its user and connection.
 - Proxy reverse and install our web app configuration and disable the default.

## ToDo Web App Features:
- Login page and sign up form.
- User is able to Create,Read,Update and Delete a task.
- All the data is stored in remote database.
- Using SQLAlchemy to interact with MySQL database.
- Using PyMySQL to connect to a MySQL database server from Python.
- Hosted on different server from the Admin panel

## Admin Panel Features:
- Admin is able to delete a user.
- View insight of the tasks that have been created.
- Hosted on different server from the Web App.
