file1=open("/home/prajpoot/Downloads/vb3.3/analysis/unsolved/ambiguity_LHS_RHS_solved1","r")
basev="/home/prajpoot/Downloads/vb3.3/v3.3/"
for line in file1.readlines():
	parts=line.strip().split("\t")
	classes=parts[2].strip().split(" ")
	res=""
	for i in classes:
		files=open(basev+i+".xml","r")
		data=files.read()
		if parts[1].strip() in data:
			res=res+" "+i
		files.close()
	if res.strip()!="":
		print parts[0]+"\t"+parts[1]+"\t"+res
	
		

file1.close()