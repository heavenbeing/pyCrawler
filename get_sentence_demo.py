# -*- coding: utf-8 -*-
import io
import json
import urllib, urllib2, sys
import re
from multiprocessing import Pool

import requests
from requests.exceptions import RequestException

import io
# https://v1.hitokoto.cn/?encode=json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# host = 'https://v1.hitokoto.cn/?encode=json'
# method = 'GET'
# bodys = {}
# url = host
#
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# content = response.read()
# if (content):
#     print(content)

num = 0


def write_to_file(content):
    with io.open('result_sententes.txt', 'a', encoding='utf-8') as f:
        # f.write(u'{}\n'.format(content))
        f.write(u',\n'+content)
        f.close()
        #
        # with open(filename, 'w', encoding='utf-8') as f:
        #     f.write(u'{}\n'.format(index))


def main(offset):
    host = 'https://v1.hitokoto.cn/?encode=json'
    method = 'GET'
    bodys = {}
    url = host

    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    content = response.read()

    if (content & num<=10000):
        num+1
        print(content)
        # print(item)
        write_to_file(content)


if __name__ == '__main__':
    p = Pool()
    p.map(main, [i*10 for i in range(5)])