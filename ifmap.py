#!/usr/bin/python
#
# Copyright 2011, Infoblox, All Rights Reserved
#
# Open Source, see LICENSE
# 


from pysimplesoap.simplexml import SimpleXMLElement
from pysimplesoap.client import SoapClient
import urllib2

path = "file:///Users/aantonop/Dropbox/D-Corp/Development/ifmap-python-client/"
wsdl = path + "ifmap-2.0.wsdl"
base = path + "ifmap-base-2.0.xsd"
meta = path + "ifmap-metadata-2.0.xsd"

namespaces = {
	'ifmap'	:	"http://www.trustedcomputinggroup.org/2010/IFMAP/2",
	'meta'	:	"http://www.trustedcomputinggroup.org/2010/IFMAP-METADATA/2",
}

envelope = """<?xml version="1.0" encoding="UTF-8"?>
<env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope" xmlns:ifmap="http://www.trustedcomputinggroup.org/2010/IFMAP/2" xmlns:meta="http://www.trustedcomputinggroup.org/2010/IFMAP-METADATA/2" >
        <env:Body>
                %(body)s
        </env:Body>
</env:Envelope>"""

publish_blob = """<ifmap:publish session-id=\"%(sessionid)s\"><update lifetime="forever"><identity name="%(username)s" type="username" /><access-request name="111:23" /><metadata><meta:role ifmap-cardinality="multiValue"><name>%(role)s</name></meta:role></metadata></update>
<update lifetime="forever"><mac-address value="ff:11:22:33:44:55"  /><ip-address value="10.0.0.5"   />
<metadata><meta:ip-mac  ifmap-cardinality="multiValue" ><start-time >2009-10-27T00:00:00</start-time><end-time >2009-10-28T00:00:00</end-time>
<dhcp-server >10.0.0.3</dhcp-server></meta:ip-mac></metadata></update>
<update lifetime="forever"><access-request name="111:23"  /><ip-address value="10.0.0.5"   />
<metadata><meta:access-request-ip  ifmap-cardinality="singleValue" ></meta:access-request-ip></metadata></update>
<update lifetime="forever"><access-request name="111:23"  /><metadata><meta:capability  ifmap-cardinality="multiValue" >
<name >Trusted</name><administrative-domain >Infoblox</administrative-domain></meta:capability></metadata></update>
<update lifetime="forever"><device><name>123:45</name></device>
<metadata><meta:device-attribute  ifmap-cardinality="multiValue" ><name >AntiVirusRunning</name></meta:device-attribute></metadata></update>
</ifmap:publish>"""

class ifmapClient:
    """ IF-MAP Client """
    server = None
    session = None
    soapclient = None
        
    def __init__(self, url, user, password):
        
        self.server = {
            'url'       :   url,
            'user'      :   user,
            'password'  :   password,
        }
        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, self.server['url'], self.server['user'], self.server['password'])
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)

        
    def connect(self):
        
        if self.session:
            return self.session.sessionid
        
        else:
            self.soapclient = SoapClient(location = self.server['url'], action='')
            newSessionRequest = '<ifmap:newSession />'
            response = self.call('newSession', newSessionRequest)
            self.session = {'sessionid': response.newSessionResult['session-id'],
                'publisher_id': response.newSessionResult['ifmap-publisher-id'],
            }
                  
    def call(self, method, body):
        request = envelope % {'body':body}
        response = self.soapclient.send(method, request)
        responseXML = SimpleXMLElement(response, namespace=namespaces['ifmap'])
        return responseXML
    
    def publishtest(self):
        username = 'jdoe'
        role = 'employee'
        publish_req = publish_blob % {'sessionid': self.session['sessionid'],'username':username,'role':role, }
        response = self.call('publish', publish_req)
        return response
        
class ifmapIDFactory:
	pass

