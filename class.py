class House:	#define a class
	windows=""	#class attributes
	door=0
	length=0
	breadth=0
	def square_feet(self):	#define a function in a class and it is known as methods of class 
		print(f"The squarefeet of the house is {self.length*self.breadth} sq.ft")


house1=House()	#creating object

house1.windows="Glass"	#accessing class attributes &assign value to the attributes
house1.door=4
print(f"Windows Feature is {house1.windows}")
print(f"The house1 have {house1.door} door")

house1.length=15
house1.breadth=45
house1.square_feet()