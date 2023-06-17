name=input("Enter your name: ")

if(len(name)<3):
	print("Name atleast have 3 characters")
elif(len(name)>50):
	print("Name can be max of 50 characters")
else:
	print(name +"!!! It is a good name")