# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#这里的导入sys模块针对运行中出现ASICC码出现问题所调用。注意写的是什么，简单的三行。
class Tool:
    #处理字符串，注意思考这个存在的意思是什么？（w为了我门后面正则表达式时所获取的一大串，既包括我们所需要的，也有一些我们不需要的。）
    #第二，我们要采用高效的类来实现。这里的类的形式与之前的不同，在以后在写程序中，我们要会理解这样的类我们如何编写，如何与其他的一起调用。
    #第三，我们注意运用到了哪些函数，re中的compile与sub这2个，compile所起到的作用是什么（与之前的作用类似，都是所想要匹配的内容。）在之后的替换实现的是方法实现，
    #带参数的方法实现，这里连接了与其他类的运用。注意re.sub()三个参数是什么，怎么用。
    removes = re.compile('<strong>')
    removew =re.compile('</strong>')
    def replace(self,x):
        x = re.sub(self.removes,"",x)
        x = re.sub(self.removew,"",x)
        return x.strip()
#这里是主体部分：主体部分主要注意的是程序的一步一步的实现（每一步实现什么，下一步实现什么），之间的方法调用（如何在下一个方法中调用上一个刚写完的方法这种思想需要我们好好注意）。
#在初始化中，我们注意到了调用了其他类。（这里我们就要特别注意下，哪边有括号为什么。）
#分清层次，每一步干嘛：
class ALBB:
 
    #第一个初始化一般是构建我们的正确网址以及其他类的调用，还有一些参数，列表的设置。普通参数与self参数的确立要清楚点。
    def __init__(self,goods,i):
        baseURL='http://www.alibaba.com/products/'+goods+'/'+str(i)+'.html'
        self.baseURL = baseURL
        self.tool = Tool()
        self.success=False
    #获取html的 固定写法：三部曲要知道：   
    def getPage(self):
        try:
            url = self.baseURL
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read()
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接阿里巴巴失败,错误原因",e.reason
                return None
    #在这里回忆下标准的正则表达的运用。可能与之前的不大一样，但这最基本的地方必须要知道如何书写：还有就是findall后产生的结果是list.
    def getcontents(self):
        page=self.getPage()
        pattern = re.compile('<h2 class="title"><a href.*?>(.*?)</a>',re.S)
        result = re.findall(pattern,page)
        return result
    def keyword(self):
        key=raw_input(u"请输入搜索产品".encode('gbk'))
        return key
    def getnum(self):
        page=self.getPage()
        pattern = re.compile('<span class="disable">(.*?)</span>',re.S)
        num=re.findall(pattern,page)
        return num[0]
    def getall(self,key,a):
        page=self.getPage()
        all=self.getcontents()
        
        print u'正在搜索第 '+str(a)+u'页'
        
        for item in all:
            
            if self.tool.replace(item)==key:
                print u'成功找到，信息如下'
                print u'我们需要的产品在第',str(a),u'页',u'第',all.index(item)+1,u'列'
                self.success=True
        return
def keygoods():
    goods=raw_input(u"请输入商品名称".encode('gbk'))
    return goods    
def keyword():
        key=raw_input(u"请输入搜索产品".encode('gbk'))
        return key
goods=keygoods()       
key=keyword()
shi=ALBB(goods,1)
num=shi.getnum()
for i in range(1,int(num)):
    if shi.success==False:
        shi=ALBB(goods,i)
        shi.getall(key,i)
    else:
        break

