v4.1.5 2024-08-24
-----------------

 - Update dependencies
 - Clean up testing
 - Remove Pyup


v4.1.4 2024-01-20
-----------------

 - Fix documentation on path args
 - Update dependencies
 - Switch from rst to markdown
 - Switch from setup.py to pyproject


v4.1.3 2024-01-16
-----------------

 - Fix API key character casing
 - Update dependencies
 - Various testing/cleanup


v4.1.2 2023-01-15
-----------------

 - Explicitly support iTOL API Key with examples
 - Update dependencies


v4.1.1 2022-11-05
-----------------

 - Support python 3.11
 - Refactors


v4.1.0 2022-04-04
-----------------

 - Fully add type definitions
 - Update dependencies
 - Optimize testing


v4.0.2 2022-01-25
-----------------

 - Fix executibility of `itol.py` and `itolexport.py`
 - Update test dependencies
 - Clean up packaging configuration


v4.0.1 2021-11-07
-----------------

 - Support Python 3.10
 - Update dependencies
 - Update readme
 - Disable integration testing because of subscription requirements
 - Switch from codeship to drone


v4.0.0 2020-01-05
-----------------

 - Drop support for python 2
 - Update dependencies


v3.0.3 2019-07-05
-----------------

 - Update dependencies
 - Clean up some tempfile operations
 - Remove support for python 3.4 and python 3.5


v3.0.2 2018-12-15
-----------------

 - Update upload/download url
 - Dependency updates
 - Minor refactor


v3.0.1 2018-08-08
-----------------

 - Removed extraneous old files from wheel release
 - Explicitly use relative imports

v3.0.0 2018-07-29
-----------------

 - Vastly simplified upload API (cli usage remains the same).
 - Removed `Itol.add_variable()` function, added `Itol.params` and and `Itol.add_file`
 - Lowercased all files, import from python package instead (i.e. `from itolapi import Itol`)

v2.0.2 2018-07-28
-----------------

 - Cleanup itolapi example scripts
 - Add integration tests against itol api
 - Better test coverage

v2.0.1 2018-07-24
-----------------

 - Simplify tests and get to 100% test coverage
 - Several code refactors

v2.0.0 2018-07-16
-----------------

 - Switched to itol4
 - Removed itol2 support

v1.3.2 2018-07-15
-----------------

 - Many internal changes to update packaging and testing

v1.3.1 2017-08-23
-----------------

- Basic support for itol2
- README fixes
- Dependency updates
- Testing updates

v1.3.0 2016-02-14
-----------------

- Fix upload urls for Itol
- Add test coverage
- Fix code quality checks

v1.2.2 2016-02-02
-----------------

- Add changelog
- Update Readme

v1.2.1 2015-06-22
-----------------

- Fixes for python 3 support

v1.2.0 2015-04-25
-----------------

- Add tox tests
- Switch from hacky python url requests to requests package
- Add support for python 3

v1.1.2 2015-03-15
-----------------

- Update PyPI classifiers

v1.1 2014-08-09
---------------

- Refactors and better readme

v1.0 2014-08-03
---------------

- Initial release of iTOL python API under MIT license
