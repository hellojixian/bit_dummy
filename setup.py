#!/usr/bin/env python

"""Installation script
Version handling borrowed from pandas project.
"""

import sys
import os
import warnings

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name = "bit_dummy",
     version = "100",
     description = "stock winning rate evaulation script",
     author = "Jixian Wang",
     author_email = "hellojixian@gmail.com",
     url = "https://github.com/hellojixian/bit_dummy",
     packages = ['bin'],
     install_requires = ['numpy','pandas','pymysql','configparser'],
     long_description = """Really long text here."""
)