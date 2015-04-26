from setuptools import setup

try:
    readme = open("README.rst")
    long_description = str(readme.read())
finally:
    readme.close()

setup(name='itolapi',
      version='1.2.0',
      description='API for interacting with itol.embl.de',
      long_description=long_description,
      url='http://github.com/albertyw/itolapi',
      author='Albert Wang',
      author_email='albertyw@mit.edu',
      license='MIT',
      packages=['itolapi'],
      install_requires=[
          'requests>=2.0, <3.0',
      ],
      scripts=['itolapi/Itol.py', 'itolapi/ItolExport.py'],
      test_suite="tests",
      tests_require=[
          'mock>=1.0.1',
          'tox',
      ],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
      ],
)
