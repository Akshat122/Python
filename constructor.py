class Test:
	def __init__(self,marks=""):
		self.marks=marks
	def display(self):
		print("Marks {}".format(self.marks))

T=Test(900)
T.display()
T1=Test()
T1.display()
