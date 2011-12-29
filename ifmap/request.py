#!/usr/bin/python
#
# Copyright 2011, Infoblox, All Rights Reserved
#
# Open Source, see LICENSE
#
from util import attr

class RequestBase:
	""" foundation class for request factory """
	pass

class NewSessionRequest(RequestBase):
	def __init__(self, max_poll_result=None):
		self.__max_poll_result = max_poll_result

	def __str__(self):
		return '<ifmap:newSession %s' % (attr({'max-poll-result-size':self.__max_poll_result})) + '/>';
		
class RenewSessionRequest(RequestBase):
	def __init__(self, session_id):
		self.__session_id = session_id

	def __str__(self):
		return '<ifmap:renewSession %s' % (attr({'session-id':self.__session_id})) + '/>';

class EndSessionRequest(RequestBase):
	def __init__(self, session_id):
		self.__session_id = session_id

	def __str__(self):
		return '<ifmap:endSession %s' % (attr({'session-id':self.__session_id})) + '/>';
	
class PublishRequest(RequestBase):
	__session_id = None
	def __init__(self, session_id, operations, namespaces=None, validation=None):
		self.__session_id = session_id
		self.__namespaces = namespaces
		self.__validation = validation
		self.__operations = operations

	def __str__(self):
		_attr = attr({'session-id': self.__session_id, 'validation' : self.__validation})
		return '<ifmap:publish %s' % _attr + '>' + self.__operations + '</ifmap:publish>'
	