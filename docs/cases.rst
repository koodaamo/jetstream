Data component use cases
==============================

Each component type has clearly defined roles with responsibilities and/or
constraints that should be followed in order to fully benefit from
functionality offered by Jetstream.

However the component classification is considered inclusive rather than
exclusive: responsibilities can be exceeded as long as constraints are
not broken.

For example, when an Input or Output is placed inside the pipe (rather
than at the pipe start / end), however, the following is possible with them:

* :term:`Input` can interleave stream from the previous component(s) with
  its own, effectively joining data from two sources.

* :term:`Output` can pass stream from previous component to next, effectively
  splitting data towards two destinations.

A component could also fulfill more than one role: for example implement both
an Input and (a validating) Inspector, and a Transformer.

If the application domain is narrow and specific, or if it looks like
the probability of single-role components finding use inside other
pipe configurations is low, it may make sense to have fewer components
implement more than one role. If it seems all roles should therefore be
combined into just one component, Jetstream is perhaps not a good fit for
the use case - rather, a custom app should be built.

On the other hand, it makes sense to refactor any generic, easily reusable
functionalities into their own components.

Here are some type-specific notes to help choose the right component type
for each use case, and how to combine components to achieve desired result when
it's not possible to get that from a single component.


Input components
-----------------

An :term:`Input` **connects to a data source and produces a data
stream**. It does nothing else. Given that, an input component is typically set
as the first component of the pipe. In that case, there is no :term:`data pipe`
passed to it as an input parameter.

However, if a pipe is configured so that the input component is not the first
one, it receives a data pipe, and can then be used to implement following
actions on received data:

* append more records to the end of :term:`data stream`
* mix produced records with existing records

An input MAY NOT modify the structure or content of data passed to it. To modify
data in any way, always use a transformer.

For developing inputs, see :ref:`developing-inputs`.

Inspector components
---------------------

An :term:`Inspector` **reads the data but does not touch (or output) it**.
However it has **control over the processing** of the :term:`data stream`,
and may include parts of data within its own non-data output. An inspector can
thus perform for example one or more of the following actions:

* validate data
* flag it
* log events
* alert user
* summarize data
* analyze it

For developing inspectors, see :ref:`developing-inspectors`.

Transformer components
-----------------------

:term:`Transformer` modifies data and passes it on, and may also drop records.
Thus a transformer can be naturally used to:

- rearrange fields
- filter out data records
- convert data from a type to another
- modify data labels and/or values

A transformer may also add to the data. It is however limited to using the data
it has received as input, including any information available within the
Jetstream system, such as configuration information passed to the transformer.
It may not fetch data on its own from any other, external data source.

For developing Transformers, see :ref:`developing-transformers`.

Output components
------------------

An :term:`Output` **connects to a :term:`data destination` and writes data to
it**. So the end of the pipe always has some sort of Output configured, even if
it is simply some code that reads and prints out the data, for example.

When not configured as pipe end, an output component can be used to:

* copy data to another destination

.. todo:: add loop-back data source/destination functionality to Jetstream

For developing Outputs, see :ref:`developing-outputs`.
