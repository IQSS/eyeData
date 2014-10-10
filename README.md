eyeData
=======

Repo for DPSI Team eyeData. This project includes a set of tools for searching and exploring survey data on Dataverse.


----

## Local Install (on OS X)

This is a quick checklist to install eyeData on an OS X machine.  Currently, it installs the [twoscoops project template](https://github.com/twoscoops/django-twoscoops-project) for [Django 1.6](https://docs.djangoproject.com/en/1.6/), including creating a sqlite database and running a skeleton site. 

#### Install [pip](http://pip.readthedocs.org/en/latest/installing.html)

* use sudo if needed

#### Install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)

* depends on pip
* remember to set the (shell startup file)[http://virtualenvwrapper.readthedocs.org/en/latest/install.html#shell-startup-file]


#### Pull down the [eyeData repository](https://github.com/IQSS/eyeData)

* Use the [mac client](https://mac.github.com/) if desired

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

* Edit the [postactivate script for the virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/scripts.html#postactivate)

```
vim $VIRTUAL_ENV/bin/postactivate
```

'vim' may be any text editor

* add these lines to the postactivate file and save the file

```
export DJANGO_DEBUG=True
export DJANGO_SETTINGS_MODULE=eyedata.settings.local
```

* Test the 'postactivate' script from the command line

```
deactivate
workon eyedata
echo $DJANGO_SETTINGS_MODULE
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
