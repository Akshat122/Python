class Employee:
	"""class for employee"""
#	def __init__(self):
#		pass
	def __init__(self,a,b):
		self.id=a
		self.name=b
	def get(self ,a,b):
		self.id=a
		self.name=b
	def show(self):
		print("ID {}".format(self.id))
		print("Name {} ".format(self.name))

Emp=Employee(101,"Akshat")
#print(Employee.__doc__)
#Emp.get(101,"David")
#Emp.show()
#Emp1=Employee()
#setattr(Emp,'name',"Akshat")
#a=getattr(Emp,'name')
#print(a)
#print(Employee.__name__)
