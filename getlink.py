
#coding=utf-8

import re
import os
import urllib.request


web_url = 'http://www.naturalearthdata.com/downloads/10m-cultural-vectors/'
html_file_local_temp = 'html.txt'

html = ''

#因为代码需要调试，下载网页存储为本地文件速度快
if os.path.isfile(html_file) :
	file_object = open(html_file_local_temp)
	try:
	     html = file_object.read( )
	finally:
	     file_object.close( )
else:
	response = urllib.request.urlopen(web_url)
	html = response.read()

	print ('html 下载完成')
	html = html.decode('utf-8')
	with open(html_file_local_temp, "w") as code:
	     code.write(html)

#print (html)


#pattern = re.compile(r'href="(http://.*\.zip)"')
pattern = re.compile(r'http://(.+?\.zip)')

url_list = []
it = re.finditer(pattern, html)
for match in it:
	url_list.append( match.group(0) )
	#print ( match.group(0) )

#去除重复url
myset = set(url_list)

#alist = list(myset) 

#输出到屏幕上
for item in myset:
	print ( item )

#m = re.search(pattern, html)
#if m:
#	for item in m.group:
#		print( item )
#		print('\n')
#else:
#	print ('not match'  )