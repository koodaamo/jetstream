#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='jetstream',
    version='0.1.0',
    description='Jetstream data processing framework',
    long_description=readme + '\n\n' + history,
    author='Petri Savolainen',
    author_email='petri.savolainen@koodaamo.fi',
    url='https://github.com/koodaamo/jetstream',
    packages=["jetstream"],
    namespace_packages=[
        'jetstream',
    ],
    package_dir={'jetstream': 'jetstream'},
    include_package_data=True,
    install_requires=[
       "jetstream.core",
       "jetstream.cli"
    ],
    license="BSD",
    zip_safe=False,
    keywords='jetstream',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)
