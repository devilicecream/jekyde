#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")
    ) as fh:
        return fh.read()


setup(
    name="jekyde",
    version="0.0.1",
    license="MIT license",
    description="An example package. Generated with cookiecutter-pylibrary.",
    long_description="%s\n%s"
    % (
        re.compile("^.. start-badges.*^.. end-badges", re.M | re.S).sub(
            "", read("README.rst")
        ),
        re.sub(":[a-z]+:`~?(.*?)`", r"``\1``", read("CHANGELOG.rst")),
    ),
    author="Walter Danilo Galante",
    author_email="walter.galante@ovalmoney.com",
    url="https://github.com/devilicecream/jekyde",
    packages=find_packages("jekyde"),
    package_dir={"": "jekyde"},
    py_modules=[splitext(basename(path))[0] for path in glob("*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Utilities",
    ],
    project_urls={
        "Documentation": "https://jekyde.readthedocs.io/",
        "Changelog": "https://jekyde.readthedocs.io/en/latest/changelog.html",
        "Issue Tracker": "https://github.com/devilicecream/jekyde/issues",
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires=">=3.6.*",
    install_requires=[
        "zope.sqlalchemy<=1.0",
        "six>=1.7",
        "SQLAlchemy>=1.3.0",
        "Ming<=0.9.0",
        "PyMySQL<=0.9.3",

    ],
    extras_require={},
    entry_points={},
)
