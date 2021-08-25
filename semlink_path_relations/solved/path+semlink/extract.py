# f=open("all.txt","r")
# classsentdic={}
# for line in f.readlines():
# 	parts=line.split("\t")
# 	classi=parts[0].split(" ")
# 	vbclass=classi[4].split("-")[0]+"-"+classi[4].split("-")[1]
# 	classt=vbclass
# 	if classt in classsentdic:
# 		classsentdic[classt]=classsentdic[classt]+"#####"+vbclass+"\t"+classi[3]+"\t"+parts[1].strip()
# 	else:
# 		classsentdic[classt]=line.strip()
# count=0

# f.close()
# f=open("all_data","r")
# for line in f.readlines():
# 	parts=line.strip().split("\t")
# 	cis=parts[2].strip().split(" ")
# 	for i in cis:
# 		if(i in classsentdic):
# 			print parts[1]+"\t"+i+"---------------------"
# 			exms=classsentdic[i].split("#####")
# 			for k in exms:
# 				print k
# 			print "--------------------------------------\n\n\n"

# f.close()

# SSSSSSSSSSSSSSSSSSSSSS
# gold={}
# f=open("/home/prajpoot/Downloads/vb3.3/analysis/solved/path+semlink/1.2.2c.okay","r")
# for line in f.readlines():
# 	parts=line.strip().split(" ")
# 	kid=parts[0]+" "+parts[1]+" "+parts[2]
# 	val=line.strip()
# 	if kid not in gold:
# 		gold[kid]=val
# f.close()

# f=open("/home/prajpoot/Downloads/vb3.3/analysis/solved/path+semlink/all.txt","r")
# for line in f.readlines():
# 	parts=line.strip().split(" ")
# 	kid=parts[0]+" "+parts[1]+" "+parts[2]
# 	if kid in gold:
# 		sentence=line.split("\t")[1].split(" ")
# 		args=gold[kid].split(" ")[10:]
# 		res=""
# 		for i in args:
# 			if i=="":
# 				continue
# 			ratio=i.split("-")[0].split(":")
# 			# print int(ratio[0]),int(ratio[len(ratio)-1])+int(ratio[0])
# 			res=res+"\t"+i.split("-")[1]+": "+ " ".join((sentence[int(ratio[0]):int(ratio[len(ratio)-1])+int(ratio[0])+1]))
# 		print line.strip().replace(kid,"")+"\t"+"\t"+res.strip()


# XXXXXXXXXXXXXXXXXXXXXXXX


# f=open("path_rel_classes","r")
# listopr=[]
# for line in f.readlines():
# 	listopr.append(line.strip())
# f.close()

# f=open("themerole_data","r")
# count=0
# for line in f.readlines():
# 	count+=1
# 	# print line.strip().split("\t")[0].split(" ")
# 	# print "\n\n"+str(count)
# 	if line.strip().split("\t")[0].split(" ")[1].strip() in listopr:
# 		print line.strip()

# RRRRRRRRRRRRRRRRRRRRR

f=open("/home/prajpoot/Downloads/vb3.3/analysis/solved/path+semlink/data_aligner","r")

for line in f.readlines():
	parts=line.split("-->")
	if len(parts)>1:
		if parts[1].count("null")==1:
			roles=parts[1].split("\t")
			if roles[0].strip()=="ch_of_state" and roles[len(roles)-1].strip()!=roles[len(roles)-2].strip() and roles[len(roles)-3].strip()!=roles[len(roles)-1].strip() and "not_" in roles[2].strip():
				print line.strip()
				continue				
			if roles[len(roles)-1].strip()!=roles[len(roles)-2].strip() and roles[1].strip()!="null" and roles[len(roles)-3].strip()!=roles[len(roles)-1].strip():
				print line.strip()