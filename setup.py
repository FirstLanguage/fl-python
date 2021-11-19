# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages

if sys.version_info[0] < 3:
    with open('README.md', 'r') as fh:
        long_description = fh.read()
else:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()

setup(
    name='firstlanguageapi',
    version='1.0.0',
    description='Python client library for FirstLanguage API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Us',
    author_email='info@firstlanguage.in',
    url='https://dev.firstlanguage.in/contactus',
    packages=find_packages(),
    install_requires=[
        'jsonpickle~=1.4, >= 1.4.1',
        'requests~=2.24',
        'cachecontrol~=0.12.6',
        'python-dateutil~=2.8.1',
        'enum34~=1.1, >=1.1.10'
    ],
    tests_require=[
        'nose>=1.3.7'
    ],
    test_suite = 'nose.collector'
)