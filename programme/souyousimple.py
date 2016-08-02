# -*- coding:utf-8 -*-
import urllib2
import re
import time

class Souyou(object):
    def __init__(self,url):
        self.url = url
        self.pic_list = []
        self.url_list = []
    def get_all_num(self):
        page = self.get_page(self.url)
        pattern = re.compile('<span class="num"><em></em>1 / (.*?)</span>')
        num  = re.findall(pattern,page)
        return int(num[0])
    def get_page(self,url):
        # request = urllib2.Request(url)
        # response = urllib2.urlopen(request)
        # return response.read()
        print url
        headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
        opener = urllib2.build_opener()
        opener.addheaders = [headers]
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request).read()
        except Exception,e:
            # print "Insert error:",e
            time.sleep(1)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request).read()
        time.sleep(0.1)
        return response
    def get_pic(self,url):
        page = self.get_page(url)
        pattern = re.compile('<img id="bigImg" src="(.*?)"',re.S)
        result = re.findall(pattern,page)
        if result:
            self.pic_list.append(result[0])
    def get_all_url(self):
        num = self.get_all_num()
        for num1 in range(1,num+1):
            url = self.url.replace(".html","_"+str(num1)+".html")
            self.url_list.append(url)
    def get_all_pic(self):
        self.get_all_url()
        for url in self.url_list:
            self.get_pic(url)
    def down_pic(self):
        import urllib
        import time
        import os
        self.get_all_pic()
        picpath = 'D:\\meinvs1'
        if not os.path.exists(picpath):
            print "chuangj"
            os.makedirs(picpath)

        print self.pic_list
        for pic_url in self.pic_list:
            target = picpath+"\\%s.jpg" % str(pic_url[-10:-4])
            print target

            download_img = urllib.urlretrieve(pic_url,target)#将图片下载到指定路径中
            time.sleep(0.1)
# url ="http://www.souutu.com/mnmm/xgmm/"

# url_list=[]
# def get_all_urls(url):
#
#     headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
#     opener = urllib2.build_opener()
#     opener.addheaders = [headers]
#     try:
#         request = urllib2.Request(url)
#         response = urllib2.urlopen(request).read()
#     except Exception,e:
#         # print "Insert error:",e
#         #             time.sleep(1)
#         request = urllib2.Request(url)
#         response = urllib2.urlopen(request).read()
#     time.sleep(0.5)
#     pattern = re.compile('<div class="timg">.*?<a href="(.*?)"',re.S)
#     result = re.findall(pattern,response)
#     return result
#
# urls = get_all_urls(url)
# for url in urls:
#     Sou = Souyou(url)
#     Sou.down_pic()
url = raw_input("url: ")
Sou = Souyou(url)
Sou.down_pic()







