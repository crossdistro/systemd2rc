#!/usr/bin/env python

from distutils.core import setup

setup(name='systemd2rc',
    version='0.0.1',
    description='Conversion script to turn systemd unit files into rc scripts for various distributions',
    author='Pavel Šimerda',
    author_email='pavlix@pavlix.net',
    scripts=['systemd2rc']
)
