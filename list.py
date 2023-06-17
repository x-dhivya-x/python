#list are ordered, changeable,contains same and different datatypes ,allow duplicate values.
list=["A","B","C","D"]
print(list)

list.append("E")
print(list)

list[0]= "Z"
print(list)

print(list[0:])

list.insert(2,"X")
print(list)

list.remove("D")    #remove method del the particular item
print(list)

list.pop(1)  #pop method delete the particular item specified by the index
print(list)


list.pop()    #without mention the index pop method del the last item
print(list)

del list[2]      #del also del the item specified by index #del also del entire list #del listnames
print(list)

#The clear() method empties the list.
#The list still remains, but it has no content.

list.clear()
print(list)


#without list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
for x in range(len(fruits)):
  if "a" in fruits[x]:
   print(fruits[x])

#with list comprehension   

newlist = [x for x in fruits if "a" in x]

print(newlist)  


#sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
#sorting in ascending order

list=["red","blue","orange","pink","yellow","black","white","violet","brown"]
list.sort()
print(list)

#sorting in descending order
list.sort(reverse=True)
print(list)

#sorting in numbers

list=[8,3,7,6,9,2,1,5]
list.sort()
print(list)

#join list

l1= [1,2,3,4]
l2= ["dhivya","hari","jagatheesh"]
l3= l1 + l2
print(l3)

for x in l2:
  l1.append(x)
  print(l1)


l1=[6,3,10,1,7,9]
max=l1[0]
for i in l1:
  if i>max:
    max=i
    print(max)
    

list1=[3,5,6,7,5,5,1,7,3,4]
unique=[]
for i in list1:
  if i not in unique:
    unique.append(i)
print(unique)