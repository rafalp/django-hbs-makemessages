=======================
django-hbs-makemessages
=======================

.. image:: https://travis-ci.org/rafalp/django-hbs-makemessages
    :target: https://travis-ci.org/rafalp/django-hbs-makemessages


Library providing ``django-admin-hbs.py`` script that exposes custom ``makemessages`` command that can extract language strings from .hbs and .handlebars files.

This library complements `django-ember-gettext <https://github.com/rafalp/django-ember-gettext>`_ Ember.js addon that provides Django's `gettext` support in Ember.js application.


Tutorial
========

Install library via pip:

    pip install django-hbs-makemessages

CD to directory containing ``locale`` directory and JS app and fire makemessages:

    django-admin-hbs.py makemessages -l en_us -d djangojs

Now check your locale's djangojs.po file for your locale and see if it contains translation files:

    #: emberapp/routes/application.js:8
    msgid "Connection lost"
    msgstr ""

    #: emberapp/routes/application.js:13
    msgid "Page not available"
    msgstr ""

    #: emberapp/routes/application.js:24
    msgid "Page not found"
    msgstr ""

    #: emberapp/templates/application.handlebars.:2
    #: emberapp/templates/application.hbs.:2
    msgid "Welcome to Ember.js!"
    msgstr ""

    #: emberapp/templates/application.handlebars.:3
    #: emberapp/templates/application.hbs.:3
    msgid "IndexController renders %(template)s template!"
    msgstr ""


Authors
=======

**Rafał Pitoń**

* http://rpiton.com
* http://github.com/rafalp
* https://twitter.com/RafalPiton


Copyright and license
=====================

Copyright © 2014 `Rafał Pitoń <http://github.com/ralfp>`_
This program comes with ABSOLUTELY NO WARRANTY.

This is free software and you are welcome to modify and redistribute it under the conditions described in the license.
For the complete license, refer to LICENSE.rst
