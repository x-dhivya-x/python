l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
matrix=[l1,l2,l3]
print(f"{l1}\n{l2}\n{l3}")
position=input("Enter the position to hide your things: ")
row=int(position[0])
column=int(position[1])
result=matrix[row-1][column-1]='X'
print(f"{l1}\n{l2}\n{l3}")