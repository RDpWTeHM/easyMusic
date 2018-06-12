#! /usr/bin/python3

#
# file name: spiderutils.py
# author   : Joseph Lin
# E-mail   : joseph.lin@aliyun.com
#
#

###
### import packages:
### 
import os
import sys

import requests

###
### Functions define:
###
def getHTMLText( URL, Params=None, Timeout=30):
	try:
		r = requests.get( URL, params=Params, timeout=Timeout )
		r.raise_for_status()
		r.encoding = r.apparent_encoding

		return r.text
	except:
		return None

###
###
###

if __name__ == "__main__":
	htmlData = getHTMLText("http://www.baidu.com")
	if htmlData == None:
		sys.exit(1)
	print (htmlData)
#fi just test.