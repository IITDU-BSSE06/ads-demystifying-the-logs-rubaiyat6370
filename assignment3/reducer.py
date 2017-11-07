oldurl = None
maxCount = -9999

for line in sys.stdin:
	data = line.strip()
	if data == "" or data is None:
		continue
	url = data
	if oldurl and oldurl != url:
		#print oldurl, "\t", hit
		if hit > maxCount:
			path = oldurl
			#maxCount = hit
		oldurl = url
		hit = 0
	oldurl = url
	hit += 1
print path
#print maxCount
	
