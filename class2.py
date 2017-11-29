class count:
	c=0
	def __init__(self,name):
		self.name=name
		count.c+=1
	@classmethod
	def display(self):
		print("Name : {}".format(self.name))

C=count("David")
C.display()
print(C.c)
C1=count("Max")
C1.display()
print(C1.c)
print(C.c)
count.display()
