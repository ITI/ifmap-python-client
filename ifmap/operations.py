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
        
        
        