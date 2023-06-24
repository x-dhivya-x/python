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