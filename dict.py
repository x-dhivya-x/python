#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

family={
	1:"Jagatheeshwaran",
	2:"Mohana",
	3:"Harivignesh",
	4:"Dhivya"
}
print(family)
print(family.keys())
print(family.values())
print(family.items())

"""
#Duplicates Not Allowed
#Dictionaries cannot have two items with the same key

	4:"Dhivya",
	4:"Subha"
"""

print(family[1])

#method called get() that will give the value of thee respected key

print(family.get(1))

family[5]="Jagatheesh"
#The update() method will update the dictionary with the items from the given argument
family.update({3:"Hari"})
print(family)

family.pop(5)
print(family)
for x in family:
	
    print(family[x])

phone=input("Enter the phone: ")
digits={
	"1":"one",
	"2":"two",
	"3":"three",
	"4":"four",
	"5":"five"
}
output=""
for x in phone:
	output+=digits[x]+" "
print(output)
