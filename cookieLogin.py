import urllib
import urllib2
import cookielib

filename = 'cookie.txt'

cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({"email":"localhost_port80@163.com","password":"12345678abc","from":"web"})

loginUrl = 'https://web.learning-genie.com/#/login'

result = opener.open(loginUrl,postdata)

cookie.save(ignore_discard=True,ignore_expires=True)

gradeUrl = 'https://web.learning-genie.com/#/centers/273F752A-C71A-E811-B096-068A0B6E51E2/groups'

result = opener.open(gradeUrl)

print result.read()

