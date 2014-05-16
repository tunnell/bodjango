bodjango
========

Online monitoring website for physics DAQ systems. Tailored towards waveform data. Based on a django and mongodb backend and a bootstrap frontend.

Included files from other packages (highcharts, jquery, etc.) copyright their respective owners.

Installing
----------

For the mongodb DB access, a special version of Django is required.  Please following the instruction [here](http://django-mongodb-engine.readthedocs.org/en/latest/topics/setup.html).  The commands should be::

    $ pip install virtualenv
    $ virtualenv bodjango
    $ cd bodjango
    $ source bodjango/bin/activate
    $ pip install django
    $ django-admin.py startproject monitoring
    $ echo export PYTHONPATH=$VIRTUAL_ENV/monitoring
    $ echo export DJANGO_SETTINGS_MODULE=monitoring.settings 
 
Make a copy of the repository::

    $ pip install git+https://github.com/django-nonrel/django@nonrel-1.5
    $ pip install git+https://github.com/django-nonrel/djangotoolbox
    $ pip install git+https://github.com/django-nonrel/mongodb-engine

Then you must also install the following::

    $ pip install django-debug-toolbar south

You should then be able to do::

    $ cd $VIRTUAL_ENV/monitoring
    $ python manage.py runserver

To start the test server.