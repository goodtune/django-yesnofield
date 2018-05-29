=============================
yesnofield
=============================

.. image:: https://badge.fury.io/py/django-yesnofield.svg
    :target: https://badge.fury.io/py/django-yesnofield

.. image:: https://travis-ci.org/goodtune/django-yesnofield.svg?branch=master
    :target: https://travis-ci.org/goodtune/django-yesnofield

.. image:: https://codecov.io/gh/goodtune/django-yesnofield/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/goodtune/django-yesnofield

Provide a subclass of BooleanField that handles the Yes/No use case.

Documentation
-------------

The full documentation is at https://django-yesnofield.readthedocs.io.

Quickstart
----------

Install yesnofield::

    pip install django-yesnofield

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_yesnofield.apps.YesNoFieldConfig',
        ...
    )

Add yesnofield's URL patterns:

.. code-block:: python

    from django_yesnofield import urls as django_yesnofield_urls


    urlpatterns = [
        ...
        url(r'^', include(django_yesnofield_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
