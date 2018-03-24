# -*- coding: utf-8 -*-
import urllib, urllib2, sys
# appcode:66aebb644d3f4b729e12fa77644f4c85
# appKey: 24830681
# appSecret :add042d56f427fd7bbfe7d7b55fcacc0

host = 'http://jisutqybmf.market.alicloudapi.com'
path = '/weather/query'
method = 'GET'
appcode = '66aebb644d3f4b729e12fa77644f4c85'
querys = 'city=%E9%83%91%E5%B7%9E&citycode=citycode&cityid=cityid&ip=ip&location=location'
bodys = {}
url = host + path + '?' + querys

request = urllib2.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)
