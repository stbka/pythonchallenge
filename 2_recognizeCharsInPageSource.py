#!/usr/bin/env python

from string import ascii_lowercase
from urllib import urlopen


URL = "http://www.pythonchallenge.com/pc/def/ocr.html"

def solution_1(url):
	# raw_html = urlopen(url, proxies = { 'http': 'http://proxy:8888' }).read()
	raw_html = urlopen(url).readlines()
	
	s = ''

	for l in raw_html:
		if len(l.replace(' ', '').replace('\n', '')) == 80:
			# data.append(l.replace('\n', ''))
			for char in list(l.replace('\n', '')):
				if char in ascii_lowercase:
					s += char
	return s
	
	
print solution_1(URL)