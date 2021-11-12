#!/usr/bin/python3
#-*-coding:utf-8 -*-
import rich
from   poc import struts2_032
from   colorama import Fore as fore
import sys

def console():
    target = input("[ INPUT ] 输入目标url：")
    
    struts2_032.run(target)

