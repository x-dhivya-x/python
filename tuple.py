#tuple are ordered ,unchangeable ,allow duplicate values
#we cant modify,change,update,insert any value to the tuple so it is called unchangeable or immutable in tuple


x=(11,22,33,44,55)
print(x)
print(type(x))

#we convert tuple into list or anything then we change the value in tuple

y=list(x)
print(y)
print(type(y))
y.append(66)
print(y)
x= tuple(y)
print(x)


for i in x:
	print(i)

