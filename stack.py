#Implement a stack using a list in Python. Include the necessary methods such as push, removeElm, and isEmpty.

## creating the class
class stack:
	# defining the funtions:
	def __init__(self):
		self.stack = []

	# adding the element in the defined array 
	def addElem(self,item):
		self.stack.append(item);

	# removing the element from the array 
	def removeElm(self,item):
		if not self.isEmpty():
			return self.stack.removeElm()
		else:
			return 'Stack is empty'
	
	def isEmpty(self):
		return len(self.stack) == 0\


my_stack = stack()
my_stack.addElem(10)
my_stack.addElem(20)
my_stack.addElem(30)

print(my_stack.removeElm())  # Output: 30
print(my_stack.removeElm())  # Output: 20
print(my_stack.isEmpty())  # Output: False
print(my_stack.removeElm())  # Output: 10
print(my_stack.isEmpty())  # Output: True