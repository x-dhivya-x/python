import random
characters=['a','b','c','d','e','f','g','h','i',
		   'j','k','l','m','n','o','p','q','r','s','t','u',
           'v','w','x','y','z','A','B','C','D','E','F','G',
		   'H','I','J','K','L','M','N','O','P','Q','R','S',
           'T','U','V','W','X','Y','Z']
symbols=['@','!','#','$','%','&','*','(',')','+']
numbers=['0','1','2','3','4','5','6','7','8','9']
print("WELCOME TO THE PASSWORD GENERATOR!!!")
n_character=int(input("How many characters you want in the password: "))
n_symbol=int(input("How many symbols you want in the password: "))
n_number=int(input("How many numbers you want in the password: "))
password_list=[]
for i in range(n_character):
	char=random.choice(characters)
	password_list.append(char)
for j in range(n_symbol):
	sym=random.choice(symbols)
	password_list.append(sym)
for k in range(n_number):
	num=random.choice(numbers)
	password_list.append(num)
#print(password_list)
random.shuffle(password_list)
#print(password_list)
password=""
for i in password_list:
	password=password+i
print(f"Generated password is {password}")
