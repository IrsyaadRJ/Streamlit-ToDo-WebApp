# -*- mode: ruby -*-
# vi: set ft=ruby :

# A Vagrantfile to set up three VMs, two webservers and a database server,
# connected together using an internal network with manually-assigned
# IP addresses for the VMs.
# @author: Irsyaad Rijwan

Vagrant.configure("2") do |config|
    # Using ubuntu/64 box
    config.vm.box = "ubuntu/focal64"
    # Insert the key manually 
    # To avoid stuck during ssh session (Windows Error)
    config.ssh.insert_key = false
    config.ssh.private_key_path = "~/.vagrant.d/insecure_private_key"
    
    # Here is the section for defining the database server, which I have
  # named "dbserver".
    config.vm.define "dbserver" do |dbserver|
        dbserver.vm.hostname = "dbserver"
       
        # VM's private network IP 192.168.56.12
        dbserver.vm.network "private_network", ip: "192.168.56.12"
        dbserver.vm.synced_folder ".", "/vagrant", owner: "vagrant", group: "vagrant", mount_options: ["dmode=775,fmode=777"]

        dbserver.vm.provision "shell", path: "build-dbserver-vm.sh"
    end
  
    # First VM "webserver1"
    config.vm.define "webserver1" do |webserver1|
        # These are options specific to the webserver VM
        webserver1.vm.hostname = "webserver1"
        # Port forwarding to IP address 127.0.0.1 port 8081
        webserver1.vm.network "forwarded_port", guest: 80, host: 8081, host_ip: "127.0.0.1"
        # VM's private network IP 192.168.56.13
        webserver1.vm.network "private_network", ip: "192.168.56.13"

        # This following line is only necessary in the CS Labs... but that
        # may well be where markers mark your assignment.
        webserver1.vm.synced_folder ".", "/vagrant", owner: "vagrant", group: "vagrant", mount_options: ["dmode=775,fmode=777"]

        # Shell commands to provision the webserver1.
        webserver1.vm.provision "shell", path: "build-webserver1-vm.sh"
        # Shell commands to start the webserver1.
        # On the background using tmux
        webserver1.vm.provision "shell", path: "start-web-app1.sh"
    end
    # Second VM "webserver2"
    config.vm.define "webserver2" do |webserver2|
        # These are options specific to the webserver VM
        webserver2.vm.hostname = "webserver1"
        # Port forwarding to IP address 127.0.0.1 port 8082
        webserver2.vm.network "forwarded_port", guest: 80, host: 8082, host_ip: "127.0.0.1"
        # VM's private network IP 192.168.56.14
        webserver2.vm.network "private_network", ip: "192.168.56.14"
    
        # This following line is only necessary in the CS Labs... but that
        # may well be where markers mark your assignment.
        webserver2.vm.synced_folder ".", "/vagrant", owner: "vagrant", group: "vagrant", mount_options: ["dmode=775,fmode=777"]
    
        # Shell commands to provision the webserver1.
        webserver2.vm.provision "shell", path: "build-webserver2-vm.sh"
        # Shell commands to start the webserver2.
        # On the background using tmux
        webserver2.vm.provision "shell", path: "start-web-app2.sh"
    end
  
  
  end
  
  #  LocalWords:  webserver xenial64
  