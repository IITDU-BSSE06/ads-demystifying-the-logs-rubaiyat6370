#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	url = data[6]
	print url
