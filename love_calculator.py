name1=input("What is your name? ").lower()
name2=input("What is his/her name? ").lower()
combine_name=name1+name2
t=combine_name.count('t')
r=combine_name.count('r')
u=combine_name.count('u')
e=combine_name.count('e')
true=t+r+u+e
l=combine_name.count('l')
o=combine_name.count('o')
v=combine_name.count('v')
e=combine_name.count('e')
love=l+o+v+e
love_score=str(true)+str(love)
if int(love_score)<10 or int(love_score)>90:
	print(f"Your love score is {love_score} and You are made for each other!!!")
elif int(love_score)>=40 and int(love_score)<=50:
	print(f"Your love score is {love_score} and Both are good couples!!!")
else:
	print(f"Your love score is {love_score}")