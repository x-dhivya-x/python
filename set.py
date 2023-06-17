#set is a collection which is unordered, unchangeable*,do not allow duplicate values and unindexed.

set={"dhivya",2,4,0,9,"welcome","dhivya"}
print(set)
#print(set[1])   #error -set object is not subscriptable


#Set items are unchangeable, but you can remove items and add new items.

set.add(1704)
print(set)

#To add items from another set into the current set, use the update() method.
#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

s1={1,2,3,4}
s2={5,6,7,8}
s3=[9,10,11,12]
s1.update(s2) 
s2.update(s3) 
print(s1)
print(s2)

x={"noodles","friedrice","naan","grillchicken"}
w={"rice","gravy","dosa"}

# If the item to remove does not exist, remove() will raise an error.
#If the item to remove does not exist, discard() will NOT raise an error.
#pop() method to remove an item, but this method will remove the last item.set is unordered so we dont know which item is removed
#The return value of the pop() method is the removed item.


x.remove("naan")
print(x)
y=x.pop()
print(y)
print(x)

#clear() method empties the set:
#del keyword will delete the set completely:

#join 2 set

z =x.union(w)
print(z)



