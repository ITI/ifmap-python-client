#!/usr/bin/python
#
# Copyright 2011, Infoblox, All Rights Reserved
#
# Open Source, see LICENSE
#

import urllib
from logging import getLogger

log = getLogger(__name__) # when imported, the logger will be named "ifmap.client"

# Import either httplib2 or urllib2 and map to same name
try:
	import httplib2 as http_client_lib
	Http = http_client_lib.Http
	HttpException = http_client_lib.HttpLib2Error
except ImportError:
	import urllib2 as http_client_lib
	HttpException = (http_client_lib.URLError, http_client_lib.HTTPError)
	class Http(): # wrapper to use when httplib2 not available
		def request(self, url, method, body, headers):
			f = http_client_lib.urlopen(http_client_lib.Request(url, body, headers))
			return f.info(), f.read()

namespaces = {
	'env'   :   "http://www.w3.org/2003/05/soap-envelope",
	'ifmap' :   "http://www.trustedcomputinggroup.org/2010/IFMAP/2",
	'meta'  :   "http://www.trustedcomputinggroup.org/2010/IFMAP-METADATA/2",
}

class client:
	"""
	IF-MAP client
	"""
	http = Http()
	__url = None
	__session_id = None
	__publisher_id = None
	__last_sent = None
	__last_received = None
	__namespaces = None

	__envelope ="""<?xml version="1.0" encoding="UTF-8"?>
<env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope" %(ns)s>
  <env:Body>
		%(body)s
  </env:Body>
</env:Envelope>
"""

	def __init__(self, url, user=None, password=None, namespaces={}):
		if user and password:
			self.__password_mgr=http_client_lib.HTTPPasswordMgrWithDefaultRealm()
			self.__password_mgr.add_password(None, url, user, password)
			handler = http_client_lib.HTTPBasicAuthHandler(self.__password_mgr)
			opener = http_client_lib.build_opener(handler)
			http_client_lib.install_opener(opener)

		if namespaces:
				self.__namespaces = namespaces

		self.__url = url

	def last_sent(self):
		return self.__last_sent

	def last_received(self):
		return self.__last_received

	def envelope(self, body) :
		_ns = ""
		for ns_prefix, ns_uri in self.__namespaces.items():
			if ns_prefix == "env": break # don't add the envelope namespace again
			_ns += "xmlns:"+ns_prefix+'="'+ns_uri+'" '
		return self.__envelope % {'body':body, 'ns': _ns}

	def call(self, method, body):
		xml = self.envelope(body)
		headers={
		  'Content-type': 'text/xml; charset="UTF-8"',
		  'Content-length': str(len(xml)),
		  "SOAPAction": '"%s"' % (method),
		}
		try:
				log.info("sending IF-MAP message to server")
				log.debug("========  sending IF-MAP message ========")
				log.debug("\n%s\n", xml)
				log.debug("========  /sending IF-MAP message ========")

				response, content = self.http.request(self.__url,"POST", body=xml, headers=headers )
				self.__last_sent = xml
				self.__last_received = content

				log.debug("========  received IF-MAP response ========")
				log.debug("\n%s\n", content)
				log.debug("========  /receive IF-MAP response ========")

				return content

		except	HttpException, e:
				log.error("HTTP Connection error in IF-MAP client: %s", e.reason)
		except:
				log.error("Uknown error sending IF-MAP message to server")
				raise

	def set_session_id(self, session_id):
		self.__session_id = session_id

	def set_publisher_id(self, publisher_id):
		self.__publisher_id = publisher_id

	def get_session_id(self):
		return self.__session_id

	def get_publisher_id(self):
		return self.__publisher_id


if __name__ == "__main__":
	print """The ifmap client library is not meant to be run from the command line or python interpreter
- you should use it by including it in your python software. See testmap.py for an example.
Hint: add this line to use the library - 'from ifmap import ifmapClient' """
