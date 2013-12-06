========
Usage
========

There are two ways to use Jetstream: either to perform some tasks on your data
using the 'jet' command-line tool provided by Jetstream, or as a part of your
own application.

In either case, Jetstream must first be configured, using YAML_. The
configuration tells Jetstream what components to instantiate and how, and how to
combine them into one or more pipes runnable by Jetstream.

Installation
------------

At the command line::

    $ easy_install jetstream

Or using pip::

    $ pip install jetstream

Or, if you have virtualenvwrapper installed::

    $ mkvirtualenv jetstream
    $ pip install jetstream

Next, add a configuration file. A file called `config.yaml` placed in the
current directory is used automatically if found.


Configuration
-----------------------
The YAML_ configuration consists of two or more sections declaring the
components to be used (at least an :term:`Input` and :term:`Output`) and a
section declaring the :term:`pipes`.

**Component configuration:**

Each :term:`component` is configured under a component type section which is
either 'inputs', 'introspectors', 'transformers', or 'outputs'. Under the type
section, each component is listed as:

.. code-block:: yaml

  <component title>: &<component_id>
    description: <some description here>
    use: <a fully-qualified Python dotted name of the factory>

The description field is optional but recommended. Also note that the
`component_id` can not include spaces. An example configuration of an
:term:`Input` :term:`component`:

.. code-block:: yaml

   inputs:
     my MySQL data source: &sqlsource
       description: an example MySQL data source
       use: mypackage.mymodule.get_my_sql_source

**Pipe configuration:**

Each :term:`pipe` is configured under 'pipes' section, and is of the form:

.. code-block:: yaml

  <pipe title>:
    - *<component_id>
    - *<component2_id>

Where there can be an arbitrary number of component id's listed. An example
configuration of a :term:`pipe` with two components:

.. code-block:: yaml

   pipes:
      example pipe:
         - *sqlsource
         - *csvoutput

Any number of components can be freely arranged into a :term:`pipe`, as long as
it is started by an :term:`Input`, and ends in an :term:`Output` - although if
there's no Output configured, Jetstream will add a standard Output that simply
prints out the :term:`data records`.

.. note:: The ampersand (&) and asterisk (*) characters are required; they are
   part of the YAML anchor/alias syntax.


**Full example:**

Here is the full configuration file from Jetstream tests:

.. literalinclude:: ../tests/test.yaml

Using the command-line tool
--------------------------------------

The `jet` tool provides means to load a YAML configuration, list
the pipes that have been configured, and run such pipes.

Get usage instructions by calling jet with `-h` or `--help` option::

   $ jet -h

Embedding Jetstream
--------------------------

To use Jetstream in your own project, use the Streamer
class directly::

   import jetstream.core as core

   streamer = core.Streamer(pipename, path_to_yaml_config_file)
   for record in streamer:
      # do whatever your app needs to do with the stream

For more details, see the Streamer API in the jetstream.core_
docs.

.. _YAML: http://en.wikipedia.org/wiki/YAML
.. _jetstream.core: http://jetstreamcore.rtfd.org/
