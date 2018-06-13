#!/usr/bin/python3

"""
# file name: kv_baidu_search.py
# Author   : Joseph Lin
# 
### 
### ------ 2018/Jun/13 15:08  ------
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
	
	kv = {'wd':'Spider'}
	#htmlData = spiderutils.getHTMLText("https://en.wikipedia.org/wiki/Crawler")
	htmlData = spiderutils.getHTMLText("http://www.baidu.com/s", Params=kv)

	print(htmlData)
#fed.

if __name__ == "__main__":
	main()
#fi.

