============
Contributing
============

Contributions are welcome, and they are greatly appreciated! There are
many ways to contribute and every little bit helps.

Ways to contribute
------------------

Add components
~~~~~~~~~~~~~~~~~~~~~

Please consider contributing any data components your develop back to the
Jetstream community.

See :doc:extending.

Report bugs
~~~~~~~~~~~~~~~~~~~~

Report bugs at the relevant package issue tracker:

https://github.com/koodaamo/jetstream/issues.

When reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.


Implement features
~~~~~~~~~~~~~~~~~~~~
Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~~

Although quite well documented, the project could always use more documentation, 
whether as part of the official Jetstream framework docs, in docstrings, or on the
web in blog posts, articles, and such.

Submit feedback
~~~~~~~~~~~~~~~~~~~~
The best way to send feedback is to file an issue at https://github.com/koodaamo/jetstream/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Developer guide
-------------------

Ready to contribute? Here's how to set up `jetstream` for local development.

Getting started
~~~~~~~~~~~~~~~~~~~~

1. Fork the `jetstream` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/jetstream.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv jetstream
    $ cd jetstream/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature
   
   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the tests, including testing other Python versions with tox::

    $ flake8 jetstream tests
    $ python setup.py test
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv. 

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull request guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 2.6, 2.7, and 3.3, and for PyPy. Check 
   https://travis-ci.org/koodaamo/jetstream/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
~~~~

To run a subset of tests::

	$ python -m unittest tests.test_jetstream
