#-*- coding:utf-8 -*-
import urllib
import urllib2
import re
import os
import time

class Spider():
	"""docstring for Spider"""
	def __init__(self,url,path):
		self.url = url
		self.path = path

	# 获取所有包含aiss的页面
	def getAllPage(self):
		url = self.url
		allPageList = []
		for i in range(1,12):
			allPageList.append("%slist_83_%d.html"%(url,i))#每页的地址 只有list_83_后面变化 共11页
		return allPageList
	#获取页面所有内容
	def getHtml(self,url):
		sleep_download_time = 3
		time.sleep(sleep_download_time)
		request = urllib2.Request(url)
		html = urllib2.urlopen(request).read()
		return html

	#获取模特名称
	def getName(self,url):
		html = self.getHtml(url)
		namere = ur'SPAN id=txtTitle>(.*?)</SPAN>'
		namelist = re.findall(namere,html)
		namere1 = ur'AISS|\[|\]'
		name = re.compile(namere1).sub(' ',namelist[0])
		return name
	#获取每页中的模特列表
	def getModels(self,url):
		html = self.getHtml(url)
		modelsUrlre = ur'<p><a href="(.*?.html)"'
		modelsUrlList1 = re.findall(modelsUrlre,html)
		modelsUrlList = []
		for i in modelsUrlList1:
			modelsUrlList.append(url.split("/tag")[0]+i)
		return modelsUrlList
	#获取模特页面url
	def getUrl(self,url): #url 为模特专属第一页
		urlre = re.compile(r'<a>(.*?): </a></li>')
		html = self.getHtml(url)
		html = unicode(html,'gbk').encode("utf-8")
		# 获取总共多少页
		pageNum = int(re.findall(urlre,html)[0][3:-3])#共XX页:
		urltest = url.split('aiss/')[-1].split('.')[0]
		urllist = []
		for i in range(2,pageNum):
			urltest = url.split('.html')[0]+'_'+str(i)+'.html'
			urllist.append(urltest)
		urllist.append(url)
		return urllist
	#获取模特图片url
	def getimgurl(self,url):
		html = self.getHtml(url)
		#三种图片url 正则
		imgurlre1 = 'src="(http.*?.jpg)"'
		imgurlre2 = "img src='(http.*?)' border"
		imgurlre3 = "src='(http.*?.jpg)'" 		
		#不需要匹配的图片url
		notimgurl = ['http://image.51xiqu.com/xiee/2105132w4-0.jpg','http://image.51xiqu.com/xiee/222s01412-0.jpg','http://image.51xiqu.com/xiee/2021163601-0.jpg','http://image.51xiqu.com/xiee/2035231561-0.jpg','http://image.5442.com/2015/0602/02/5442.jpg!220.jpg','http://image.5442.com/2015/0319/12/5442.jpg!220.jpg','http://image.5442.com/2015/0708/03/5442.jpg!220.jpg','http://www.77tuba.com/upimgs/litimg/151222/16202116029.jpg']
		#剔除不需要匹配的图片
		def nott(a):
			return a not in notimgurl
		imglist = filter(nott,re.findall(imgurlre1,html))	
		#当imgurllist 剔除不需要匹配的图片后 为空，则更换 正则
		if not imglist:
			imglist = filter(nott,re.findall(imgurlre2,html))
			if not imglist:
				imglist = filter(nott,re.findall(imgurlre2,html))
		return imglist
	#保存图片
	def saveImg(self,folder_path,url):
		imgName = folder_path+url.split('/')[-1]
		urllib.urlretrieve(url,imgName)
	#为每个模特创建文件夹
	def mkdir(self,filename):
		folder_path = path + filename +"/"  
		if not os.path.exists(folder_path):  
			os.makedirs(folder_path) 
		return 	folder_path

url = "http://www.dazui88.com/tag/aiss/"
path = 'F:/img/'
Spider = Spider(url,path)
#获取所有的aiss
allpage = Spider.getAllPage()
modelsNum = 0
#print "总共有%d页,分别为：%s\n"%(len(allpage),allpage)
for i in allpage:
	models = Spider.getModels(i)#获取每页的模特
	#print "%s页模特的数量为：%d\n"%(i,len(models))
	for j in models:
		modelsNum = modelsNum+1
		modelsName = Spider.getName(j)
		folder_path = Spider.mkdir(modelsName)
		url = Spider.getUrl(j)#获取单个模特的所有页
		imgnum = 0
		for k in url:
			imglist = Spider.getimgurl(k)#获取模特的每页的图片URL
			for m in imglist:
				imgnum = imgnum +1
				Spider.saveImg(folder_path,m)#保存图片
		#print "%s 共有照片%d张\n"%(modelsName,imgnum)