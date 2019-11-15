#import the random package so that we can generate a random choice
from random import randint	
# from gameFunctions import winlose
from gameFunctions import compare
from gameFunctions import config



# set up some variables for player and AI lives1

# player_lives = 5
# computer_lives = 5

#choices is an array => an array is a container that can hold multiple values.
choices=["rock","paper","scissors"]

#set the computer variable to one of these choices
computer= choices[randint(0,2)]

# set up the game loop so that we don't have to restart all the time

player = False


while player is False:
	#set player to True

	print("———————————————————————————————")	
	print("____________________  _________")
	print("\______   \______   \/   _____/")
	print(" |       _/|     ___/\_____  \ ")
	print(" |    |   \|    |    /        \ ")
	print(" |____|_  /|____|   /_______  /")
	print("        \/                  \/ ")
	print("———————————————————————————————")
	print("Computer lives: ", config.computer_lives, "/5\n")
	print("Player lives: ", config.player_lives, "/5\n")
	print(" ____  __  ___  _  _  ____  _   ")
	print("(  __)(  )/ __)/ )( \(_  _)/ \  ")
	print(" ) _)  )(( (_ \) __ (  )(  \_/  ")
	print("(__)  (__)\___/\_)(_/ (__) (_)  ")
	



	config.player = input("Choose Rock, Paper or Scissors\n")
	config.player = config.player.lower()

	print("Computer chose", config.computer, "\n")
	print("Player chose", config.player, "\n")
 
	compare.compare()


	# if player.lower() == "quit":
	# 	exit()
	# elif computer == player: 
	# 	print("Draw!")

	# elif player.lower() == "rock":
	# 	if computer == "paper":
	# 			print("You lose!", computer, "covers", player, "\n")
	# 			player_lives = player_lives - 1
	# 	else:
	# 			print("You win!", player, "smashes", computer, "\n")
	# 			computer_lives = computer_lives - 1

	# elif player.lower() == "scissors":
	# 	if computer == "rock":
	# 		print("You lose!", computer, "smashes", player, "\n")
	# 		player_lives = player_lives - 1
	# 	else:
	# 			print("You win!", player, "cuts", computer, "\n")
	# 			computer_lives = computer_lives - 1

	# elif player.lower() == "paper":
	# 	if computer == "scissors":
	# 		print("You lose!", computer, "cuts", player, "\n")
	# 		player_lives = player_lives - 1
	# 	else:
	# 			print("You win!", player, "covers", computer, "\n")
	# 			computer_lives = computer_lives - 1	
	# else:
	# 		print("That's not a valid choice, try again.")



			

	# handle all lives lost for player or AI
	# if player_lives is 0:
	# 	winlose.winorlose("lost") 
		# print("You have lost the game! Would you like to play again?")
		# choice = input("Y / N ?")	
		# print(choice)

		# if (choice is "N") or (choice is "n"):
		# 	print("You chose to quit.")
		# 	exit()

		# elif (choice is "Y") or (choice is "y"):
		# 	# reset the game so we can start all over again.
		# 	player_lives = 5
		# 	computer_lives = 5
		# 	player = False
		# 	computer = choices [randint(0,2)]

	# elif computer_lives is 0: 
	# 	winlose.winorlose("won")
		# print("You have won the game! Would you like to play again?")
		# choice = input("Y / N?")	
		# print(choice)

		# if (choice is "N") or (choice is "n"):
		# 	print("You chose to quit.")
		# 	exit()

		# elif (choice is "Y") or (choice is "y"):
		# 	# reset the game so we can start all over again.
		# 	player_lives = 5
		# 	computer_lives = 5
		# 	player = False
		# 	computer = choices [randint(0,2)]
		

	# else:
	# 	# need to check all of our conditions after checking for a tie.	
	# 	player = False
	# 	computer = choices[randint(0,2)]

	





