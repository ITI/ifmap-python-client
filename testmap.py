

from ifmap import ifmapClient


client = ifmapClient("https://127.0.0.1:8443", 'test', 'test')

client.connect()

client.publishtest()