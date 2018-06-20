#!/usr/bin/python3

"""
# file name: kv_baidu_search.py
# Author   : Joseph Lin
# 
### 
### ------ 2018/Jun/13 15:21  ------
### v0.0.1  
### change log: N/A
###
### ------ 2018/Jun/15 11:01  ------
### v0.0.4
### author    : Joseph Lin
### change log: 添加处理 JSON format of playlist data.
###
### ------
###
"""


###
### import packages
###
import sys
import os

import spiderutils

import requests

from bs4 import BeautifulSoup

import json


###
### Global variables
###
doDebug = False

browsersKV = {'User-Agent':'Mozilla/5.0  (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
g_urlKV    = {'id':''}

g_payload  = {'params':''}

"""
	注意， .com/#/... 实际上不是这个样子的链接请求！
	这个是浏览器运行 js 后，显示出来的样子。
"""
g_url_common = "https://music.163.com/#/user/home"

###
### function define
###
def foo():
	pass


## tmp:
def getHTMLText( URL, Params=None, Head=None, Timeout=30):
	try:
		r = requests.get( URL, params=Params, headers=Head, timeout=Timeout )
		r.raise_for_status()
		r.encoding = r.apparent_encoding

		return r.text
	except:
		return None


def getPlayList(userID):
	kv = {'id':userID}
	browsersKV = {'User-Agent':'Mozilla/5.0  (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
	htmlData = getHTMLText("https://music.163.com/#/user/home", Params=kv, Head=browsersKV)
	# print(htmlData)

	# htmlData = spiderutils.getHTMLText("https://music.163.com/user/home", Params=kv)
	htmlData = getHTMLText("https://music.163.com/user/home", Params=kv, Head=browsersKV)
	# print(htmlData)

	# htmlData = getHTMLText("https://music.163.com/weapi/user/playlist", Params={'csrf_token':''}, Head=browsersKV)
	payload = {'params':'Ce+PkA3nHWdJq0x6wzZwNq7N9Q91WSx6icLDTkRJAUmNikCHR5pJrBkYbnKTXuKS92hLwYpCrktCPU5r6n44Pt27rjhxrWh59Ha6yb/k5IJpA/6QMGl5xCav7fxoG4Fe0WE8Twc032sTSJ8Z5cHncdhlliY9HeCXTQYHsY6nseuDeAX0cmJSo4YTvQLkes3P', 'encSecKey':'77b55cefb01176d56068956432bb07969e81b611fc680e4b95bb1490783240d4a0659f2a17d5be44de4e20dedbd540d30d203913fabde2779e344dd0aaaab2ddc6b82436df54731c0efe22770c4f5b04c0c676b2bce08e195834733864892f4a4d18645a1b9b44878cf8c11b01c618fb178717372ff62ff2634dd80e7a2287e7' }
	try:
		r = requests.post("https://music.163.com/weapi/user/playlist", params={'csrf_token':''}, headers=browsersKV, data=payload )
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		htmlData = r.text
	except:
		htmlData = None
		sys.exit(1)
	# print(htmlData)
	### 分析歌单 URL， 用于下面get playlist的 id！
#fed


###
#### language of song's name. 
def Is_chinese(uchar):
	""" 判断一个unicode 是否是汉字"""
	if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
		return True
	else:
		return False

def myAlign(string, length=0):
	if length==0:
		return string

	slen = len(string)
	CN_counter = 0
	for u in string:
		if Is_chinese(u):
			CN_counter += 2
		else:
			CN_counter += 1
	slen = CN_counter

	re = string
	if isinstance(string, str):
		placeholder = ' '
	else:
		placeholder = u' '

	while slen<length:
		re += placeholder
		slen += 1
	return re


def PringSongList_format(songList):
	songPrtLaterList = list()
	i=0
	tplt = "{0:^16}"
	for song in songList:
		CN_counter = 0
		for u in song:
			if Is_chinese(u):
				CN_counter += 2
			else:
				CN_counter += 1
		slen = CN_counter
		# if len(song)>16:
		if slen>18:
			songPrtLaterList.append(song)
			continue

		if i%4==0:
			print("")
		# print('{0:{1}<10}'.format(song,chr(12288)),  end="")
		#print(song.ljust(15," "),  end="")
		print( myAlign(song, 20), end="" )
		i=1+i
	print("")

	songList_v2 = list()
	for song in songPrtLaterList:
		CN_counter = 0
		for u in song:
			if Is_chinese(u):
				CN_counter += 2
			else:
				CN_counter += 1
		slen = CN_counter
		# if len(song)>16:
		if slen>37:
			songList_v2.append(song)
			continue

		if i%2==0:
			print("")
		# print('{0:{1}<10}'.format(song,chr(12288)),  end="")
		#print(song.ljust(15," "),  end="")
		print( myAlign(song, 40), end="" )
		i=1+i
	print("")

	for song in songList_v2:
		print(song)
	print("%s\n" %(80*'='))


USER_ID_doDebug = True
def USERIDDBG(_str):
	print(_str)
class USER_ID:
	"""docstring for USER_ID"""
	def __init__(self, ID=0):
		# super(USER, self).__init__() ## ????
		self.ID = ID

		self.userFrameUrl = "https://music.163.com/user/home" 
		self.userFrameUrlKV = None
		self.userFrameHTMLData = None

		self.songListUrl = "https://music.163.com/playlist"
		self.songListUrlKV_DIC = None
		self.songListUrlPayload_DIC = None
	
	def getUserID():
		return self.ID

	def setUserID(ID):
		self.ID = ID
		if USER_ID_doDebug:
			USERIDDBG("USER ID: "+str(ID))

	def printClassAll(self):
		print("\n======  class variables trace:  ============= ")
		print(self.ID)

		print(self.userFrameUrl)
		print(self.userFrameUrlKV)
		#print(self.userFrameHTMLData)
		
		print(self.songListUrl)
		print(self.songListUrlKV_DIC)
		print(self.songListUrlPayload_DIC)
		print("%s" %(30*'='))

	def private_generateUserFrameHTMLurl(self):
		self.userFrameUrlKV = {'id':self.ID}
	def getUserFrameHTMLurlKV(self):
		self.private_generateUserFrameHTMLurl()
		return self.userFrameUrlKV

	def getUserFrameHTMLData(self):
		self.userFrameHTMLData = getHTMLText(self.userFrameUrl, 
											Params=self.getUserFrameHTMLurlKV(), 
											Head=browsersKV)
		return self.userFrameHTMLData

	"""
		.com/#/...                             
		通用首页HTML代码 ----GET---->        用户首页      --POST-->      用户playList 数据（JSON）
		             .com/home?id=<USER-ID>           .com/playlist?...          
												       + formdata
	"""
	def private_GeneratePlayListKVSET(self):
		"""
			大概是生成 HASH 去对应 USER 的 iframe 请求
			POST + formdata => 获得 JOSN 格式的数据！
			-[o] 找到 JavaScript 解析 JOSN 数据的位置
		"""
		pass

	def getPlayListJSON(self):
		"""
			通过POST 方法获取到 response 过来的 JSON 数据
		"""
		try:
			with open('PlayList.json') as f_PlayListJSON:
				playListJSON = f_PlayListJSON.read()
		except IOError as e:
			print("IO ERROR: " + str(e))
			sys.exit(215)
		
		return playListJSON

	def getPlayListUrlKVSet(self):
		"""
			通过 JSON 数据分析出来 即将请求 songList 的 ParamsKV
			https://music.163.com/playlist?id=13630786
			{'id':'13630786', 'id':'588662883'}
		"""
		playListJSON = self.getPlayListJSON()
		if USER_ID_doDebug:
			if playListJSON.find("小白兔"):
				USERIDDBG("\n@@@@@  GET JSON data success! @@@@@")
			else:
				USERIDDBG("\n------Get JSON data Faile!----")

		## 使用 JSON 库将其转化为 dict 
		playListJSON = json.loads(playListJSON)
		## type(playListJSON) == dict
		tmp_playList = playListJSON['playlist']
		## type(tmp_playList) == LIST
		## type(tmp_playList[X]) == dict

		tmp_DIC = dict()
		for eachPlayList in tmp_playList:
			tmp_DIC[eachPlayList['name']] = eachPlayList['id']

		if USERIDDBG:
			USERIDDBG(tmp_DIC)
		##########
		self.songListUrlKV_DIC = tmp_DIC
		
		#### -[o]joseph, delete fallow later:
		if USER_ID_doDebug:
			print(type(self.songListUrlKV_DIC))
			print(str(len(self.songListUrlKV_DIC)))
			print("")
			for i in range(len(self.songListUrlKV_DIC)):
				print("{:<4d}{}:{}".format(i,list(self.songListUrlKV_DIC.keys())[i],list(self.songListUrlKV_DIC.values())[i]))

		return self.songListUrlKV_DIC

	def getSongList(self, selectPlayList):
		if selectPlayList in self.songListUrlKV_DIC:
			pass
		else:
			return None

		IDofSongList = self.songListUrlKV_DIC[selectPlayList]
		if USER_ID_doDebug:
			USERIDDBG(IDofSongList)

		requestKV = {'id':IDofSongList}
		html_songListData = getHTMLText(self.songListUrl, Params=requestKV, Head=browsersKV)
		
		bshtml = BeautifulSoup(html_songListData, "html.parser")
		bsSongtb = bshtml.findAll("ul", {"class":"f-hide"})
		## bsSongtb is "SET" type of bs4

		bsSongList = bsSongtb[0]
		## bsSongList is "LIST" type of bs4

		songList = list()
		for song in bsSongList.findAll("li"):
			songList.append( song.get_text() )

		return songList


###
### running logical
###
def main():
	argc = len(sys.argv)
	ID = 0
	if argc !=2:
		ID = input("Enter your USER ID of Music.163.com: ") 
	else:
		ID = sys.argv[1]

	user = USER_ID(ID)
	user.printClassAll()

	## fake request
	# getHTMLText(g_url_common, Params=user.userFrameUrlKV, Head=browsersKV)
	## real request
	htmlData = user.getUserFrameHTMLData()
	
	#print(htmlData)
	# print(htmlData[(htmlData.find(u"喜欢的音乐")-20):(htmlData.find(u"纯音乐")+200)])

	user.getPlayListUrlKVSet()
	user.printClassAll()

	while(True):
		selectPlayList = input("Enter play list name which you want to get song list: ")
		if selectPlayList=='q':
			sys.exit(0)
		if selectPlayList in user.songListUrlKV_DIC:
			"""
				在 code 里面的写的 “中文” 和 在终端输入的“中文”， 
				是可以直接相等比较的！
			"""
			print('[Debug:] right value!')
		else:
			print('[Debug:] wrong value!')
			selectPlayList = input("Try again: ")
			continue
		
		# print(user.getSongList(selectPlayList))
		songList = user.getSongList(selectPlayList)
		PringSongList_format(songList)



def old_main():
	argc = len(sys.argv)
	if argc!=2:
		print( "usage: $ %s <your userID>" %sys.argv[0], file=sys.stderr)
		print( "like: $ %s 39692581" %sys.argv[0], file=sys.stderr)
		print( "[Debug:] this ID not work in this case for now.")
		sys.exit(1)

	# getPlayList(sys.argv[1])
	while True:
		songListID = input("Enter your song List id(which can be found on url)(Enter q to quit): ")
		if songListID=='q':
			sys.exit(0)
		# print(songListID)
		songlistKV={'id':songListID}
		html_songListData = getHTMLText("https://music.163.com/playlist", Params=songlistKV, Head=browsersKV)
		# print(htmlData[10000:16000])

		bshtml = BeautifulSoup(html_songListData, "html.parser")
		bsSongtb = bshtml.findAll("ul", {"class":"f-hide"})
		## bsSongtb is "SET" type of bs4

		bsSongList = bsSongtb[0]
		## bsSongList is "LIST" type of bs4

		songList = list()
		for song in bsSongList.findAll("li"):
			songList.append( song.get_text() )

		songPrtLaterList = list()
		i=0
		tplt = "{0:^16}"
		for song in songList:
			CN_counter = 0
			for u in song:
				if Is_chinese(u):
					CN_counter += 2
				else:
					CN_counter += 1
			slen = CN_counter
			# if len(song)>16:
			if slen>18:
				songPrtLaterList.append(song)
				continue

			if i%4==0:
				print("")
			# print('{0:{1}<10}'.format(song,chr(12288)),  end="")
			#print(song.ljust(15," "),  end="")
			print( myAlign(song, 20), end="" )
			i=1+i
		print("")

		songList_v2 = list()
		for song in songPrtLaterList:
			CN_counter = 0
			for u in song:
				if Is_chinese(u):
					CN_counter += 2
				else:
					CN_counter += 1
			slen = CN_counter
			# if len(song)>16:
			if slen>37:
				songList_v2.append(song)
				continue

			if i%2==0:
				print("")
			# print('{0:{1}<10}'.format(song,chr(12288)),  end="")
			#print(song.ljust(15," "),  end="")
			print( myAlign(song, 40), end="" )
			i=1+i
		print("")

		for song in songList_v2:
			print(song)
		print("%s\n" %(80*'='))
#fed.


if __name__ == "__main__":
	main()
#fi.

