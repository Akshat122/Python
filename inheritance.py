class Test1:
	def __init__(self,name):
		self.name=name
	def __display(self):
		print("Name {}".format(self.name))
class Test2(Test1):
	def __init__(self,last_name,name):
		self.last_name=last_name
		Test1.__init__(self,name)
	def concat(self):
		self.last_name=self.name+self.last_name
		print("Name {}".format(self.last_name))

T=Test2("Kumar","Hari")
T.concat()
T.display()
