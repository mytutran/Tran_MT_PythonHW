from random import randint
# define a python function that takes an argument
def winorlose(status):
	#status will be either won or lost - you're passing this in as an argument
	print("called win or lose")
	print("+++++++++++++++++++++++++++++++++++++++++")

	print("You", status, "! Would you like to play again?")
	choice = input("Y / N ?")	
	print(choice)

	if (choice.lower() is "Y"):
			print("You chose to quit.")
			exit()

	elif (choice.lower() is "N"):
			# reset the game so we can start all over again.
			global player_lives
			global computer_lives
			global player
			global computer
			global choices
			player_lives = 1
			computer_lives = 1
			player = False
			computer = choices [randint(0,2)]
		
	else:
			print("That's not a valid choice! Input 'Y' or 'N'")
			choice = input("Y / N ?")	
			print(choice)


		
