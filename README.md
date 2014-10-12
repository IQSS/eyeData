eyeData
=======

Repo for DPSI Team eyeData. This project includes a set of tools for searching and exploring survey data on Dataverse.


----

## Local Install (on OS X and Windows 8.1)

This is a quick checklist to install eyeData on an OS X or Windows 8.1 machine.  Currently, it installs the [twoscoops project template](https://github.com/twoscoops/django-twoscoops-project) for [Django 1.6](https://docs.djangoproject.com/en/1.6/), including creating a sqlite database and running a skeleton site. 

#### Install [pip](http://pip.readthedocs.org/en/latest/installing.html)

* use sudo if needed
* if on Windows, make sure [python](https://www.python.org/downloads/) is installed.

#### Install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)

* depends on pip
* if on windows, either install [virtualenvwrapper-win-1.1.5](https://pypi.python.org/pypi/virtualenvwrapper-win) or [cygwin](https://www.cygwin.com/).
* remember to set the (shell startup file)[http://virtualenvwrapper.readthedocs.org/en/latest/install.html#shell-startup-file]
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
``` 
or, on windows, [this](http://stackoverflow.com/questions/2615968/installing-virtualenvwrapper-on-windows) might be helpful.

#### Pull down the [eyeData repository](https://github.com/IQSS/eyeData)

* Use the [mac client](https://mac.github.com/) if desired or [windows client](https://windows.github.com/)

### Setup on the local machine

#### cd into the eyeData repository

```
cd ~\eyeData
```

#### Install the virtualenv and the requirements

This may take a minute or two.  Xcode needs to be installed.
    
```
mkvirtualenv eyedata
pip install -r requirements/local.txt
```

If you run into Xcode (or other errors) when running the install, google it.  Sometimes the [Xcode license agreement hasn't been accepted](http://stackoverflow.com/questions/26197347/agreeing-to-the-xcode-ios-license-requires-admin-privileges-please-re-run-as-r/26197363#26197363)

#### Configure settings (still in ~\eyeData)

* Edit the [postactivate script for the virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/scripts.html#postactivate).

```
vim $VIRTUAL_ENV/bin/postactivate
```
On windows:
```
vim %VIRTUAL_ENV%\Scripts\activate.bat
```

'vim' may be any text editor

* add these lines to the postactivate file and save the file

```
export DJANGO_DEBUG=True
export DJANGO_SETTINGS_MODULE=eyedata.settings.local
```
On windows:
```
set "DJANGO_DEBUG=True"
set "DJANGO_SETTINGS_MODULE=eyedata.setings.local"
```

* Test the 'postactivate' script from the command line

```
deactivate
workon eyedata
echo $DJANGO_SETTINGS_MODULE
```
On Windows, use:
```
echo %DJANGO_SETTINGS_MODULE%
```

You should see ```eyedata.settings.local```

#### Sync the database (still in ~\eyeData)

```
cd eyedata
python manage.py syncdb
```

* Follow the prompts to create a superuser, create tables, etc.

#### Run the test server (still in ~\eyeData\eyedata)

```
python manage.py runserver
```

* Feel grateful to be alive

#### Edit the template files

* Location ```~\eyeData\eyedata\templates```

* ```base.html``` is the over-arching template


## Working with the project (post installation)

```
cd ~\eyeData\eyedata
workon eyedata
python manage.py runserver
```

![basic-screenshot](https://github.com/IQSS/eyeData/blob/master/docs/eyeData.png)

## Vagrant environment

This git repository contains a [Vagrant](http://vagrantup.com) environment that is used to mimic the Linux server that hosts the application in production. If you have [Vagrant](http://www.vagrantup.com/) and [VirtualBox](http://virtualbox.org) installed you should be able to run `vagrant up` see the running eyeData app at http://localhost:8000 (but you'll need to set "DEBUG = True" in eyedata/eyedata/settings/production.py).
