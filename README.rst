===============================
Overview
===============================

.. image:: https://badge.fury.io/py/jetstream.png
    :target: http://badge.fury.io/py/jetstream
    
.. image:: https://travis-ci.org/koodaamo/jetstream.png?branch=master
        :target: https://travis-ci.org/koodaamo/jetstream

.. image:: https://pypip.in/d/jetstream/badge.png
        :target: https://crate.io/packages/jetstream?version=latest

Jetstream is both a data batch processing tool and a framework for data
integration applications. It provides facilities for composing and
running data processing pipelines, configured using YAML syntax.

Jetstream is thoroughly documented at http://jetstream.rtfd.org.

Installing Jetstream by `pip install jetstream` pulls in the following
packages:

* jetstream.core_ provides the main framework
* jetstream.cli_ - provides the 'jet' command-line interface tool

The following common packages are under development and will be included
in once they are released:

* jetstream.http - supports reading and writing HTTP resources
* jetstream.csv - supports reading and writing CSV files
* jetstream.sql - supports SQL db reading and writing

It's easy to extend Jetstream yourself by implementing:

- Inputs for reading data from various sources
- Inspectors for e.g. validating data
- Transformers for parsing and modifying data
- Outputs for writing processed data somewhere else

The jetstream.component_ package template provides boilerplate for
bootstrapping your Jetstream component. First, install cookiecutter::

   $ pip install cookiecutter

Then build the component template package::

   $ cookiecutter git://github.com/koodaamo/jetstream.component

The result will be a boilerplate component that you can try out
as a part of a Jetstream pipeline right away.

.. _jetstream.core: https://github.com/koodaamo/jetstream.core
.. _jetstream.cli: https://github.com/koodaamo/jetstream.cli
.. _jetstream.component: https://github.com/koodaamo/jetstream.component
