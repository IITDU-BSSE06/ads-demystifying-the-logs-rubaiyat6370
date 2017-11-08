#!/usr/bin/python

import sys
salesTotal = 0
oldKey = None

for line in sys.stdin:
	data = line.strip()
	if data == "" or data is None:
		continue
	thisKey = data

	if oldKey and oldKey != thisKey:
		print oldKey, "\t", salesTotal
		oldKey = thisKey
		salesTotal = 0
	oldKey = thisKey
	salesTotal += 1

if oldKey != None:
	print oldKey, "\t", salesTotal
