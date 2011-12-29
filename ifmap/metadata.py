# Copyright 2011, Infoblox, All Rights Reserved
#
# Open Source, see LICENSE
#
from util import attr, link_ids

class MetadataBase:
    """ foundation class for metadata factory """
    pass

class Metadata(MetadataBase):
    """
    Metadata factory
    """
    __ns_uri = ''
    
    def __init__(self, name, value=None, attributes=None, ns_prefix=None, ns_uri=None, elements=''):
        self.__value = value
        self.__attributes = attributes
        self.__elements = elements
        
        if ns_prefix:
            self.__name = ns_prefix + ':' + name
        elif not ns_uri:
            self.__name = 'meta:' + name
            
        if ns_uri:
            if ns_prefix:
                self.__ns_uri = ' xmlns:' + ns_prefix + '="' + ns_uri + '"'
            else:
                self.__ns_uri = ' xmlns="' + ns_uri + '"'
    
    def __str__(self):
        __attr = ' '+ attr(self.__attributes)
        return '<metadata><' + self.__name + self.__ns_uri + __attr + '>' + self.__value + self.__elements + '</' + self.__name + '></metadata>'
        