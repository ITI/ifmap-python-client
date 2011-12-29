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
	
class SearchRequest(RequestBase):
	"""
	Search request factory
	session_id
	identifier (single, or linked with link_ids())
	namespaces
	validation "None"|"BaseOnly"|"MetadataOnly"|"All"
	search_parameters - dictionary eg. {'max_depth':'3', 'max_size':'10000'}
		result_filter             => string, #Optional. Rules for extracting specific data from the results
		match_links               => string, #Optional. Filter to match links to be followed, unmatched links will not be followed in the search process
		max_depth                 => number, #Optional. Maximum distance of any included identifiers. Start depth is equal to 0
		max_size                  => number, #Optional. Maximum size in bytes of the results
		terminal_identifier_type  => string, #Optional. Terminal identifier type of the search request
	"""
	def __init__(self, session_id, identifier, namespaces=None, validation=None, search_parameters={}):
		self.__session_id = session_id
		self.__identifier = identifier
		self.__namespaces = namespaces
		self.__validation = validation
		self.__parameters = search_parameters

	def __str__(self):
		_params = attr(self.__parameters)
		_attr = attr({'session-id': self.__session_id, 'validation' : self.__validation})
		return '<ifmap:search ' + _attr + _params + '>' +  self.__identifier + '</ifmap:search>'
	
class SubscribeRequest(RequestBase):
	"""
	Subscribe request factory
	"""
	
	def __init__(self, session_id, validation=None, namespaces=None, operations=None):
		self.__session_id = session_id
		self.__namespaces = namespaces
		self.__validation = validation
		self.__operations = operations
	
	def __str__(self):
		_attr = attr({'session-id': self.__session_id, 'validation' : self.__validation})
		return '<ifmap:subscribe %s' % _attr + '>' + self.__operations + '</ifmap:subscribe>'
	
class PollRequest(RequestBase):
	def __init__(self, session_id, validation=None, namespaces=None):
		self.__session_id = session_id
		self.__namespaces = namespaces
		self.__validation = validation
	
	def __str__(self):
		_attr = attr({'session-id': self.__session_id, 'validation' : self.__validation})
		return '<ifmap:poll %s' % _attr + '/>'
	
class PurgeRequest(RequestBase):
	def __init__(self, session_id, publisher_id=None, validation=None):
		self.__session_id = session_id
		self.__publisher_id = publisher_id
		self.__validation = validation

	def __str__(self):
		__attr = attr({'session-id':self.__session_id, 'validation':self.__validation,'ifmap-publisher-id':self.__publisher_id})
		return '<ifmap:purgePublisher %s' % __attr + '/>';
