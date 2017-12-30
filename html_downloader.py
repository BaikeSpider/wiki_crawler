# coding:utf-8
from urllib import parse
from ipdb import set_trace 
import urllib.request

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        # set_trace()
        
        # headers = ('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
        req = urllib.request.build_opener()
        # req.addheader = [headers]
        response = req.open(url)
       
        if response.getcode() != 200:
               return None
        return response.read()

