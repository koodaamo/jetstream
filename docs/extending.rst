Extending Jetstream
===============================

The primary means of extending Jetstream is by developing new data components,
which is relatively easy. The architecture overview describes how
:term:`data components` fit in Jetstream & what their role is.

The jetstream.component_ package template provides boilerplate for
bootstrapping your Jetstream component. First, install cookiecutter::

   $ pip install cookiecutter

Then build the component template package::

   $ cookiecutter git://github.com/koodaamo/jetstream.component

The result will be a boilerplate component that you can try out
as a part of a Jetstream pipeline right away.

.. _jetstream.component: https://github.com/koodaamo/jetstream.component

Architecture overview
-------------------------

This diagram illustrates how Jetstream provides for running
a configurable sequence of data-processing steps, implemented as a
':term:`pipe`' of :term:`Input`, :term:`Inspector`, :term:`Transformer`
and :term:`Output` components.

.. figure:: images/overview.png

Jetstream runs component pipes using what is called a :term:`Streamer`.
For a more detailed explanation, also see :doc:`streamer`.


Implementing components
--------------------------

.. note:: If you're not sure what kind of component to develop, maybe it's
   useful to read on some thoughts on what different components can be used
   for, see :doc:`cases`.

Jetstream delegates set-up tasks and component configuration to a component
factory. It is called with (optional) set of keyword arguments that can be
loaded from configuration or passed via the :term:`streamer` API. 

The factory is then expected to return a ready-to-run component: an iterable
iterable callable that accepts the :term:`data stream` as a parameter,
and produces a :term:`data stream` when iterated over.

Thus any function that returns a sequence (such as `list` or `tuple`),
a  generator (ie. a function that **yields**), or a class implementing
`__iter__` can all be used as a component.

An example of a very simple dummy component & its factory:

.. code:: python

   def factory():

      def component(stream):
         for record in stream:
            # this is just a pass-thru / echo component
            result = record
            yield result

      return component


Using a Jetstream base class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In practice, it usually makes sense to implement the factory and the component
using a single class that accepts the configuration settings as constructor
parameters, implements an `__iter__` method that *yields* (making the method a
generator), and implements `__call__` so that it returns `self`.

This is precisely what the (abstract) base classes in the jetstream.base module
provide. It is recommended that one of these classes be used as a base class
for a component:

.. autoclass:: jetstream.base.InputComponent
   :members:

.. autoclass:: jetstream.base.InspectorComponent
   :members:

.. autoclass:: jetstream.base.TransformerComponent
   :members:

.. autoclass:: jetstream.base.OutputComponent
   :members:

They simply implement a passthru/echo component that does nothing to the stream,
similar to the first simple example above.

For a minimal implementation using a base class, override the `__iter__` method
of a base component with a generator function (anything that *yields*):

.. code:: python

   def __iter__(self):
      "a do-nothing component implementation"

      for record in self._stream:
         # do something
         yield record

.. note:: The base classes make the stream parameter (passed to each
   component at initialization) available as `self._stream`.

Jetstream components are classified according to to their roles:

* :term:`Input` is expected to produce a stream.

* :term:`Inspector` is expected to not change the stream.

* :term:`Transformer` is expected to change the stream.

* :term:`Output` is expected to consume the stream.

For more, see :doc:`usage`.

.. note:: The first component of the pipe is given an empty stream
   (attempting to read from it raises `StopIteration`).

.. note:: An Output component must yield at least `None` as long as it keeps
   writing to a data endpoint.


.. _developing-inputs:

Input components
~~~~~~~~~~~~~~~~~~~

In addition to implementing some data reading capability, Input components need
to provide an indexer that returns a mapping of data to be indexed.

(attributename, attributetype) tuple. Jetstream will use that information to
index the data, associating it with the the Streamer run, which in turn logs
information such as configuration, source and timestamp.

The component should be able to handle the data stream regardless of how many
records it provides.

since the number of records that can be read may be limited
in many ways; for example by the data source:

 - data may contain a fixed number of records by nature
 - there may be usage limits to data volume or time of day
 - there is an error at data source

... or by user context:

 - data may be limited by authentication > authorization
 - only a subset of available data is requested by query terms
 - user may want a smaller number of records than what is available

... or due to an error occurring at the data source or network:

 - data stream may unexpectedly terminate, or may arrive only partially

It is of course also possible that data is available ad infinitum.

.. todo:: capability declarations related to stream reading abilities

.. _developing-inspectors:

Inspector components
~~~~~~~~~~~~~~~~~~~~~~

.. _developing-transformers:

Transformer components
~~~~~~~~~~~~~~~~~~~~~~

.. _developing-outputs:

Output components
~~~~~~~~~~~~~~~~~~~~~~

and an Output is
allowed to return an exhausted iterator.


Registering components
-------------------------

Components don't necessarily need to be registered; they can always be
referred to using the `use` field of the YAML component configuration.

However, registering components makes it easier to use them.

Jetstream uses the standard setuptools entry points API for pluggable component
registrations. Each entry point is expected to resolve to a component factory
that is a callable accepting two parameters:

 1. configuration settings (a mapping)
 2. the data :term:`streamer` (an iterable)

The entry points to register under are as follows, one for each component type:

 - jetstream.input
 - jetstream.inspector
 - jetstream.transformer
 - jetstrem.output

Here is an example entry point declaration to go into your package's `setup.py`:

.. code-block:: python

    entry_points = {
        'jetstream.input': [
            'NoSQLInput = jetstream.nosqlinput.component:get_component'
        ]
    },

This would register the `get_component` function found in module
`jetstream.nosqlinput.component` as the factory for an Input component called
"NoSQLInput".