class IPAddress(ifmapIDFactory):
	"""
	XML Factory for an IP Address IF-MAP Identifier
	"""
	
	def __init__(self, ip_address, type=None, administrative_domain=None):
		self.__ip_address = ip_address
		self.__type = type
		self.__administrative_domain = administrative_domain
		return None;
		
	def administrative_domain(self):
		return self.__administrative_domain
	
	def ip_address(self):
		return self.__ip_address
	
	def type(self):
		return self.__type
	
	def __str__(self):
		self.__XML = "<ip-address"
		self.__XML += ' value="'+self.__ip_address+'"'
		# type and administrative_domain are optional 
		if self.__type:
			self.__XML +=' type="'+self.__type+'"'
		if self.__administrative_domain:
			self.__XML += ' administrative-domain="'+self.__administrative_domain+'"'
		self.__XML += " />"
		return self.__XML
	
class MACAddress(ifmapIDFactory):
	"""
	XML Factory for a MAC Address IF-MAP Identifier
	"""
	
	def __init__(self, mac_address, administrative_domain=None):
		self.__mac_address = mac_address
		self.__administrative_domain = administrative_domain
		return None;
		
	def administrative_domain(self):
		return self.__administrative_domain
	
	def mac_address(self):
		return self.__mac_address
	
	def __str__(self):
		self.__XML = "<mac-address"
		self.__XML += ' value="'+self.__mac_address+'"'
		# administrative_domain is optional 
		if self.__administrative_domain:
			self.__XML += ' administrative-domain="'+self.__administrative_domain+'"'
		self.__XML += " />"
		return self.__XML
	
class Device(ifmapIDFactory):
	"""
	XML Factory for a Device IF-MAP Identifier
	"""
	
	def __init__(self, name, aik_name=None):
		self.__name = name
		self.__aik_name = aik_name
		return None;
		
	def aik_name(self):
		return self.__aik_name
	
	def name(self):
		return self.__name
	
	def __str__(self):
		self.__XML = "<device>"
		self.__XML += '<name>'+self.__name+'</name>'
		# aik_name is optional 
		if self.__aik_name:
			self.__XML += '<aik-name>'+self.__aik_name+'<aik-name>'
		self.__XML += "</device>"
		return self.__XML
	
class AccessRequest(ifmapIDFactory):
	"""
	XML Factory for an Access Request IF-MAP Identifier
	"""
	
	def __init__(self, name, administrative_domain=None):
		self.__name = name
		self.__administrative_domain = administrative_domain
		return None;
		
	def administrative_domain(self):
		return self.__administrative_domain
	
	def name(self):
		return self.__name
	
	def __str__(self):
		self.__XML = "<access-request"
		self.__XML += ' name="'+self.__name+'"'
		# administrative_domain is optional 
		if self.__administrative_domain:
			self.__XML += ' administrative-domain="'+self.__administrative_domain+'"'
		self.__XML += " />"
		return self.__XML

class Identity(ifmapIDFactory):
	"""
	XML Factory for an IF-MAP Identifier
	"""
	
	def __init__(self, name, type=None, other_type=None, administrative_domain=None):
		self.__name = name # required
		self.__type = type # "aik_name"|"distinguished_name"|"dns_name"|"email_address"|"kerberos_principal"|"username"|"sip_uri"|"tel_uri"|"hip_hit"|"other"
		self.__other_type = other_type # vendor-specific type 
		self.__administrative_domain = administrative_domain
		return None;
		
	def administrative_domain(self):
		return self.__administrative_domain
	
	def name(self):
		return self.__name
	
	def type(self):
		return self.__type
	
	def other_type(self):
		return self.__other_type
	
	def __str__(self):
		self.__XML = "<identity"
		self.__XML += ' name="'+self.__name+'"'
		# type and administrative_domain are optional 
		if self.__type:
			self.__XML +=' type="'+self.__type+'"'
		if self.__other_type:
			self.__XML +=' other-type="'+self.__other_type+'"'
		if self.__administrative_domain:
			self.__XML += ' administrative-domain="'+self.__administrative_domain+'"'
		self.__XML += " />"
		return self.__XML
	
if __name__ == "__main__":
	print """The ifmap client library is not meant to be run from the command line or python interpreter
- you should use it by including it in your python software. See testmap.py for an example.
Hint: add this line to use the library - 'from ifmap import ifmapClient' """
