"""
 Script to perform tests on ifmap library

>>> 1+1 # make sure at least one test passes
2
>>> print IPAddress("10.0.0.1","IPv4","ifmaplab")
<ip-address administrative-domain="ifmaplab" type="IPv4" value="10.0.0.1" />
>>> print IPAddress("10.0.0.1","IPv4",)
<ip-address type="IPv4" value="10.0.0.1" />
>>> print IPAddress("10.0.0.1",)
<ip-address value="10.0.0.1" />
>>> print IPAddress("3ffe:1900:4545:3:200:f8ff:fe21:67cf","IPv6","ifmaplab")
<ip-address administrative-domain="ifmaplab" type="IPv6" value="3ffe:1900:4545:3:200:f8ff:fe21:67cf" />
>>> print IPAddress("3ffe:1900:4545:3:200:f8ff:fe21:67cf","IPv6",)
<ip-address type="IPv6" value="3ffe:1900:4545:3:200:f8ff:fe21:67cf" />
>>> print IPAddress("3ffe:1900:4545:3:200:f8ff:fe21:67cf",)
<ip-address value="3ffe:1900:4545:3:200:f8ff:fe21:67cf" />
>>> print MACAddress("aa:bb:cc:dd:ee:ff","ifmaplab",)
<mac-address administrative-domain="ifmaplab" value="aa:bb:cc:dd:ee:ff" />
>>> print MACAddress("aa:bb:cc:dd:ee:ff",)
<mac-address value="aa:bb:cc:dd:ee:ff" />
>>> print Device("123:45")
<device><name>123:45</name></device>
>>> print Device("123:45","aikdummynamef34feccc28b3d44f")
<device><name>123:45</name><aik-name>aikdummynamef34feccc28b3d44f<aik-name></device>
>>> print AccessRequest("111:23","ifmaplab",)
<access-request name="111:23" administrative-domain="ifmaplab" />
>>> print AccessRequest("111:23",)
<access-request name="111:23" />
>>> print Identity("john.doe")
<identity name="john.doe" />
>>> print Identity("john.doe@example.com", type="email_address")
<identity name="john.doe@example.com" type="email_address" />
>>> print Identity("ef9b13e5df7dae502c51db7ca4624552", type="other", other_type="RFID")
<identity name="ef9b13e5df7dae502c51db7ca4624552" type="other" other-type="RFID" />
>>> print Identity("ef9b13e5df7dae502c51db7ca4624552", type="other", other_type="RFID", administrative_domain="ifmaplab")
<identity name="ef9b13e5df7dae502c51db7ca4624552" type="other" other-type="RFID" administrative-domain="ifmaplab" />
>>> print CustomIdentity("student-id")
<custom-identifier><student-id /></custom-identifier>
>>> print CustomIdentity("student-id", "nsu")
<custom-identifier><nsu:student-id /></custom-identifier>
>>> print CustomIdentity("student-id", "nsu","http://nsu.example.org/student")
<custom-identifier><nsu:student-id xlmns=nsu:http://nsu.example.org/student /></custom-identifier>
>>> print CustomIdentity("student-id", namespace="http://nsu.example.org/student")
<custom-identifier><student-id xlmns=http://nsu.example.org/student /></custom-identifier>
>>> print CustomIdentity("student-id", attributes={'ID':"1864b64efe4903d7f45b4cdbdad38ab7d828e499", 'serial':"S1223505",})
<custom-identifier><student-id serial="S1223505" ID="1864b64efe4903d7f45b4cdbdad38ab7d828e499" /></custom-identifier>
>>> print CustomIdentity("student-id", "nsu", "http://nsu.example.org/student", attributes={'ID':"1864b64efe4903d7f45b4cdbdad38ab7d828e499", 'serial':"S1223505",})
<custom-identifier><nsu:student-id xlmns=nsu:http://nsu.example.org/student serial="S1223505" ID="1864b64efe4903d7f45b4cdbdad38ab7d828e499" /></custom-identifier>
>>> print NewSessionRequest('10000')
<ifmap:newSession max-poll-result-size="10000" />
>>> print NewSessionRequest()
<ifmap:newSession />
>>> print RenewSessionRequest('12345678')
<ifmap:renewSession session-id="12345678" />
>>> print EndSessionRequest('12345678')
<ifmap:endSession session-id="12345678" />
>>> print PublishUpdateOperation(id1=str(IPAddress("10.0.0.1")), metadata='<meta></meta>')
<update><ip-address value="10.0.0.1" /><meta></meta></update>
>>> print PublishUpdateOperation(id1=str(IPAddress("10.0.0.1")), metadata='<meta></meta>', lifetime='forever')
<update lifetime="forever" ><ip-address value="10.0.0.1" /><meta></meta></update>
>>> print PublishUpdateOperation(id1=str(IPAddress("10.0.0.1")), id2=str(IPAddress("10.0.0.2")), metadata='<meta></meta>')
<update><link><ip-address value="10.0.0.1" /><ip-address value="10.0.0.2" /></link><meta></meta></update>
>>> print PublishUpdateOperation(id1=str(IPAddress("10.0.0.1")), id2=str(IPAddress("10.0.0.2")), metadata='<meta></meta>', lifetime='forever')
<update lifetime="forever" ><link><ip-address value="10.0.0.1" /><ip-address value="10.0.0.2" /></link><meta></meta></update>
>>> print PublishDeleteOperation(id1=str(IPAddress("10.0.0.1")))
<delete><ip-address value="10.0.0.1" /></delete>
>>> print PublishDeleteOperation(id1=str(IPAddress("10.0.0.1")), id2=str(IPAddress("10.0.0.2")))
<delete><link><ip-address value="10.0.0.1" /><ip-address value="10.0.0.2" /></link></delete>
>>> print PublishDeleteOperation(id1=str(IPAddress("10.0.0.1")), id2=str(IPAddress("10.0.0.2")), filter='filter1')
<delete filter="filter1" ><link><ip-address value="10.0.0.1" /><ip-address value="10.0.0.2" /></link></delete>
>>> print PublishDeleteOperation(id1=str(IPAddress("10.0.0.1")), filter='filter1')
<delete filter="filter1" ><ip-address value="10.0.0.1" /></delete>
>>> print PublishNotifyOperation(id1=str(IPAddress("10.0.0.1")), metadata='<meta></meta>')
<notify><ip-address value="10.0.0.1" /><meta></meta></notify>
>>> print PublishNotifyOperation(id1=str(IPAddress("10.0.0.1")), id2=str(IPAddress("10.0.0.2")), metadata='<meta></meta>')
<notify><link><ip-address value="10.0.0.1" /><ip-address value="10.0.0.2" /></link><meta></meta></notify>
>>> print PublishRequest('12345678', str(PublishUpdateOperation(id1=str(IPAddress("10.0.0.1")), id2=str(IPAddress("10.0.0.2")), metadata='<meta></meta>', lifetime='forever')))
<ifmap:publish session-id="12345678" ><update lifetime="forever" ><link><ip-address value="10.0.0.1" /><ip-address value="10.0.0.2" /></link><meta></meta></update></ifmap:publish>
>>> print PublishRequest('12345678', str(PublishUpdateOperation(id1=str(IPAddress("10.0.0.1")), id2=str(IPAddress("10.0.0.2")), metadata='<meta></meta>', lifetime='forever')), validation='MetadataOnly')
<ifmap:publish session-id="12345678" validation="MetadataOnly" ><update lifetime="forever" ><link><ip-address value="10.0.0.1" /><ip-address value="10.0.0.2" /></link><meta></meta></update></ifmap:publish>
>>> print Response('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><ns3:Envelope xmlns:ns2="http://www.trustedcomputinggroup.org/2010/IFMAP/2" xmlns:ns3="http://www.w3.org/2003/05/soap-envelope"><ns3:Body><ns2:response><newSessionResult ifmap-publisher-id="test-2100079558-1" session-id="1323996407-1025975286-283779864-1097320563"/></ns2:response></ns3:Body></ns3:Envelope>')
<newSessionResult ifmap-publisher-id="test-2100079558-1" session-id="1323996407-1025975286-283779864-1097320563" />
>>> print newSessionResult('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><ns3:Envelope xmlns:ns2="http://www.trustedcomputinggroup.org/2010/IFMAP/2" xmlns:ns3="http://www.w3.org/2003/05/soap-envelope"><ns3:Body><ns2:response><newSessionResult ifmap-publisher-id="test-2100079558-1" session-id="1323996407-1025975286-283779864-1097320563"/></ns2:response></ns3:Body></ns3:Envelope>').get_session_id()
1323996407-1025975286-283779864-1097320563
>>> print newSessionResult('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><ns3:Envelope xmlns:ns2="http://www.trustedcomputinggroup.org/2010/IFMAP/2" xmlns:ns3="http://www.w3.org/2003/05/soap-envelope"><ns3:Body><ns2:response><newSessionResult ifmap-publisher-id="test-2100079558-1" session-id="1323996407-1025975286-283779864-1097320563"/></ns2:response></ns3:Body></ns3:Envelope>').get_publisher_id()
test-2100079558-1
>>> print Metadata('role', 'employee')
<metadata><meta:role >employee</meta:role></metadata>
>>> print Metadata('role', 'employee', {'pot':'black', 'kettle':'black'})
<metadata><meta:role pot="black" kettle="black" >employee</meta:role></metadata>
>>> print Metadata('role', 'employee', {'pot':'black', 'kettle':'black'}, 'meta')
<metadata><meta:role pot="black" kettle="black" >employee</meta:role></metadata>
>>> print Metadata('role', 'employee', {'pot':'black', 'kettle':'black'}, 'meta', 'http://meta.com/')
<metadata><meta:role xmlns:meta="http://meta.com/" pot="black" kettle="black" >employee</meta:role></metadata>
>>> print SearchRequest('12345', str(IPAddress('10.0.0.1')))
<ifmap:search session-id="12345" ><ip-address value="10.0.0.1" /></ifmap:search>
>>> print SearchRequest('12345', str(IPAddress('10.0.0.1')), validation="None")
<ifmap:search session-id="12345" validation="None" ><ip-address value="10.0.0.1" /></ifmap:search>
>>> print SearchRequest('12345', str(IPAddress('10.0.0.1')), validation='None', search_parameters={'max_depth':'3', 'max_size':'10000'})
<ifmap:search session-id="12345" validation="None" max_depth="3" max_size="10000" ><ip-address value="10.0.0.1" /></ifmap:search>
>>> print SubscribeUpdateOperation('subscription-1',str(IPAddress("10.0.0.1")))
<update name="subscription-1" ><ip-address value="10.0.0.1" /></update>
>>> print SubscribeDeleteOperation('subscription-1')
<delete name="subscription-1" />
>>> print SubscribeRequest('12345', operations=str(SubscribeUpdateOperation('subscription-1',str(IPAddress("10.0.0.1")))))
<ifmap:subscribe session-id="12345" ><update name="subscription-1" ><ip-address value="10.0.0.1" /></update></ifmap:subscribe>
>>> print PurgeRequest('12345','publisher-12345')
<ifmap:purgePublisher session-id="12345" ifmap-publisher-id="publisher-12345" />
>>> print PollRequest('12345')
<ifmap:poll session-id="12345" />
>>>
"""

