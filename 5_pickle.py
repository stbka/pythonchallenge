#!/usr/bin/env python

import pickle
from urllib import urlopen


URL = 'http://www.pythonchallenge.com/pc/def/banner.p'

def solution_1(url):
	
	pagesource = urlopen(url).read()
	object = pickle.loads(pagesource)
	
	for e in object:
		print e
	
	for line in object:
		for char, count in line:
			print char * count,
		print
	

solution_1(URL)	