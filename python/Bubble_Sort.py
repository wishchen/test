#!/usr/bin/python
#-*-coding:utf8-*-
__author__ = 'Im'

import os
import time
import sys
import traceback

reload(sys)
sys.setdefaultencoding('utf8')

def bubbleSort():
	"""冒泡排序
	两个for循环嵌套 外层循环整个list 内层循环从外层+1开始循环做比 大的后移 可能有list为空的情况,list中元素相等的情况
	"""
	# range(0, 10)
	# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

	lil = []
	li = [3, 2, 4, 7, 4, 1, 9, 0]
	if len(li) == 0:
		print u"list 不能为空"
		return
	for i in range(len(li)):
		for j in range(i + 1, len(li)):
			# print "i & j: ", i, j
			if li[i] >= li[j]:
				temp = li[i]
				li[i] = li[j]
				li[j] = temp
			else:
				pass
	print li

if __name__ == "__main__":
	bubbleSort()