import logging

# create logger
logger = logging.getLogger('ifmap.client')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)

from xml.etree import ElementTree

from ifmap.client import client, namespaces
from ifmap.request import NewSessionRequest, RenewSessionRequest, EndSessionRequest, PublishRequest, SearchRequest, SubscribeRequest, PurgeRequest, PollRequest
from ifmap.id import IPAddress, MACAddress, Device, AccessRequest, Identity, CustomIdentity
from ifmap.operations import PublishUpdateOperation, PublishNotifyOperation, PublishDeleteOperation, SubscribeUpdateOperation, SubscribeDeleteOperation
from ifmap.util import attr, link_ids
from ifmap.response import Response, newSessionResult
from ifmap.metadata import Metadata

def client_test():
    print 'testing ifmap client (this requires a running server)'
    mapclient = client("https://127.0.0.1:8443", 'test', 'test', namespaces)

    result = mapclient.call('newSession', NewSessionRequest())
    mapclient.set_session_id(newSessionResult(result).get_session_id())
    mapclient.set_publisher_id(newSessionResult(result).get_publisher_id())

    meta = str(Metadata('role', 'employee', {'ifmap-cardinality':'multiValue'}))
    pubreq = PublishRequest(mapclient.get_session_id(), str(PublishUpdateOperation(id1=str(IPAddress("10.0.0.1")), metadata=meta, lifetime='forever')))
    result = mapclient.call('publish', pubreq)

    searchreq = SearchRequest(mapclient.get_session_id(), str(IPAddress("10.0.0.1")), validation="None")
    result = mapclient.call('search', searchreq)

    subreq = SubscribeRequest(mapclient.get_session_id(), operations=str(SubscribeUpdateOperation('subscription-1',str(IPAddress("10.0.0.1")))))
    result = mapclient.call('subscribe', subreq)

    pollreq = PollRequest(mapclient.get_session_id())
    result = mapclient.call('poll', pollreq)

    subreq = SubscribeRequest(mapclient.get_session_id(), operations=str(SubscribeDeleteOperation('subscription-1')))
    result = mapclient.call('subscribe', subreq)

    purgereq = PurgeRequest(mapclient.get_session_id(), mapclient.get_publisher_id())
    result = mapclient.call('purge', purgereq)

    endreq = EndSessionRequest(mapclient.get_session_id())
    result = mapclient.call('endSession', endreq)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    client_test()
