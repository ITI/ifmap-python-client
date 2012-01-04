Copyright 2011, Infoblox, Inc. All Rights Reserved

Released under BSD, see LICENSE

IF-MAP Python Client Library
============================

This is a Python library for building IF-MAP clients.

It supports the Trusted Computing Group IF-MAP protocol v.2.0
There is no support for IF-MAP 1.0 or 1.1 and there are no plans to support those versions.

Currently Implemented:

* Session: newSession, endSession, renewSession
* Publish: Update, Notify, Delete
* Identities: IP, MAC, Device, Access Request, Identity, Custom Identifier
* Metadata: IF-MAP metadata and custom namespace metadata
* Search: Search on all of the above IDs
* Subscribe: SubscribeUpdate, SubscribeDelete
* Purge: PurgeRequest
* Poll: PollRequest

TODO:
* Implement XML schema validation (as optional)



Installation
------------

Get the python library from github:
$ git clone git://github.com/IF-MAP/ifmap-python-client.git

Or download as a zip file and unzip:
https://github.com/IF-MAP/ifmap-python-client/zipball/master


Requirements
------------

The main library has no python requirements, except for ifmap.response (response.py) which uses xlm.etree to parse results.
You can implement the client entirely without response.py and parse your own responses in anyway you like.
If you do not use response.py, then you do not need any Python libraries. If you use it, you need xml.etree.

Library Structure
-----------------

* ifmap - the directory containing the library components
* testmap.py - a test script showing example code

Code Example
-------
An example of working code:

from xml.etree import ElementTree # Only needed to parse results

from ifmap.client import client, namespaces
from ifmap.request import NewSessionRequest, RenewSessionRequest, EndSessionRequest, PublishRequest, SearchRequest
from ifmap.id import IPAddress, MACAddress, Device, AccessRequest, Identity, CustomIdentity
from ifmap.operations import PublishUpdateOperation, PublishNotifyOperation, PublishDeleteOperation
from ifmap.util import attr, link_ids
from ifmap.response import Response, newSessionResult
from ifmap.metadata import Metadata

mapclient = client("https://127.0.0.1:8443", 'test', 'test', namespaces)

result = mapclient.call('newSession', NewSessionRequest())
mapclient.set_session_id(newSessionResult(result).get_session_id())
mapclient.set_publisher_id(newSessionResult(result).get_publisher_id())

meta = str(Metadata('role', 'employee', {'ifmap-cardinality':'multiValue'}))
pubreq = PublishRequest(mapclient.get_session_id(), str(PublishUpdateOperation(id1=str(IPAddress("10.0.0.1")), metadata=meta, lifetime='forever')))
result = mapclient.call('publish', pubreq)
print Response(result)

searchreq = SearchRequest(mapclient.get_session_id(), str(IPAddress("10.0.0.1")), validation="None")
result = mapclient.call('search', searchreq)
