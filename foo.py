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
    mapclient = client("https://localhost:8096", 'mapclient', 'mapclient', namespaces)

    result = mapclient.call('newSession', NewSessionRequest())
    mapclient.set_session_id(newSessionResult(result).get_session_id())
    mapclient.set_publisher_id(newSessionResult(result).get_publisher_id())

    meta = str(Metadata('role', '', {'ifmap-cardinality':'multiValue'}, elements='<name>employee</name>'))
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
