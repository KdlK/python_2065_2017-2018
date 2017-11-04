class Person:
	def __init__(self, age, name):
		self.age = age
		self.name = name
	def outputAge(self):
		print(self.age)

p = Person(17, 'Valera')
p.outputAge()			