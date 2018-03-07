import urllib2

request = urllib2.Request('http://www.xxxx67674676474674674xxxxxx.com')
try:
    urllib2.urlopen(request)
except urllib2.URLError, e:
    print e.reason
