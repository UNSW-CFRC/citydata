# CityData

Generates a development CityData server.

Developer Workshop
------------------

Available at:

    http://geonode.org/dev-workshop


## Terms

    In the doco below:  
    * ENV = dev | test | prod
    * ORG = asu | cityfutures

## Create a custom project

Note: You can call your geonode project whatever you like following the naming conventions for python packages (generally lower case with underscores (``_``). In the examples below, replace ``citydata`` with whatever you would like to name your project.

## Clone this project

1. Open it locally, say in GitHub Desktop and Atom.

Now you can:
2. set the variables in:
  - ENV-ORG (inventory file)
  - group_vars/ORG

Now run the `citydata.yml` playbook to create the server, prepare it, install geonode, customise it and serve it in a production mode:

```
ansible-playbook citydata.yml -i ENV-ORG --ask-vault-pass
```

You will be prompted to enter the vault password.

If you don't have this you'll need to set and encrypt replacements for the encrypted variables using a new vault password.

# Configuration

Since this application uses geonode, base source of settings is ``geonode.settings`` module. It provides defaults for many items, which are used by geonode. This application has own settings module, ``citydata.settings``, which includes ``geonode.settings``. It customizes few elements:
 * static/media files locations - they will be collected and stored along with this application files by default. This is useful during development.
 * Adds ``citydata`` to installed applications, updates templates, staticfiles dirs, sets urlconf to ``citydata.urls``.

Whether you deploy development or production environment, you should create additional settings file. Convention is to make ``citydata.local_settings`` module. It is recommended to use ``citydata/local_settings.py``.. That file contains small subset of settings for edition. It should:
 * not be versioned along with application (because changes you make for your private deployment may become public),
 * have customized at least ``DATABASES``, ``SECRET_KEY`` and ``SITEURL``.

You can add more settings there, note however, some settings (notably ``DEBUG_STATIC``, ``EMAIL_ENABLE``, ``*_ROOT``, and few others) can be used by other settings, or as condition values, which change other settings. For example, ``EMAIL_ENABLE`` defined in ``geonode.settings`` enables whole email handling block, so if you disable it in your ``local_settings``, derived settings will be preserved. You should carefully check if additional settings you change don't trigger other settings.

To illustrate whole concept of chained settings:
```
    |  GeoNode configuration |             |   Your application default    |             |  (optionally) Your deployment(s) |
    |                        |             |        configuration          |             |                                  |
    |------------------------|-------------|-------------------------------|-------------|----------------------------------|
    |                        | included by |                               | included by |                                  |
    |   geonode.settings     |     ->      |  citydata.settings    |      ->     |  citydata.local_settings |
```
