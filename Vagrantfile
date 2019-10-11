# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "vm" do |vm|
    vm.vm.box = "ubuntu/bionic64"

    vm.vm.synced_folder '.', '/vagrant', disabled: true

    vm.vm.provision "ansible" do |ansible|
      ansible.playbook = "main.yml"
      ansible.extra_vars = {
        ansible_python_interpreter: '/usr/bin/python3'
      }
    end

    vm.vm.provider "virtualbox" do |v|
      v.name = "Docker Practice VM"
      v.memory = 1024
      v.cpus = 1
    end
  end
end
