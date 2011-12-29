#!/usr/bin/python
#
# Copyright 2011, Infoblox, All Rights Reserved
#
# Open Source, see LICENSE
#

def attr(attributes):
    """
    attr creates an XML string for any attribute that has a value
    attr({'session-id': '2345', 'validation':'metadata'})
    """
    if attributes and (type(attributes) == type({})): # check if it is a dictionary
        __xml = ""
        for label, value in attributes.items():
            if value:
                __xml += label + '="' + value + '" '
        return __xml
    else:
        return ''

def link_ids(id1, id2):
    """
    Takes two id arguments.
    Returns XML for id1 or links id1 and id2 together
    """
    if id1 and id2: # Both exist, so link them
        return '<link>' +  id1 + id2 + '</link>'
    else:
        return id1
    

    