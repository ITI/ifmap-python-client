from ifmap.client import client, namespaces
from ifmap.request import NewSessionRequest
from ifmap.id import IPAddress, MACAddress, Device, AccessRequest, Identity, CustomIdentity


import logging

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


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


	#
	#def test_connect(self):
	#
	#	newSessionRequest = '<ifmap:newSession />'
	#	response = self.call('newSession', newSessionRequest)
	#	self.__session = {'sessionid': response.newSessionResult['session-id'],
	#		'publisher_id': response.newSessionResult['ifmap-publisher-id'],
	#	}
	#
	#def test_publish(self):
	#	username = 'jdoe'
	#	role = 'employee'
	#	publish_req = publish_blob % {'sessionid': self.session['sessionid'],'username':username,'role':role, }
	#	response = self.call('publish', publish_req)
	#	return response



print IPAddress("10.0.0.1","IPv4","ifmaplab")
print IPAddress("10.0.0.1","IPv4",)
print IPAddress("10.0.0.1",)
print IPAddress("3ffe:1900:4545:3:200:f8ff:fe21:67cf","IPv6","ifmaplab")
print IPAddress("3ffe:1900:4545:3:200:f8ff:fe21:67cf","IPv6",)
print IPAddress("3ffe:1900:4545:3:200:f8ff:fe21:67cf",)
print MACAddress("aa:bb:cc:dd:ee:ff","ifmaplab",)
print MACAddress("aa:bb:cc:dd:ee:ff",)
print Device("123:45")
print Device("123:45","aikdummynamef34feccc28b3d44f")
print AccessRequest("111:23","ifmaplab",)
print AccessRequest("111:23",)
print Identity("john.doe")
print Identity("john.doe@example.com", type="email_address")
print Identity("ef9b13e5df7dae502c51db7ca4624552", type="other", other_type="RFID")
print Identity("ef9b13e5df7dae502c51db7ca4624552", type="other", other_type="RFID", administrative_domain="ifmaplab")
print CustomIdentity("student-id")
print CustomIdentity("student-id", "nsu")
print CustomIdentity("student-id", "nsu", "http://nsu.example.org/student")
print CustomIdentity("student-id", namespace="http://nsu.example.org/student")
print CustomIdentity("student-id", attributes={'ID':"1864b64efe4903d7f45b4cdbdad38ab7d828e499", 'serial':"S1223505",})
print CustomIdentity("student-id", "nsu", "http://nsu.example.org/student", attributes={'ID':"1864b64efe4903d7f45b4cdbdad38ab7d828e499", 'serial':"S1223505",})

print NewSessionRequest('10000')
print NewSessionRequest()

mapclient = client("https://127.0.0.1:8443", 'test', 'test', namespaces)

method = 'newSession'
request = NewSessionRequest()
result = mapclient.call(method, request)

print '==== sent ===='
print mapclient.last_sent()

print '==== received ===='
print mapclient.last_received()

print 'test complete'


