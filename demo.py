import urllib
import urllib2

values = {"userEmail": "local@qqq.com.bak", "userPassword": "12345678abc"}
data = urllib.urlencode(values)
url="http://localhost:63343/lg-web/src/measureAI/index.html?_ijt=fgb2esvreeht2sls23krtan3lm#/login"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()
