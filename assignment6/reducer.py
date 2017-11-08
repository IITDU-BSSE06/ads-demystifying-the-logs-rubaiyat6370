#!/usr/bin/python

import sys

yearNine = 0
yearTen = 0
yearEleven = 0

for line in sys.stdin:
	data = line.strip()
	if data == "" or data is None:
		continue
	values = line.strip().split("/")
	year = values[2].strip().split(":")
	
	if year[0] == "2009":
		yearNine += 1
	if year[0] == "2010":
		yearTen += 1
	if year[0] == "2011":
		yearEleven += 1

print "2009", "\t", yearNine
print "2010", "\t", yearTen
print "2011", "\t", yearEleven
	