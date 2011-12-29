# Copyright 2011, Infoblox, All Rights Reserved
#
# Open Source, see LICENSE
#

from xml.etree import ElementTree

class Response():
    """
    Base class to handle and parse IF-MAP responses
    """
    __xml = ""

    def __init__(self, result):
        """
        Take a result string and process it
        """
        if result: 
            __env = ElementTree.fromstring(result)
            __body = __env.find('{http://www.w3.org/2003/05/soap-envelope}Body')
            __response = __body.find('{http://www.trustedcomputinggroup.org/2010/IFMAP/2}response')
            self.__xml = __response.find('*')
            
    def element(self):
        """
        Returns the raw Element object
        """
        return self.__xml
    
    def __str__(self):
        """
        Print the XML tree as a string
        """
        return ElementTree.tostring(self.__xml)

class newSessionResult(Response):
    """
    newSessionResult
    """
    def __init__(self, result):
        self.__newSession = Response(result).element()
        
    def get_session_id(self):
        return self.__newSession.attrib['session-id']
    
    def get_publisher_id(self):
        return self.__newSession.attrib['ifmap-publisher-id']
        


 