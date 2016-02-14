print ("hello")
3+4
print (3+5)

class Person:
	def __init__(self):
		print(("Age of people").split())
	def __del__(self):
		print("delete people")
	def set(self, age):
		self.age=age

	def get(self):
		return self.age

p=Person()
p.set(7)
a=p.get()
print(type(a))
print("---", a)
print(list(range(6,0,-1)))