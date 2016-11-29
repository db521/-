# coding=utf-8
import re

import requests

r = requests.get('http://www.dy2018.com/2/')
#指定当前网页的字符集
r.encoding='gb2312'
print r.encoding
text=r.text
#查找所有的标题,正则的写法是:分2段,第一段是:title=",第二段是:2016年日本6.5分喜剧片《英雄迷的生活》BD日语中字,这种的内容
#第三段是">,第三段只出现1次,所以是{1}
#下面2个正则同理
textre=r'(title=")+(.*)(">){1}'
#查找评分的
judgere=ur'(◎评分: )+(.*)(</font>){1}'
#查找这个URL地址的,还没成功,明天尝试
urlre=r'(href=")+(/i/)(\d){.html}{1}'
#findall是查找所有的结果的,返回的内容是一个list,需要遍历取出来
texttall=re.findall(textre,text)
judgeall=re.findall(judgere,text)
urlall=re.findall(urlre,text)
print urlall
#ZIP是把2个list直接拼接到一起的一个东西,很高大上
#比如:a='abc'   b='123'  zip(a,b)的结果就是:[(a, 1), (b, 2), (c, 3)]
# all=zip(texttall,judgeall)
# for x in all:
#     print x[1][0]+x[1][1]+'---'+x[0][1]

