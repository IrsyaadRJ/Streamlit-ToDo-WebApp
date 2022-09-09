# Streamlit-ToDo-WebApp
Using Vagrant to automate the process of deploying and hosting web app with a remote database and an admin panel.
- Using vagrant to deploy 3 local VMs.
  - 1 local VM for database server. 
  - 1 local VM for webserver to host a streamlit web app for the user. 
  - 1 local VMs for a webserver to host a streamlit admin panel for the admin.

## How to run this on your local computer
- Clone this repo
- Install Vagrant and VirtualBox
- Run the following command on your command line interpreter:
```
vagrant up
```
- Go to http://localhost:8081 on your local browser
- To use ToDo application login as a user.
- To use admin's interface login as an admin.
- User's credentials :
```
  ID          Password
  blank404    blank404
  biggie      biggie
```
- Admin credentials:
```
  ID          Password
  admin       admin
```
## How does it work:
- Each private network is given its own private network to be able to communicate with one another.
- Using tmux to be able to run streamlit web app and admin panel on the background.
- A local Streamlit server on a given port will automatically run once the scripts is executed.
- Reverse proxy is needed to host the streamlit apps on the Apache Web Server on a the same port as the port forwarding configuration.
  - Without doing reverse proxy our streamlit application can only connect with our local VM.
- Enable our web application configuration on Apache and disable the default.
- Port forwarding on a given port in vagrant configuration allows our local computer to be able to connect to the streamlit application.

## Vagrant's Configuration
- Port forwarding to local host on a given port.
- Unique private network for each VMs.
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
- Using Plotly to create graphs.
- Hosted on different server from the Admin panel
- Running on the backround of the VM using tmux

## Admin Panel Features:
- Admin is able to delete a user.
- View insight of the tasks that have been created.
- Hosted on different server from the Web App.
- Running on the backround of the VM using tmux
- Using Plotly to create graphs.
