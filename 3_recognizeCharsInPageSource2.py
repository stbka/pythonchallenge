#!/usr/bin/env python

from urllib import urlopen
import re

URL = "http://www.pythonchallenge.com/pc/def/equality.html"

def solution_1(url):
	raw_html = urlopen(url).read()
	
	s = ''
	
	first_char = 0
	last_char = first_char + 9
	
	while last_char <= len(raw_html):
		tmp_text = raw_html[first_char:last_char]
		re_obj = re.search("[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]", tmp_text)
		if re_obj:
			s += tmp_text[re_obj.start():re_obj.end()][4]
		
		first_char += 1
		last_char += 1
		
	return s
	
	
print solution_1(URL)