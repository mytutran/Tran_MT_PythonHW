#import the random package so that we can generate a random choice
from random import randint 

# set up some variables for player and AI lives

#choices is an array => an array is a container that can hold multiple values.
choices=["Rock","Paper","Scissors"]

#set the computer variable to one of these choices
computer= choices[randint(0,2)]

# set up the game loop so that we don't have to restart all the time
player = False
while player is False:
	#set player to True
	print("+++++++++++++++++++++++++++++++++++++++++")
	print("Computer lives: ", computer_lives, "/5\n")
	print("Player lives: ", player_lives, "/5\n")
	print("Choose your weapon!\n")
	print("+++++++++++++++++++++++++++++++++++++++++")

	if player = input("Choose Rock, Paper or Scissors\n")

		print("Computer chose", computer, "\n")
		print("Player chose", player, "\n")
	else 	

			if player == "Quit":
				exit()
			elif computer == player:
				print("Draw!")

			elif (player == "Scissors" and computer == "Rock"):
				print("You lose!")
			
			elif (player == "Scissors" and computer == "Paper"):
				print("You win!")

			elif (player == "Paper" and computer == "Rock"):
				print("You win!")

			elif (player == "Paper" and computer == "Scissors"):
				print("You lose!")

			elif (player == "Rock" and computer == "Scissors"):
				print("You win!")

			elif (player == "Paper" and computer == "Scissors"):
				print("You lose!")			

	else:
		print("That's not a valid choice, try again.")			





	#need to check all of our conditions after checking for a tie.	
	player = False
	computer = choices[randint(0,2)]
