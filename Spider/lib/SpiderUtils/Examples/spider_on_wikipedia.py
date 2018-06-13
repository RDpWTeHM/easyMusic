#!/usr/bin/python3


"""
# file name: crawler_baiduBaiKe.py
# Author   : Joseph Lin
# 
### 
### ------ 2018/Jun/13 14:23  ------
### v0.0.1  
### change log: N/A
###
### ------
###
"""


###
### import packages
###
import spiderutils

import os
import sys

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
    
    #htmlData = spiderutils.getHTMLText("https://en.wikipedia.org/wiki/Crawler")
    htmlData = spiderutils.getHTMLText("https://en.wikipedia.org/wiki/Spider")

    print(htmlData)
#fed.

if __name__ == "__main__":
    main()
#fi.


