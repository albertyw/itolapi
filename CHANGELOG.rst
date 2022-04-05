4.1.0 April 4, 2022
-------------------

 - Fully add type definitions
 - Update dependencies
 - Optimize testing


4.0.2 January 25, 2022
----------------------

 - Fix executibility of ``itol.py`` and ``itolexport.py``
 - Update test dependencies
 - Clean up packaging configuration


4.0.1 November 7, 2021
----------------------

 - Support Python 3.10
 - Update dependencies
 - Update readme
 - Disable integration testing because of subscription requirements
 - Switch from codeship to drone


4.0.0 January 5, 2020
---------------------

 - Drop support for python 2
 - Update dependencies


3.0.3 July 5, 2019
------------------

 - Update dependencies
 - Clean up some tempfile operations
 - Remove support for python 3.4 and python 3.5


3.0.2 December 15, 2018
-----------------------

 - Update upload/download url
 - Dependency updates
 - Minor refactor


3.0.1 August 8, 2018
--------------------

 - Removed extraneous old files from wheel release
 - Explicitly use relative imports

3.0.0 July 29, 2018
-------------------

 - Vastly simplified upload API (cli usage remains the same).
 - Removed ``Itol.add_variable()`` function, added ``Itol.params`` and and ``Itol.add_file``
 - Lowercased all files, import from python package instead (i.e. ``from itolapi import Itol``)

2.0.2 July 28, 2018
-------------------

 - Cleanup itolapi example scripts
 - Add integration tests against itol api
 - Better test coverage

2.0.1 July 24, 2018
-------------------

 - Simplify tests and get to 100% test coverage
 - Several code refactors

2.0.0 July 16, 2018
-------------------

 - Switched to itol4
 - Removed itol2 support

1.3.2 July 15, 2018
-------------------

 - Many internal changes to update packaging and testing

1.3.1 August 23, 2017
---------------------

- Basic support for itol2
- README fixes
- Dependency updates
- Testing updates

1.3.0 February 14, 2016
-----------------------

- Fix upload urls for Itol
- Add test coverage
- Fix code quality checks

1.2.2 February 2, 2016
----------------------

- Add changelog
- Update Readme

1.2.1 June 22, 2015
-------------------

- Fixes for python 3 support

1.2.0 April 25, 2015
--------------------

- Add tox tests
- Switch from hacky python url requests to requests package
- Add support for python 3

1.1.2 March 15, 2015
--------------------

- Update PyPI classifiers

1.1 August 9, 2014
------------------

- Refactors and better readme

1.0 August 3, 2014
------------------

- Initial release of iTOL python API under MIT license
