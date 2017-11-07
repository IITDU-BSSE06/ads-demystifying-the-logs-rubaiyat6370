#!/usr/bin/python

import sys

hit = 0
for line in sys.stdin:
	data = line.strip()
	if data == "" or data is None:
		continue
	url = data
	if "/assets/js/the-associates.js" == url:
		hit +=1
print hit
