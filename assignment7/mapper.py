#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	request = data[5]
	print request