# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from PIL import ImageEnhance,ImageFilter
from pytesser import *
from pytesseract import *
import time,os,uuid,urllib2,cookielib,urllib,io,StringIO

'''获取文件后缀名'''
def get_file_extension(file):
    return os.path.splitext(file)[1]
'''創建文件目录，并返回该目录'''
def mkdir(path):
    # 去除左右两边的空格
    path=path.strip()
    # 去除尾部 \符号
    path=path.rstrip("\\")

    if not os.path.exists(path):
        os.makedirs(path)

    return path
'''自动生成一个唯一的字符串，固定长度为36'''
def unique_str():
    return str(uuid.uuid1())
'''
抓取网页文件内容，保存到内存

@url 欲抓取文件 ，path+filename
'''
# def get_file(url):
#     try:
#         cj=cookielib.LWPCookieJar()
#         opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#         urllib2.install_opener(opener)
#         req=urllib2.Request(url)
#         operate=opener.open(req)
#         data=operate.read()
#         return data
#     except BaseException, e:
#         print e
#         return None
'''
保存文件到本地

# @path  本地路径
# @file_name 文件名
# @data 文件内容
# '''
# def save_file(path, file_name, data):
#     if data == None:
#         return
#
#     mkdir(path)
#     if(not path.endswith("/")):
#         path=path+"/"
#     file=open(path+file_name, "wb")
#     file.write(data)
#     file.flush()
#     file.close()
# 二值化
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

#由于都是数字
#对于识别成字母的 采用该表进行修正
rep={'O':'0',
    'I':'1','L':'1',
    'Z':'2',
    'S':'8'
    }

def  getverify1(name):

    # 打开图片
    im = Image.open(name)
    # 转化到亮度
    imgry = im.convert('L')
    imgry.save('g'+name)
    # 二值化
    out = imgry.point(table,'1')
    out.save('b'+name)
    # 识别
    text = image_to_string(out)
    print "text:" + text

    # 识别对吗
    text = text.strip()
    text = text.upper()

    for r in rep:
        text = text.replace(r,rep[r])

    out.save(text + ".gif")
    return text

#browser = webdriver.Firefox() # Get local session of chrome
# browser.maximize_window()
#browser.get("http://test.xiaoshushidai.com/xs.php") # Load page

#获取文件后缀名
print get_file_extension("1.gif")

#創建文件目录，并返回该目录
#print mkdir("E:/ljq")

#自动生成一个唯一的字符串，固定长度为36
print unique_str()
url = "http://139.196.241.89:55555/BoocaaCare/verify?0.9190148629752934"
save_file("./","1.gif", get_file(url))
vcode = getverify1('1.gif')
print(vcode)