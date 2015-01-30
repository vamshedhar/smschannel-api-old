#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sms-channel-api
version = sms-channel-api.__version__

setup(
    name='sms-channel-api',
    version=version,
    author='',
    author_email='vamshedhar@gmail.com',
    packages=[
        'sms-channel-api',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['sms-channel-api/manage.py'],
)
