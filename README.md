bodjango
========

Online monitoring website for physics DAQ systems. Tailored towards waveform data. Based on a django and mongodb backend and a bootstrap frontend.

Included files from other packages (highcharts, jquery, etc.) copyright their respective owners.

Installing
----------

For the mongodb DB access, a special version of Django is required.  Please following the instruction [here](http://django-mongodb-engine.readthedocs.org/en/latest/topics/setup.html).  The commands should be::

    $ pip install virtualenv
    $ virtualenv bodjango
    $ source bodjango/bin/activate
    $ pip install git+https://github.com/django-nonrel/django@nonrel-1.5
    $ pip install git+https://github.com/django-nonrel/djangotoolbox
    $ pip install git+https://github.com/django-nonrel/mongodb-engine

Then you must also install the following::

    $ pip install django-debug-toolbar south
