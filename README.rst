========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |codecov|
    * - package
      - | |version| |wheel|
.. |docs| image:: https://readthedocs.org/projects/jekyde/badge/?style=flat
    :target: https://readthedocs.org/projects/jekyde
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/devilicecream/jekyde.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/devilicecream/jekyde

.. |codecov| image:: https://codecov.io/github/devilicecream/jekyde/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/devilicecream/jekyde

.. |version| image:: https://img.shields.io/pypi/v/jekyde.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/jekyde

.. |wheel| image:: https://img.shields.io/pypi/wheel/jekyde.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/jekyde

.. end-badges

An example package. Generated with cookiecutter-pylibrary.

* Free software: MIT license

Installation
============

::

    pip install jekyde

Documentation
=============


https://jekyde.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
