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
        
    
