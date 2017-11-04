#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	ip = data[6]
	print ip
