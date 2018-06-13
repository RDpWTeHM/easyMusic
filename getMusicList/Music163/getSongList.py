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

###
### Global variables
###
doDebug = False

browsersKV = {'User-Agent':'Mozilla/5.0  (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}


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
### running logical
###
def main():
	argc = len(sys.argv)
	if argc!=2:
		print( "usage: $ %s <your userID>" %sys.argv[0], file=sys.stderr)
		print( "like: $ %s 39692581" %sys.argv[0], file=sys.stderr)
		print( "[Debug:] this ID not work in this case for now.")
		sys.exit(1)

	# getPlayList(sys.argv[1])

	songListID = input("Enter your song List id(which can be found on url): ")
	# print(songListID)
	songlistKV={'id':songListID}
	html_songListData = getHTMLText("https://music.163.com/playlist", Params=songlistKV, Head=browsersKV)
	# print(htmlData[10000:16000])

	bshtml = BeautifulSoup(html_songListData, "html.parser")
	bsSongtb = bshtml.findAll("ul", {"class":"f-hide"})
	## bsSongtb is "SET" type of bs4

	bsSongList = bsSongtb[0]
	## bsSongList is "LIST" type of bs4

	for song in bsSongList.findAll("li"):
		print(song.get_text())

#fed.

if __name__ == "__main__":
	main()
#fi.

