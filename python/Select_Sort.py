#!/usr/bin/python
#-*-coding:utf8-*-
__author__ = 'Im'

import os
import time
import sys
import traceback

reload(sys)
sys.setdefaultencoding('utf8')

def selectSort():
	"""选择排序
	一次循环找出其中符合规则的值放在相应的位置上
	每一次循环找出最小值 记录下标 循环结束后互换位置
	"""


	li = [3, 2, 4, 7, 4, 1, 9, 0]
	if len(li) == 0:
		print u"list 不能为空"
		return
	for i in range(len(li) - 1):
		temp = i
		ttemp = li[i]
		for j in range(i, len(li)):
			if ttemp >= li[j]:
				temp = j
				ttemp = li[j]
			else:
				pass
			# print i, j, temp

		if i != temp:
			liTemp = li[temp]
			li[temp] = li[i]
			li[i] = liTemp
		# print li
	print li

if __name__ == "__main__":
	selectSort()

