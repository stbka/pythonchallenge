#!/usr/bin/env python

import urllib
import zipfile
import shutil
import re
from os import remove, mkdir

URL='http://www.pythonchallenge.com/pc/def/channel.zip'
ZIPFILE='channel.zip'

def solution_1(url):
	# download
	print urllib.urlretrieve(url, ZIPFILE)
	
	# use tmp dir
	mkdir("tmp", 0700)
	shutil.move(ZIPFILE, 'tmp\%s' % ZIPFILE)
	
	# extract
	zf = zipfile.ZipFile("tmp\%s" % ZIPFILE, 'r')
	zf.extractall("tmp")
	
	# seearch for the answer
	next_nothing = 90052
	while True:
		file_data = open('tmp/%s.txt' % next_nothing, 'r').read()
		re_obj = re.search('\d+', file_data)
		try:
			next_nothing = re_obj.group()
			print '.',
		except AttributeError:
			print "ERROR: Kein group attribut vorhanden."
			print "%s.txt: %s" % (next_nothing, file_data)
	
	# cleanup
	zf.close()
	#shutil.rmtree("tmp")
	
solution_1(URL)