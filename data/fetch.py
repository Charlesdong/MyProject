#!/usr/bin/python
# coding=utf-8
import time
import datetime

import requests
from bs4 import BeautifulSoup 


class SpiderBase(object):

    def __init__(self, url):
        self.url = url

    def spider_request_get(self, header=''):
        response = requests.get(self.url, headers=header)
        if response.content:
            print 'response.content.length: ', len(response.content), response.content
            if len(response.content) > 500 or len(response.content) < 300:
                return BeautifulSoup(response.content)
            else:
                print '请求过多，休息300秒！！！', datetime.datetime.now()
                time.sleep(300)
                return self.spider_request_get(header)

    def spider_request_post(self, data, header=''):
        response = requests.post(self.url, data=data, headers=header)
        if response.content:
            return BeautifulSoup(response.content)


class OschinaFetch(SpiderBase):

    def __init__(self, url=''):
        super(OschinaFetch, self).__init__(url)

    def generate_html(self):
        soup = self.spider_request_get()
        href_list = [(i.find('a').attrs['href'], i.find('a').attrs['title']) for i in soup.select('li.today')]
        with open('./news.html', 'w') as f:
            for h in href_list:
                href = h[0]
                if 'oschina.net' not in href:
                    href = 'http://www.oschina.net' + href
                html = u"<a href=%s title=%s>%s</a><br>" % (href, h[1], h[1])
                f.write(html.encode(encoding='utf-8'))


if __name__ == '__main__':
    fetch = OschinaFetch(url='http://www.oschina.net/')
    fetch.generate_html()
