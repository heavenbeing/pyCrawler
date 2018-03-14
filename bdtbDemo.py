#-*-coding:utf-8-*-
import urllib
import urllib2
import re

class BaiduTieba:

    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl, seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz'+str(seeLZ)

    # 传入页码，获取该页帖子
    def getPage(self,pageNum):
        try:
            url = self.baseURL+self.seeLZ+'&pn='+str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            print response.read()
            return response
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"connect to BaiduTieba Error:",e.reason
                return None

    # 获取帖子标题
    def getTitle(self):
        page = self.getPage(1)
        print page
        pattern = re.compile('<h1.*?class="core_title_txt.*?>(.*?)</h1>',re.S)
        result = re.compile(pattern, page)
        print result
        if result:
            print result.group(1)
            return result.group(1).strip()
        else:
            return None

baseURL = 'http://tieba.baidu.com/p/5089096303'
bdtb = BaiduTieba(baseURL,1)
# bdtb.getPage(1)
bdtb.getTitle()
