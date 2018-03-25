# -*- coding:utf-8 -*-
import requests
if __name__ == '__main__':
    target = 'http://www.isunon.com'
    req = requests.get(url=target)
    print(req.text)
