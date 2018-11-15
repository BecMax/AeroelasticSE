#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': 'Peter Graf',
 'author_email': 'peter.graf@nrel.gov',
 'include_package_data': True,
 #'install_requires': ['openmdao.main'],
 'keywords': ['openmdao'],
 'license' : 'Apache License, Version 2.0',
 'version' : '0.1.0',
 'name': 'AeroelasticSE',
 'package_data': {'AeroelasticSE': []},
 'package_dir': {'': 'src'},
 'packages': ['AeroelasticSE','AeroelasticSE.Turbsim_mdao','AeroelasticSE.Util'],
 'zip_safe': False}


setup(**kwargs)

