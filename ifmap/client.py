#!/usr/bin/python
#
# Copyright 2011, Infoblox, All Rights Reserved
#
# Open Source, see LICENSE
#

from logging import getLogger

log = getLogger(__name__) # when imported, the logger will be named "ifmap.client"

import requests
HttpException = requests.exceptions.HTTPError
from requests.auth import HTTPBasicAuth

namespaces = {
	'env'   :   "http://www.w3.org/2003/05/soap-envelope",
	'ifmap' :   "http://www.trustedcomputinggroup.org/2010/IFMAP/2",
	'meta'  :   "http://www.trustedcomputinggroup.org/2010/IFMAP-METADATA/2",
}

class client:
	"""
	IF-MAP client
	"""
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
			self._auth = HTTPBasicAuth(user, password)

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

				resp = requests.post(self.__url, headers=headers,
                        auth=self._auth, data=xml, verify=False)
				self.__last_sent = xml
				self.__last_received = resp.text

				log.debug("========  received IF-MAP response ========")
				log.debug("\n%s\n", resp.text)
				log.debug("========  /receive IF-MAP response ========")

				return resp.text

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
