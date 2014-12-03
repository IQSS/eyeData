#!/bin/sh
echo "Setting up eyeData"
# Platform for
# Lightweight
# Applications from
# IQSS
# Data Science
useradd plaid
# EPEL already enabled on HMDC VM
rpm -Uvh http://dl.fedoraproject.org/pub/epel/6Server/x86_64/epel-release-6-8.noarch.rpm
# on HMDC VM, httpd is already installed
yum install -y httpd mod_wsgi ack elinks libjpeg-turbo-devel
# need gcc-c++ for pandas to avoid "gcc: error trying to exec 'cc1plus'"
yum install -y gcc-c++
echo "Installing Python 2.7"
rpm --import http://ftp.scientificlinux.org/linux/scientific/6.4/x86_64/os/RPM-GPG-KEY-sl
yum install -y http://ftp.scientificlinux.org/linux/scientific/6.4/x86_64/external_products/softwarecollections/yum-conf-softwarecollections-1.0-1.el6.noarch.rpm
# for scipy
yum install blas-devel lapack-devel
echo "Setting up Django app with Python 2.7"
echo "Installing pip for Python 2.7"
scl enable python27 "easy_install pip"
echo "Install virtualenvwrapper"
scl enable python27 "pip install virtualenvwrapper"

echo "Setup virtualenv directory"
mkdir -p /webapps/virtualenvs
chown plaid /webapps/virtualenvs
mkdir /webapps/code
chown plaid /webapps/code
su plaid -l -s /bin/sh -c 'cd /webapps/code && git clone https://github.com/IQSS/eyeData.git'
cp /webapps/code/eyeData/deploy/files/etc/sudoers.d/plaid /etc/sudoers.d

cp /git/eyeData/eyedata/eyedata/settings/secret_settings_prod.json /webapps/code/eyeData/eyedata/eyedata/settings/secret_settings_prod.json
chown plaid:apache /webapps/code/eyeData/eyedata/eyedata/settings/secret_settings_prod.json
chmod 440 /webapps/code/eyeData/eyedata/eyedata/settings/secret_settings_prod.json
#
# Create directory for sqlite db
#
echo "Create general data directory"
#
mkdir -p /webapps/data/eyedata
chown apache /webapps/data/eyedata
#
echo "Create data directory for sqlite db"
mkdir -p /webapps/data/eyedata/sqlite
chown plaid /webapps/data/eyedata/sqlite
chmod 664 -R /webapps/data/eyedata/sqlite/

#
# configure apache
#
echo "Configure Apache"
cp /webapps/code/eyeData/deploy/vagrant-centos-eyedata.conf /etc/httpd/conf.d/eyedata.conf
chown plaid /etc/httpd/conf.d/eyedata.conf

# quick fix to make Apache run Python 2.7
cp /git/eyeData/deploy/files/usr/lib64/httpd/modules/mod_wsgi.so.python2.7 /usr/lib64/httpd/modules/mod_wsgi.so.python2.7
cp -a /etc/httpd/conf.d/wsgi.conf /etc/httpd/conf.d/wsgi.conf.orig
cp /git/eyeData/deploy/files/etc/httpd/conf.d/wsgi.conf /etc/httpd/conf.d/wsgi.conf
cp -a /etc/sysconfig/httpd /etc/sysconfig/httpd.orig
cp /git/eyeData/deploy/files/etc/sysconfig/httpd /etc/sysconfig/httpd

echo "Create /var/www directory owned by plaid"
mkdir /var/www/eyedata
chown plaid /var/www/eyedata

#
# run main setup script as "plaid" user with python 2.7
#
su plaid -l -s /bin/sh -c 'scl enable python27 "/webapps/code/eyeData/scripts/setup-initial-stage2.sh"'

#
# apache and plaid need write access to the database
#
chown apache:plaid /webapps/data/eyedata/sqlite/eyedata.db3
chmod 664 /webapps/data/eyedata/sqlite/eyedata.db3
#
# Create directory for uploaded files, writable by apache
#
echo "Create data directory for uploaded files"
mkdir -p /webapps/data/eyedata/eyedata_uploaded_files
chown apache /webapps/data/eyedata/eyedata_uploaded_files

service httpd start
chkconfig httpd on
# on HMDC VM, changed SELinux to "permissive" in /etc/selinux/config
