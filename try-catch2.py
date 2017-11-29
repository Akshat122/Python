while True:
	try:
		a=str(input("Enter a name : "))
		b=int(input("Enter surname : "))
		print("Done..")
		break
	except Exception as e:
		print(e)
