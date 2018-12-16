iTOL Python API
===============

|PyPI|
|Python Version|
|License|

|Codeship|
|CodeCov|
|Code Climate|
|Dependency Status|


Python API for the Interactive Tree of Life (iTOL)

Created by Albert Wang (git at albertyw.com)

With Complements to: `iTOL (Interactive Tree of Life)`_, `Python requests package`.

This iTOL API allows local software to upload trees to iTOL using ``itol.py``
and export uploaded trees using ``itolexport.py`` using direct Python
calls or through shell.  An active internet connection to the
`iTOL website`_ is required.

Installation
------------

``pip install itolapi``

Uploading Trees To iTOL (itol.py)
---------------------------------

From Command Line
~~~~~~~~~~~~~~~~~

(If you need to do anything more than displaying basic tree structures,
you must call the Python iTOL API from within a Python program)

::

    $ itol.py /path/to/example.tree
    http://itol.embl.de/external.cgi?tree=1234567890&restore_saved=1

From Python
~~~~~~~~~~~

Running from a python program is much more flexible than running from
command line and allows access to all `iTOL options`_

::

    from itolapi import Itol
    itol_uploader = Itol()
    itol_uploader.add_file('/path/to/example.tree')
    itol_uploader.params['treeName'] = 'apple'
    status = itol_uploader.upload()
    assert status != False
    itol_uploader.comm.upload_output
    # SUCCESS: 1234567890
    itol_uploader.comm.tree_id
    # 1234567890
    itol_uploader.get_webpage()
    # http://itol.embl.de/external.cgi?tree=1234567890&restore_saved=1
    itol_uploader.get_itol_export()
    # <ItolExport.ItolExport instance at 0x207c5f0>

An example for using the Python iTOL API can found in
``examples/example.py``.

Downloading Trees From iTOL (itolexport.py)
-------------------------------------------

From Command Line
~~~~~~~~~~~~~~~~~

(If you would like to set any parameters other than the tree id,
location to save the file, file format, and whether to display datasets,
you must use ItolExport from a Python program)

::

    $ itolexport.py TREEID FILELOCATION FORMAT [OPTIONS]

Options include:
 * ``-d``: show datasets
 * ``-v``: verbose output
 * ``-h``: help

From Python
~~~~~~~~~~~

Running itolexport.py from a Python program allows you to use all the
options that iTOL has available.

::

    from itolapi import ItolExport
    itol_exporter = ItolExport()
    itol_exporter.add_export_param_value('tree', tree_id)
    assert format in ['png', 'svg', 'eps', 'ps', 'pdf', 'nexus', 'newick']
    itol_exporter.add_export_param_value('format', format)
    itol_exporter.add_export_param_value(param_key, param_value)
    itol_exporter.export(file_location)

Valid ``param_key`` and ``param_value`` values can be found on `the iTOL API page`_.

Bugs/Comments
-------------
Send bugs and comments as issues on the  `Github`_ repository.

Development
-----------
To run tests:

::

    python setup.py install
    pip install -r requirements-test.txt
    pip install -r requirements-test-python3.txt
    mypy itolapi
    coverage run setup.py test
    coverage report -m

To update PyPI:

::

    pip install twine
    python setup.py sdist bdist_wheel
    twine upload dist/*

.. _iTOL (Interactive Tree of Life): http://itol.embl.de/
.. _iTOL website: http://itol.embl.de/
.. _iTOL options: http://itol.embl.de/help.cgi#batch
.. _the iTOL API page: http://itol.embl.de/help.cgi#batch
.. _Github: https://github.com/albertyw/itolapi/


.. |PyPI| image:: https://img.shields.io/pypi/v/itolapi.svg
   :target: https://pypi.python.org/pypi/itolapi/
   :alt: Latest Version

.. |Python Version| image:: https://img.shields.io/pypi/pyversions/itolapi.svg

.. |License| image:: https://img.shields.io/pypi/l/itolapi.svg
   :target: https://pypi.python.org/pypi/itolapi/
   :alt: License


.. |Codeship| image:: https://codeship.com/projects/d6470c00-c832-0132-4536-627bbcd2f5ed/status?branch=master
    :target: https://codeship.com/projects/75058
    :alt: Codeship

.. |CodeCov| image:: https://codecov.io/github/albertyw/itolapi/coverage.svg?branch=master
    :target: https://codecov.io/github/albertyw/itolapi?branch=master

.. |Code Climate| image:: https://codeclimate.com/github/albertyw/itolapi/badges/gpa.svg
    :target: https://codeclimate.com/github/albertyw/itolapi
    :alt: CodeClimate

.. |Dependency Status| image:: https://pyup.io/repos/github/albertyw/itolapi/shield.svg
   :target: https://pyup.io/repos/github/albertyw/itolapi/
