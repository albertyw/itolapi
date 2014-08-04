iTOL Python API
===============

Python API for the Interactive Tree of Life (iTOL)

Created by Albert Wang (albertyw at mit.edu)

With Complements to: `iTOL (Interactive Tree of Life)`_, `urllib2\_file
by Fabien Seisen`_

This iTOL API is meant to link between local programs written in Python
and the iTOL website. ``Itol.py`` can be used to upload trees and
datasets from a Python program or command line onto iTOL for processing
and viewing. ``ItolExport.py`` can export (download) trees from iTOL to
the local computer for viewing. An active internet connection to the
`iTOL website`_ is required.

Installation
------------

In order to use the iTOL Python API, you will need to install the
``urllib2_file`` python library. If you have pip installed, you only
need to run ``pip install urllib2_file``.

Files Required:

-  ``Itol.py``: Overall handling of parameters, datasets, tree file,
   processing of trees through calls to Comm and ItolExport
-  ``ItolExport.py``: Overall handling of parameters for
   exporting/downloading tree visualizations from itol
-  ``Comm.py``: Handles communication to itol website and stores
   returned data

Uploading Trees To iTOL (itol.py)
---------------------------------

RUNNING FROM COMMAND LINE
~~~~~~~~~~~~~~~~~~~~~~~~~

(If you need to do anything more than displaying basic tree structures,
you must call the Python iTOL API from within a Python program)

To run Python from the command line, a newick tree must be saved to a
file that can be accessed by the itol.py script. To upload the newick
tree to iTOL for processing, run itol.py with the script location as the
first argument. The output of the script should be a url that can be
used to access the drawn tree.

Examples:
^^^^^^^^^

``python /path/to/Itol.py /path/to/example.tree``

Example Output For A Good File:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``http://itol.embl.de/external.cgi?tree=18793532558412678134820&restore_saved=1``

RUNNING FROM A PYTHON PROGRAM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Running from a python program is much more flexible than running from
command line and allows access to all `iTOL options`_

The steps to run the iTOL Python API are:

1. Import the iTOL API In Python, ``import Itol``

2. Instantiate iTOL ``itol_uploader = Itol.Itol()``

3. Set the Tree
   ``itol_uploader.add_variable('treeFile','/path/to/file')``

4. Set Any Additional Parameters (Optional) To set parameters one by
   one, call ``itol_uploader.add_variable(var_name, var_value)`` as many
   times as needed. Dataset variables can be set with ``dataset#``
   prefixing the variable name using ``add_variable()``. The list of
   accepted variable names and allowed values is available on the [iTOL
   website(http://itol.embl.de/help/batch\_help.shtml).

5. Upload the tree ``itol_uploader.upload()`` The returned value will be
   False if iTOL got an error, or the tree id if the upload was good

6. Get the iTOL output: If the returned value of the previous step was
   True, Call ``itol_uploader.comm.upload_output`` to get the raw return
   statement of iTOL AND/OR Call ``itol_uploader.comm.tree_id`` to get
   the tree ID (string) created by iTOL for your upload AND/OR Call
   ``itol_uploader.get_webpage()`` to get the web page url at the iTOL
   website to view the uploaded tree AND/OR Call
   ``itol_uploader.get_itol_export()`` to get an instance of ItolExport
   in order to download your uploaded tree in different formats

An example for using the Python iTOL API can found in
``examples/example.py``.

Downloading Trees From iTOL (ItolExport.py)
-------------------------------------------

RUNNING FROM COMMAND LINE
~~~~~~~~~~~~~~~~~~~~~~~~~

(If you would like to set any parameters other than the tree id,
location to save the file, file format, and whether to display datasets,
you must use itolexport from a Python program)

To export pre-uploaded itol files, call
``python ItolExport.py TREEID FILELOCATION FORMAT`` where TREEID is the
itol id where the tree was uploaded, FILELOCATION is the location to
save the exported tree, and FORMAT is the type of export you would like
to perform. You can add a -r flag for verbose output and -d to also show
datasets. Call ``python itolexport.py -h`` for help.

RUNNING FROM A PYTHON PROGRAM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Running itolexport.py from a Python program allows you to use all the
options that iTOL has available. The steps to run itolexport from a
Python program are:

1. Import ``import ItolExport``

2. Instantiate ``itol_exporter = ItolExport.ItolExport()``

3. Select a tree ID to export Call
   ``itol_exporter.add_export_param_value('tree',tree_id)`` where
   ``tree_id`` is a string of the tree id on iTOL

4. Add an output format Call
   ``itol_exporter.add_export_param_value('format',format)`` where
   format represents the format to export. Allowed formats are png, svg,
   eps, ps, pdf, nexus, newick

5. Add any other parameters (Optional) Call
   ``itol_exporter.add_export_param_value(param_key,param_value)`` where
   ``param_key`` and ``param_value`` are the name of a parameter name
   and value. The allowed paramKeys and their values can be found on
   `the iTOL website`_.

6. Export Call ``itol_exporter.export(file_location)`` where
   ``file_location`` is the path to the location to write the export to.
   If a file is already in that location, it will be overwritten. This
   step may take a while depending on how big of a tree you are
   exporting.

Log issues on `Github`_ or send e-mails to Albert Wang for questions and
comments


.. _iTOL (Interactive Tree of Life): http://itol.embl.de/
.. _urllib2\_file by Fabien Seisen: https://github.com/seisen/urllib2_file
.. _iTOL website: http://itol.embl.de/
.. _iTOL options: http://itol.embl.de/help/batch_help.shtml
.. _the iTOL website: http://itol.embl.de/help/batch_help.shtml
.. _Github: https://github.com/albertyw/itolapi/issues
