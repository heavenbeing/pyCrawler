#!/usr/bin/python  
#-*-coding:utf-8-*-
import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/'+str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pat = r'<div.*?content">.*?<span.*?>(.*?)</span>.*?</div>.*?'
    pattern = re.compile(pat,re.S)
    items = re.findall(pattern, content)
    print '你好'
    for item in items:
        # print item
        if '<br/>' in item:
            item = item.replace('<br/>', '')  # 过滤该标签
            item = item.replace('\n', ' ')  # 换行空格替代 否则总换行
        print item
        print "*****************************"
    print response.read()
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason


