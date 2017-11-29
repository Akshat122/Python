try :
	file=open("Newfile.txt","r")
	file.write("File counter")
except Exception as e:
	print("Error : {}".format(e))

file.close()
print("closed")
