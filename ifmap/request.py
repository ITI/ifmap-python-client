#!/usr/bin/python
#
# Copyright 2011, Infoblox, All Rights Reserved
#
# Open Source, see LICENSE
#

class RequestBase:
	""" foundation class for request factory """
	pass

class NewSessionRequest(RequestBase):
	""" newSessionRequest
	"""
	__max_poll_result = None
	def __init__(self, max_poll_result=None):
		if max_poll_result:
			self.__max_poll_result = max_poll_result

	def __str__(self):
		_mp = ""
		if self.__max_poll_result:
			_mp = 'max-poll-result-size="'+ self.__max_poll_result + '" '
		self.__XML = '<ifmap:newSession %s' % (_mp) + '/>';
		return self.__XML

