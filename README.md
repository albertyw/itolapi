iTOL Python API
===============

![PyPI](https://img.shields.io/pypi/v/itolapi)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/itolapi)
![PyPI - License](https://img.shields.io/pypi/l/itolapi)

[![Build Status](https://drone.albertyw.com/api/badges/albertyw/itolapi/status.svg)](https://drone.albertyw.com/albertyw/itolapi)
[![Test Coverage](https://api.codeclimate.com/v1/badges/365d217b9dd6c2f97cb4/test_coverage)](https://codeclimate.com/github/albertyw/itolapi/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/365d217b9dd6c2f97cb4/maintainability)](https://codeclimate.com/github/albertyw/itolapi/maintainability)

> Notice: Due to [iTOL requiring paid subscriptions for batch uploads](https://itol.embl.de/infoReg.cgi),
> this library will be deprecated after October 1, 2020.

Python API for the Interactive Tree of Life (iTOL)

Created by Albert Wang (git at albertyw.com)

With Complements to [iTOL (Interactive Tree of Life)](http://itol.embl.de/).

This iTOL API allows local software to upload trees to iTOL using
`itol.py` and export uploaded trees using `itolexport.py` using direct
Python calls or through shell. An active internet connection to the
[iTOL website](http://itol.embl.de/) is required.

Installation
------------

`pip install itolapi`

Uploading Trees To iTOL (itol.py)
---------------------------------

### From Command Line

(If you need to do anything more than displaying basic tree structures,
you must call the Python iTOL API from within a Python program)

```
$ itol.py /path/to/example.tree
http://itol.embl.de/external.cgi?tree=1234567890&restore_saved=1
```

### From Python

Running from a python program is much more flexible than running from
command line and allows access to all [iTOL options](http://itol.embl.de/help.cgi#batch).

```python
from itolapi import Itol
from pathlib import Path


itol_uploader = Itol()
itol_uploader.add_file(Path('/path/to/example.tree'))
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
```

An example for using the Python iTOL API can found in
`examples/example.py`.

Downloading Trees From iTOL (itolexport.py)
-------------------------------------------

### From Command Line

(If you would like to set any parameters other than the tree id,
location to save the file, file format, and whether to display datasets,
you must use ItolExport from a Python program)

```
$ itolexport.py TREEID FILELOCATION FORMAT [OPTIONS]
```

Options include:
 - `-d`: show datasets
 - `-v`: verbose output
 - `-h`: help

### From Python

Running itolexport.py from a Python program allows you to use all the
options that iTOL has available.

```python
from itolapi import ItolExport
from pathlib import Path


itol_exporter = ItolExport()
itol_exporter.add_export_param_value('tree', tree_id)
assert format in ['png', 'svg', 'eps', 'ps', 'pdf', 'nexus', 'newick']
itol_exporter.add_export_param_value('format', format)
itol_exporter.add_export_param_value(param_key, param_value)
itol_exporter.export(Path('/path/to/example_tree'))
```

Valid `param_key` and `param_value` values can be found on [the iTOL API
page](http://itol.embl.de/help.cgi#batch).

Bugs/Comments
-------------

Send bugs and comments as issues on the
[itolapi Github](https://github.com/albertyw/itolapi/) repository.

Development
-----------

To run tests:

```bash
pip install -e .[test]
ruff check .
mypy .
coverage run -m unittest
```
