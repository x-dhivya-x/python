"""
import random
print("'stone wins against scissors'\n'paper wins against stone'\n'scissor wins against paper' ")
user_choice=int(input(f"Enter your choice ,Type 0 for 'stone' Type 1 for 'paper' Type 2 for 'scissor': "))
if user_choice>=3 or user_choice<0:
	print("Invalid input,You lose!") 
else:
	print(f"Your choice is: {user_choice}")
	computer_choice=random.randint(0,2)
	print(f"Computer choice is: {computer_choice}")
	if user_choice==0 and computer_choice==0:
		print("It's a Draw")
	elif user_choice==1 and computer_choice==0:
		print("You Wins!")
	elif user_choice==2 and computer_choice==0:
		print("Computer Wins!")
	elif user_choice==0 and computer_choice==1:
		print("Computer Wins!")
	elif user_choice==1 and computer_choice==1:
		print("It's a Draw")
	elif user_choice==2 and computer_choice==1:
		print("You Wins!")
	elif user_choice==0 and computer_choice==2:
		print("You Wins!")
	elif user_choice==1 and computer_choice==2:
		print("Computer Wins!")
	elif user_choice==2 and computer_choice==2:
		print("It's a Draw")
"""
import random
c = ("Stone","Paper","Scissor") #Added
print("stone wins against scissors\npaper wins against stone\nscissor wins against paper\n".title())
while 1: #Added
	choice=(input(f"\nType 0 for 'stone'\nType 1 for 'paper'\nType 2 for 'scissor'\n\nEnter your choice: ")).strip()
	if choice in ["0","1","2"]: #Added
		user_choice = int(choice)
		print(f"\nYour choice is: {c[user_choice]}") #Changed
		computer_choice=random.randint(0,2)
		print(f"Computer choice is: {c[computer_choice]}\n") #Changed
		if user_choice == computer_choice: #Changed
			print("It's a Draw")
		elif user_choice==1 and computer_choice==0:
			print("You Wins!")
		elif user_choice==2 and computer_choice==0:
			print("Computer Wins!")
		elif user_choice==0 and computer_choice==1:
			print("Computer Wins!")
		elif user_choice==2 and computer_choice==1:
			print("You Wins!")
		elif user_choice==0 and computer_choice==2:
			print("You Wins!")
		elif user_choice==1 and computer_choice==2:
			print("Computer Wins!")
	else: #changed
		print("Invalid input,You lose!") 
