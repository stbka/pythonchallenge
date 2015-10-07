#!/usr/bin/env python

import os
import re
import shutil
import urllib
import zipfile


URL = 'http://www.pythonchallenge.com/pc/def/channel.zip'
ZIPFILE = 'channel.zip'

def solution_1(url):
	# download
	os.environ['http_proxy'] = 'http://proxy:8888'
	print urllib.urlretrieve(url, ZIPFILE)
	
	# use tmp dir
	os.mkdir("resources/lvl6", 0700)
	shutil.move(ZIPFILE, 'resources/lvl6\%s' % ZIPFILE)
	
	# extract
	zf = zipfile.ZipFile("resources/lvl6\%s" % ZIPFILE, 'r')
	zf.extractall("resources/lvl6")
	
	# seearch for the answer
	next_nothing = 90052
	while True:
		file_data = open('resources/lvl6/%s.txt' % next_nothing, 'r').read()
		re_obj = re.search('\d+', file_data)
		try:
			next_nothing = re_obj.group()
			print '.',
		except AttributeError:
			print "\nERROR: Kein group attribut vorhanden."
			print "%s.txt: %s" % (next_nothing, file_data)
			break
	
	# cleanup
	zf.close()
	# shutil.rmtree("tmp")
	
solution_1(URL)
