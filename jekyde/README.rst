========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/jekyde/badge/?style=flat
    :target: https://readthedocs.org/projects/jekyde
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/devilicecream/jekyde.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/devilicecream/jekyde

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/devilicecream/jekyde?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/devilicecream/jekyde

.. |requires| image:: https://requires.io/github/devilicecream/jekyde/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/devilicecream/jekyde/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/devilicecream/jekyde/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/devilicecream/jekyde

.. |version| image:: https://img.shields.io/pypi/v/jekyde.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/jekyde

.. |commits-since| image:: https://img.shields.io/github/commits-since/devilicecream/jekyde/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/devilicecream/jekyde/compare/v0.0.1...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/jekyde.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/jekyde

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/jekyde.svg
    :alt: Supported versions
    :target: https://pypi.org/project/jekyde

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/jekyde.svg
    :alt: Supported implementations
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
