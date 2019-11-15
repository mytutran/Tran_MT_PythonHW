from random import randint
from gameFunctions import config

# define a python function that takes an argument

choices=["y","no"]

def winorlose(status):
	#status will be either won or lost - you're passing this in as an argument
	print("————————————")	
	print("Match Ended")
	print("————————————")	

	print("You", status,"!""Would you like to play again?")
	print("    _    ____    _    ___ _   _ ___ ")
	print("   / \  / ___|  / \  |_ _| \ | |__ \ ")
	print("  / _ \| |  _  / _ \  | ||  \| | / /")
	print(" / ___ | |_| |/ ___ \ | || |\  ||_| ")
	print("/_/   \_\____/_/   \_|___|_| \_|(_) ")

	choice = input("Y / N ?")	
	print(choice)

	if (choice is "N") or (choice is "n"):	
		print("You chose to quit.")
		exit()
			
	elif (choice is "Y") or (choice is "y"):
		
		# reset the game so we can start all over again.
		
		config.player_lives = 5
		config.computer_lives = 5
		config.player = False
		config.computer = config.choices [randint(0,2)]
		

	else:
		print("Your choice is invalid.")
		print("Input Y or N!")
		winorlose(status)
		
