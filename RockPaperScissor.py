# import random module
import random
# print multiline instruction
# performstring concatenation of string
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
	+ "Rock vs Paper -> Paper wins \n"
	+ "Rock vs Scissors -> Rock wins \n"
	+ "Paper vs Scissors -> Scissor wins \n")

while True:
	
	print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
	# take the input from user
	choice=int(input("Enter your choice :"))
	while choice > 3 or choice <1:
	    choice=int(input('Enter a valid choice please '))
		
	if choice == 1:
		choice_name= 'ROCK'
	elif choice == 2:
		choice_name= 'PAPER'
	else:
		choice_name= 'SCISSOR'
		
		# print user choice
	print('User choice is \n',choice_name)
	print('Now its Computers Turn....')
	comp_choice = random.randint(1,3)
	
	while comp_choice == choice:
		comp_choice = random.randint(1,3)
		

	if comp_choice == 1:
		comp_choice_name = 'ROCK'
	elif comp_choice == 2:
		comp_choice_name = 'PAPER'
	else:
		comp_choice_name = 'SCISSOR'
	print("Computer choice is \n", comp_choice_name)
	print(choice_name,'Vs',comp_choice_name)
	# we need to check of a draw
	if choice == comp_choice:
		print('Its a Draw',end="")
		result="DRAW"
	# condition for winning	 
	if (choice==1 and comp_choice==2):
		print('paper wins =>',end="")
		result='PAPER'
	elif (choice==2 and comp_choice==1):
		print('paper wins =>',end="")
		result='PAPER'
		
	
	if (choice==1 and comp_choice==3):
		print('Rock wins =>\n',end= "")
		result='ROCK'
	elif (choice==3 and comp_choice==1):
		print('Rock wins =>\n',end= "")
		result='ROCK'
		
	if (choice==2 and comp_choice==3):
		print('Scissors wins =>',end="")
		result='SCISSOR'
	elif (choice==3 and comp_choice==2):
		print('Scissors wins =>',end="")
		result='ROCK'
	# Printing either user or computer wins or draw
	if result == 'DRAW':
		print("<== Its a tie ==>")
	if result == choice_name:
		print("<== User wins ==>")
	else:
		print("<== Computer wins ==>")
	print("Do you want to play again? (Y/N)")
	ans = input().lower()
	if ans =='n':
		break
print("thanks for playing")
