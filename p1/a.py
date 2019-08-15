#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests

def getHTML(url):
    
    data = requests.get(url)
    
    data.encoding = data.apparent_encoding
    
    return data.text

if __name__ == "__main__" :
    
    url = 'http://www.bluecore.com.cn/'
    
    html = getHTML(url)
    
    with open('bluecore.html','a',encoding="utf-8") as f:
        
        f.write(html)