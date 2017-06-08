#-*-coding:utf-8-*-
import time
import urllib2
from bs4 import BeautifulSoup
file=open('meituancde.txt','w')
def get_url(i):
    url='https://www.lagou.com/zhaopin/ceshi/%s/?filterOption=%s'%(i,i)
    return url
def get_html(i):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }
    response=urllib2.Request(url=get_url(i),headers=headers)
    html=urllib2.urlopen(response).read().decode('UTF-8')
    soup=BeautifulSoup(html,"html.parser")
    return soup
def parse(i):
    soup=get_html(i)
    me=soup.findAll('',{'class':'money'}) #工资
    me1=soup.findAll('',{'class':'format-time'})#发布时间
    me2=soup.findAll('',{'class':'li_b_r'})#福利
    me3=soup.findAll('',{'data-lg-tj-id':'8F00'})#公司名字
    meitu={}
    i=0
    for title in me:
        meitu['salary'] =me[i].text
        for jianjie in me1:
            meitu['releaseTime']=me1[i].text
            for sellum in me2:
                meitu['welfare']=me2[i].text
                for pire in me3:
                    meitu['companyName']=me3[i].text

        i+=1
        res= repr(meitu).decode("unicode-escape")
        print res
        if len(meitu) !=0:
            file.write(res.encode("utf-8"))
            file.close()
if __name__ == '__main__':
    for i in range(1,31):
        parse(i)