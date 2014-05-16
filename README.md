bodjango
========

Online monitoring website for physics DAQ systems. Tailored towards waveform data. Based on a django and mongodb backend and a bootstrap frontend.

Included files from other packages (highcharts, jquery, etc.) copyright their respective owners.

Installing
----------

For the mongodb DB access, a special version of Django is required.  Please following the instruction [here](http://django-mongodb-engine.readthedocs.org/en/latest/topics/setup.html).  The commands should be:

    $ pip install virtualenv
    $ virtualenv django
    $ cd django
    $ source bin/activate
    $ pip install django
    $ git clone https://github.com/<username>/bodjango.git

This actually creates the Django project:

    $ django-admin.py startproject monitoring

Set some enviromental variables, that must be set for running Django but also installing the MongoDB interface:

    $ echo export PYTHONPATH=$VIRTUAL_ENV/monitoring:$VIRTUAL_ENV/bodango >> $VIRTUAL_ENV/bin/activate
    $ echo export DJANGO_SETTINGS_MODULE=monitoring.settings >> $VIRTUAL_ENV/bin/activate
    $ source bin/activate
 
Install some stuff for MongoDB access:

    $ pip install git+https://github.com/django-nonrel/django@nonrel-1.5
    $ pip install git+https://github.com/django-nonrel/djangotoolbox
    $ pip install git+https://github.com/django-nonrel/mongodb-engine

Then you must also install the following:

    $ pip install django-debug-toolbar south

You should then be able to do:

    $ cd $VIRTUAL_ENV/monitoring

Edit the monitoring/settings.py file for the DB options and also installed apps.  For example:

```python
     DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'online',                 
        'HOST': '', 
        'PORT': '', 
    }
}
```

and

```python
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'runMonitor',
    'chartit',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'debug_toolbar',
    'log',
    'django_mongodb_engine',
    'control',
)
```

You can then start the server.

    $ python manage.py runserver

To start the test server.