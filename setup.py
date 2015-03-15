from setuptools import setup

try:
    readme = open("README.rst")
    long_description = str(readme.read())
finally:
    readme.close()

setup(name='itolapi',
      version='1.1.2',
      description='API for interacting with itol.embl.de',
      long_description=long_description,
      url='http://github.com/albertyw/itolapi',
      author='Albert Wang',
      author_email='albertyw@mit.edu',
      license='MIT',
      packages=['itolapi'],
      install_requires=[
          'urllib2_file==0.2.1',
      ],
      scripts=['itolapi/Itol.py', 'itolapi/ItolExport.py'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
      ],
)
