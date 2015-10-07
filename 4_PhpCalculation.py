#!/usr/bin/env python

import re
import time
from urllib import urlopen


URL="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
#NOTHING_NUM="12345"
NOTHING_NUM="62743"

def solution_1(url, num):
	
	while True:
		result = urlopen(url + num).read()
		#re_obj = re.match("(?<=and the next nothing is )\d+", result)
		re_obj = re.search("(?<=is )\d+", result)
		num = re_obj.group(0)
		
		

		
		print "next_num:", num
		

solution_1(URL, NOTHING_NUM)