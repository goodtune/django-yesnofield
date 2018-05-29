=====
Usage
=====

To use yesnofield in a project, add it to your `INSTALLED_APPS`:

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
