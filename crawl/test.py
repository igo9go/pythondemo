import urllib2, cookielib


request = urllib2.urlopen('http://www.baidu.com')

print request.read()

import bs4
print bs4