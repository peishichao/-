# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 09:12:39 2017

@author: steven
"""
import urllib.request

class HtmlDownloader(object):
    
    def download(self,url):
        if url is None:
            return None
        
        response = urllib.request.urlopen(url)
        if response.getcode()!=200:
            return None
        return response.read()
            