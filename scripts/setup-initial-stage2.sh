#!/bin/sh
# This script should be wrapped by another script that
# encloses all of these commands in "scl enable python27"
# i.e. scl enable python27 "path/to/this/script.sh"
# See also http://developerblog.redhat.com/2013/02/14/setting-up-django-and-python-2-7-on-red-hat-enterprise-6-the-easy-way/
echo "Installing pip"
easy_install pip # 2.7 version of pip
#
# Install virtualenvwrapper
#
echo "Install virtualenvwrapper"
pip install virtualenvwrapper
#source /usr/bin/virtualenvwrapper.sh
source /opt/rh/python27/root/usr/bin/virtualenvwrapper.sh
#
# Setup virtualenv
echo "Setup virtualenv"
mkdir -p /webapps/virtualenvs
export WORKON_HOME=/webapps/virtualenvs
mkvirtualenv eyedata
workon eyedata
# Install requirements (pip)
echo "Install requirements (pip)"
cd /webapps/code/eyeData
pip install -r requirements/production.txt
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
chown apache /webapps/data/eyedata/sqlite
#
# Create directory for uploaded files
#
# echo "Create data directory for uploaded files"
mkdir -p /webapps/data/eyedata/eyedata_uploaded_files
chown apache /webapps/data/eyedata/eyedata_uploaded_files
#
# Validate settings file
#
echo "Validate settings file"
cd /webapps/code/eyeData/eyedata
python manage.py validate --settings=eyedata.settings.production
#
# Create sqlite database + initial tables
#
echo "Create sqlite database + initial tables"
python manage.py syncdb --noinput --settings=eyedata.settings.production
# resolve "Site matching query does not exist" and setup root:root
# http://stackoverflow.com/questions/11476210/getting-site-matching-query-does-not-exist-error-after-creating-django-admin/23028198#23028198
# http://stackoverflow.com/questions/1466827/automatically-create-an-admin-user-when-running-djangos-manage-py-syncdb
#
# Permissions for database
#
chown apache /webapps/data/eyedata/sqlite/eyedata.db3
#
#
echo "Setting up Apache"
echo "Create www directories (media/static/wsgi-related)"
mkdir /var/www/eyedata
mkdir /var/www/eyedata/media # user uploads
mkdir /var/www/eyedata/static # images, js, css, etc.
mkdir /var/www/eyedata/eyedata # wsgi.py
#
echo "Run collectatic to copy files to the static www directory"
#
python manage.py collectstatic --noinput --settings=eyedata.settings.production
echo "Apache config"
cp /webapps/code/eyeData/eyedata/eyedata/vagrant-centos-wsgi.py /var/www/eyedata/eyedata/wsgi.py
cp /webapps/code/eyeData/deploy/vagrant-centos-eyedata.conf /etc/httpd/conf.d/eyedata.conf
service httpd start
chkconfig httpd on
# on HMDC VM, changed SELinux to "permissive" in /etc/selinux/config
