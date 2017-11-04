#!/usr/bin/python

import sys
from sets import Set

s = set()
for line in sys.stdin:
	data = line.strip()
	fileName = data
	s.add(fileName)
	#print fileName
#print s
print len(s)
