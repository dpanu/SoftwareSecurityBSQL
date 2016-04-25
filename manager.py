#!/usr/bin/python
import urllib2
from urllib2 import Request
from urlparse import urlparse
import sys


def main(argv, req=None):
    url = argv[1]
    #parsing the url
    parse = urlparse(url)
    #checking for ?id= form
    if parse.query is None:
        print 'cannot be exploited'
        sys.exit(0)
    #recording original response
    req = Request(url)
    orig_res = urllib2.urlopen(req).read()
    #print res.read()
    url = checkAND(url)
    success = False

    while(not success):
        success = False


def checkAND(url):

    return url



def manipulate(url):
    return url


if __name__ == '__main__':
    main(sys.argv)