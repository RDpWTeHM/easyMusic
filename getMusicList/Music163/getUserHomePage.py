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

###
### Global variables
###
doDebug = False


###
### function define
###
def foo():
	pass


###
### running logical
###
def main():
	argc = len(sys.argv)
	if argc!=2:
		print( "usage: $ %s <your userID>" %sys.argv[0], file=sys.stderr)
		print( "like: $ %s 39692581" %sys.argv[0], file=sys.stderr)
		sys.exit(1)

	kv = {'id':sys.argv[1]}
	htmlData = spiderutils.getHTMLText("https://music.163.com/#/user/home", Params=kv)

	print(htmlData)
#fed.

if __name__ == "__main__":
	main()
#fi.

