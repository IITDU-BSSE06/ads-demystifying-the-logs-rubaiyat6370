#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	year = data[3]
	print year