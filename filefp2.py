fp=open("Names.txt","a+")
while (True):
	s=str(raw_input("Enter a name "))
	fp.write(s)
#	fp.write("\n")
	inp=int(raw_input("enter 0 to quit"))
	if  inp==0:
		break
	else:
		continue
fp.close()
