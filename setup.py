#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path
from pathlib import Path
from typing import Dict

# Get the long description from the README file
here = Path(path.dirname(__file__))
with open(str(here / 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

about: Dict[str, str] = {}
with open(str(here / 'itolapi' / '__version__.py'), 'r') as f:
    exec(f.read(), about)


setup(name='itolapi',
      version=about['__version__'],
      description='API for interacting with itol.embl.de',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/albertyw/itolapi',
      author='Albert Wang',
      author_email='git@albertyw.com',
      license='MIT',
      package_data={"itolapi": ["py.typed"]},
      packages=find_packages(exclude=['tests']),
      install_requires=[
          'requests>=2.0,<3.0',
      ],
      scripts=['itolapi/itol.py', 'itolapi/itolexport.py'],
      test_suite="itolapi.tests",
      classifiers=[
          'Development Status :: 7 - Inactive',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'Typing :: Typed',
      ],
      keywords='tree life compbio biology bioinformatics',
      )
