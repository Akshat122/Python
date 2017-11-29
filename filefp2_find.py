s=str(input("Enter a name to search : "))
fp=open("Names.txt","r")
a=fp.readlines()
print(a)
if s in a:
	print(fp.tell())
	print("found!!")
fp.close()
