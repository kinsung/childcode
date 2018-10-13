# -*- coding: utf-8 -*-


'''
@author: kisung@2018
'''
import os
import sys
import re
import codecs
import chardet

#在vs中用正则表达式查找 \".*\"，对其结果保存为两个文件，对其中一个文件中的文本进行翻译，把这两个文件输入，替换代码
#确保两个文件的行数是完全一致的。 
#一般情况下，只输入一个翻译后的文件即可 

class CItem:
	def __init__(self):
		self.filepath = ''
		self.lineIndex = -1
		self.srcCode = ''  #翻译后的文字 
		self.dstCode =''    #翻译后的文字 

class CItemMgr:
	def __init__(self):
		self.dict={} #key: filePath, value: CItem List
		#listItem = []
	
	def append(self, ci):		
		if not ci.filepath:
			print('ci filepath is null')
			exit()
		if ci.filepath in self.dict:
			self.dict[ci.filepath].append(ci)
		else:
			listItem = [ci]
			self.dict[ci.filepath] = listItem

	def do_replace(self):
		for key  in self.dict:
			print('key: '+ key )
			path = key.strip()
			rawdata = open(path, 'rb').read()
			result = chardet.detect(rawdata)
			charenc = result['encoding']

			f = open(path,'r',encoding=charenc)
			fileLines = f.readlines()
			f.close()

			#print('fileLines: '+fileLines[0]+'  ++ '+fileLines[1])

			itemList = self.dict[key]
			for i in range(len(itemList)):
				ci =  itemList[i]
				try:
						if ci.dstCode:
							fileLines[ci.lineIndex-1] = ci.dstCode #+'翻译后'
						else:
							fileLines[ci.lineIndex-1] = ci.srcCode #+'翻译后'
				except:
					print('超出大小 ci.lineIndex-1: '+str(ci.lineIndex-1))
					print('srcCode:'+ ci.srcCode+'dstCode'+str(ci.dstCode))

			f = open(path+'.txt','w', encoding="utf8")
			f.writelines(fileLines)
			f.close()
		

#返回 filePath、lineIndex、code
def parse_line(line):
	filePath = ''
	lineIndex = -1
	code = ''
	idx = line.find('):')
	if idx >0:
		tok0 = line[0:idx]
		idxBracket = tok0.rfind('(')
		if idxBracket >0:
			lineIndex = tok0[idxBracket+1:]
			filePath = tok0[0:idxBracket]
		code = line[idx+2:]
		#print(filePath)
		#print(lineIndex)
		#print(code)
		return filePath, int(lineIndex), code

	return '', -1, ''


def process_file(filepathSrc, filepathDst):
	fsrc = open(filepathSrc,'r',encoding="utf8")
	resultSrc = list()
	for line in fsrc.readlines():                       #依次读取每行
		#line = line.strip()                             #去掉每行头尾空白
		#if not len(line) or line.startswith('#'):      #判断是否是空行或注释行
		#	continue                                    #是的话，跳过不处理
		idx = line.find("查找")
		if idx>=0 and idx<4:
			continue
		idx = line.find("匹配行")
		if idx>=0 and idx<4:
			continue
		resultSrc.append(line)                             #保存
	#resultSrc.sort()                                       #排序结果
	fsrc.close()
	
	itemMgr = CItemMgr()
	
	if filepathDst:
		fdst = open(filepathDst,'r',encoding="utf8")
		resultDst = list()
		for line in fdst.readlines():                       #依次读取每行
			#line = line.strip()                             #去掉每行头尾空白
			#if not len(line) or line.startswith('#'):      #判断是否是空行或注释行
			#	continue                                    #是的话，跳过不处理
			idx = line.find("查找")
			if idx>=0 and idx<4:
				continue
			idx = line.find("匹配行")
			if idx>=0 and idx<4:
				continue
			resultDst.append(line)                             #保存
		#resultDst.sort()                                       #排序结果
		fdst.close()
		
		if len(resultSrc) != len(resultDst):
			print('输入翻译前后对照两个文件不匹配:'+filepathSrc +',    '+filepathDst)
			return
		for i in range(len(resultSrc)):
			lineSrc = resultSrc[i]
			lineDst = resultDst[i]
			pathSrc, lineIndexSrc, codeSrc = parse_line(lineSrc)
			pathDst, lineIndexDst, codeDst = parse_line(lineDst)
			if pathSrc != pathDst or lineIndexSrc !=lineIndexDst :
				print("源代码行不匹配:")
				return
			ci = CItem()
			ci.lineIndex = lineIndexSrc
			ci.filepath = pathSrc
			ci.srcCode = codeSrc
			ci.dstCode = codeDst
			itemMgr.append(ci)
	else:		
		for i in range(len(resultSrc)):
			lineSrc = resultSrc[i] #resultSrc即是resultDst
			pathSrc, lineIndexSrc, codeSrc = parse_line(lineSrc)
			ci = CItem()
			ci.lineIndex = lineIndexSrc
			#print('ci.lineIndex: '+str(ci.lineIndex))
			ci.filepath = pathSrc
			ci.srcCode = codeSrc
			#ci.dstCode = 
			itemMgr.append(ci)

	itemMgr.do_replace()


def main(argv):
	for arg in argv:
		print(arg)
	if len(argv)==2:
		process_file(argv[1], '')
	if len(argv)==3:
		process_file(argv[1], argv[2])



if __name__ == '__main__':
	
	main(sys.argv)
