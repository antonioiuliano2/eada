#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urlparse
import httplib

def check_server(hostname):
    '''
    Check if a host (www.abc.com) is up
    '''
    conn = httplib.HTTPConnection(hostname)
    conn.request('HEAD','')
    s = conn.getresponse().status
    return int(s) < 400
    
def check_availability(service_url):
    '''
    Checks whether the given (service) url is reachable
    '''
    pr = urlparse.urlparse(service_url)
    
    serverUp = check_server(pr.netloc)
    
