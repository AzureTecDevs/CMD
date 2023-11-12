import sys
import os

def readFile(file):
	f = open(file)
	lines = f.readlines()
	res = []
	for sub in lines:
	    res.append(sub.replace("\n", ""))
	return res

def readFileAs(file, ext):
	f = open(file)
	lines = f.readlines()
	res = []
	re = []
	for sub in lines:
		if ext == 'etx' or ext == 'ext':
			res.append(sub.replace("\n", ""))
			for txt in res:
				re.append(txt.split('&'))
			res = re
		else:
			res.append(sub.replace("\n", ""))
		return res

def getExtContents(file):
	res = readFileAs(file, 'ext')
	return res

def getExtIndex(file, index):
	re = getExtContents(file)
	res = re[0][index]
	return res

def getExtData(file, type):
	t = getExtContents(file)
	list = t[0]
	if type.lower() == 'url':
		return list[1]
	elif type.lower() == 'name':
		return list[0]
	elif type.lower() == 'isEngine':
		return list[2]
	elif type.lower() == 'code':
		return list[4]
	elif type.lower() == 'opt':
		return list[3]
	else:
		return ''