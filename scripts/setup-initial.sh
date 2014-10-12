#!/bin/sh
echo "Setting up eyeData"
# Platform for
# Lightweight
# Applications from
# IQSS
# Data Science
useradd plaid
# HMDC VM has this group:
groupadd dvnadmin
usermod -g dvnadmin plaid
# EPEL already enabled on HMDC VM
rpm -Uvh http://dl.fedoraproject.org/pub/epel/6Server/x86_64/epel-release-6-8.noarch.rpm
# on HMDC VM, httpd is already installed
yum install -y httpd mod_wsgi ack elinks libjpeg-turbo-devel
echo "Installing Python 2.7"
rpm --import http://ftp.scientificlinux.org/linux/scientific/6.4/x86_64/os/RPM-GPG-KEY-sl
yum install -y http://ftp.scientificlinux.org/linux/scientific/6.4/x86_64/external_products/softwarecollections/yum-conf-softwarecollections-1.0-1.el6.noarch.rpm
yum install -y python27
echo "Setting up Django app with Python 2.7"
scl enable python27 "/webapps/code/eyeData/scripts/setup-initial-stage2.sh"
