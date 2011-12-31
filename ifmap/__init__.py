#!/usr/bin/python
#
# Copyright 2011, Infoblox, All Rights Reserved
#
# Open Source, see LICENSE
#

"""
ifmap-python client is an implementation of the TCG IF-MAP 2.0 protocol as a client library.
"""

import sys

#
# Project properties
#

__version__ = '0.1'
__build__=""

#
# Exceptions
#
class Error(Exception):
	"""
	Base class for exception handling
	"""
	def __init__(self, msg):
		Exception.__init__(self, "Error: '%s'" % msg)
