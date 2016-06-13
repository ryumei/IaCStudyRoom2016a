# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  # config.vm.box_check_update = false

  config.vm.network "forwarded_port", guest: 8080, host: 18080, id: "Tomcat"
  # config.vm.network "private_network", ip: "192.168.33.10"

  config.vm.synced_folder "./", "/vagrant"

  config.vm.provider "virtualbox" do |vb|
      vb.gui = false
  #   vb.memory = "1024"
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update -y
    apt-get install python-dev libffi-dev libssl-dev sshpass -y
    curl -kL https://bootstrap.pypa.io/get-pip.py | python
    pip install ansible
  SHELL
end
