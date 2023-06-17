#catch the error in the try block
 
try:
	age=int(input("Enter the age: "))
	salary=10000/age
	print(age)
	print(salary)
except ValueError:
	print("Invalid Value")
except ZeroDivisionError: 
	print("Age cannot be zero")