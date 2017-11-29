a=["aabaa","s","b","sub","left","cbc"]
b=len(a)

for x in range(0,b):
		b=len(a[x])
#		print(b)
		
		if b>1:
#			print("len > 1")
	#		print(a[x])
	#		print("-----")
			if(a[x][0]==a[x][b-1]):
				print("found!!")
				print(a[x])
				print("------")
