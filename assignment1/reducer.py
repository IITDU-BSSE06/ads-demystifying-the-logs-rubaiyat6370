#!/usr/bin/python

import sys

ipcount = 0

for line in sys.stdin:
	data = line.strip()
	ip = data
	if "10.99.99.186" == ip:
		ipcount +=1

print ipcount
	
