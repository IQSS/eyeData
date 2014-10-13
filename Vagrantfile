# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "puppet-vagrant-boxes.puppetlabs.com-centos-65-x64-virtualbox-puppet.box"
  config.vm.box_url = "http://puppet-vagrant-boxes.puppetlabs.com/centos-65-x64-virtualbox-puppet.box"

  # the git repo is available within the Vagrant VM for copying files, etc.
  config.vm.synced_folder ".", "/git/eyeData"

  # initial, one-time setup of Python 2.7, installation of Django
  config.vm.provision "shell", path: "scripts/setup-initial.sh"

  # from your laptop, access Apache running on the VM at http://localhost:8000
  config.vm.network "forwarded_port", guest: 80, host: 8000

end
