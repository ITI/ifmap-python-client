from ifmap import ifmapClient, IPAddress, ifmapIDFactory, MACAddress, Device, AccessRequest, Identity


client = ifmapClient("https://127.0.0.1:8443", 'test', 'test')

client.connect()

client.publishtest()

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


"""
Test Results
<ip-address value="10.0.0.1" type="IPv4" administrative-domain="ifmaplab" />
<ip-address value="10.0.0.1" type="IPv4" />
<ip-address value="10.0.0.1" />
<ip-address value="3ffe:1900:4545:3:200:f8ff:fe21:67cf" type="IPv6" administrative-domain="ifmaplab" />
<ip-address value="3ffe:1900:4545:3:200:f8ff:fe21:67cf" type="IPv6" />
<ip-address value="3ffe:1900:4545:3:200:f8ff:fe21:67cf" />
<mac-address value="aa:bb:cc:dd:ee:ff" administrative-domain="ifmaplab" />
<mac-address value="aa:bb:cc:dd:ee:ff" />
<device><name>123:45</name></device>
<device><name>123:45</name><aik-name>aikdummynamef34feccc28b3d44f<aik-name></device>
<access-request name="111:23" administrative-domain="ifmaplab" />
<access-request name="111:23" />
<identity name="john.doe" />
<identity name="john.doe@example.com" type="email_address" />
<identity name="ef9b13e5df7dae502c51db7ca4624552" type="other" other-type="RFID" />
<identity name="ef9b13e5df7dae502c51db7ca4624552" type="other" other-type="RFID" administrative-domain="ifmaplab" />
"""
