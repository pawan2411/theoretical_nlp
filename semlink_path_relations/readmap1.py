file1=open("/home/prajpoot/Downloads/vb3.3/analysis/all","r")
for line in file1.readlines():
	parts=line.strip().split("\t")
	if len(parts[1].strip().split(","))==1 and len(parts[2].strip().split(" "))==1:
		print line.strip()
	else:
		pass
		# print line.strip()
		# pass
		

file1.close()