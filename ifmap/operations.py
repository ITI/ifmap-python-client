# Copyright 2011, Infoblox, All Rights Reserved
#
# Open Source, see LICENSE
#
from util import attr, link_ids

class OperationBase:
	""" foundation class for operation factory """
	pass

class PublishUpdateOperation(OperationBase):
    def __init__(self, id1, metadata, id2=None, lifetime=None):
        self.__id = link_ids(id1, id2)
        self.__metadata = metadata
        self.__lifetime = lifetime
    
    def __str__(self):
        if self.__lifetime:
            _attr = attr({'lifetime':self.__lifetime})
            return '<update %s>' % _attr + self.__id + self.__metadata + '</update>'
        else:
            return '<update>' + self.__id + self.__metadata + '</update>'
    
class PublishDeleteOperation(OperationBase):
    def __init__(self, id1, id2=None, filter=None):
        self.__id = link_ids(id1, id2)
        self.__filter = filter
    
    def __str__(self):
        if self.__filter:
            _attr = attr({'filter':self.__filter})
            return '<delete %s>' % _attr + self.__id + '</delete>'
        else:
            return '<delete>' + self.__id + '</delete>'

class PublishNotifyOperation(OperationBase):
    def __init__(self, id1, metadata, id2=None):
        self.__id = link_ids(id1, id2)
        self.__metadata = metadata
    
    def __str__(self):
        return '<notify>' + self.__id + self.__metadata + '</notify>'
        
class SubscribeUpdateOperation(OperationBase):
	"""
	SubscribeUpdate factory
	name
	identifier (single, or linked with link_ids())
	search_parameters - dictionary eg. {'max_depth':'3', 'max_size':'10000'}
		result_filter             => string, #Optional. Rules for extracting specific data from the results
		match_links               => string, #Optional. Filter to match links to be followed, unmatched links will not be followed in the search process
		max_depth                 => number, #Optional. Maximum distance of any included identifiers. Start depth is equal to 0
		max_size                  => number, #Optional. Maximum size in bytes of the results
		terminal_identifier_type  => string, #Optional. Terminal identifier type of the search request
	"""
	def __init__(self, name, identifier, search_parameters={}):
		self.__name = name
		self.__identifier = identifier
		self.__parameters = search_parameters
		
	def __str__(self):
		__attr = attr(self.__parameters)
		return '<update name="'+ self.__name + '" ' + __attr + '>' + self.__identifier +'</update>'
	
class SubscribeDeleteOperation(OperationBase):
	def __init__(self, name):
		self.__name = name
	
	def __str__(self):
		return '<delete name="'+ self.__name + '" />'
	


        
        