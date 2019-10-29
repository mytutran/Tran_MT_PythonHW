#import the random package so that we can generate a random choice
from random import randint 

#choices is an array => an array is a container that can hold multiple values.
choices=["Rock","Paper","Scissors"]

#set the computer variable to one of these choices
computer= choices[randint(0,2)]

# set up the game loop so that we don't have to restart all the time
player = False
while player is False:
	#set player to True
	print("+++++++++++++++++++++++++++++++++++++++++")
	print("Choose your weapon!\n")
	print("+++++++++++++++++++++++++++++++++++++++++")

	player = input("Choose Rock, Paper or Scissors\n")

	print("Computer chose", computer, "\n")
	print("Player chose", player, "\n")

	if player == "Quit":
		exit()
	elif computer == player:
		print("Draw!")

	elif player.lower() == "rock":
		if computer == "Paper":
				print("You lose!", computer, "covers", player, "\n")
		else:
				print("You win!", player, "smashes", computer, "\n")

	elif player.lower() == "scissors":
		if computer == "Rock":
			print("You lose!", computer, "smashes", player, "\n")
		else:
				print("You win!", player, "cuts", computer, "\n")

	elif player.lower() == "paper":
		if computer == "Scissors":
			print("You lose!", computer, "cuts", player, "\n")
		else:
				print("You win!", player, "covers", computer, "\n")	

	else:
		print("That's not a valid choice, try again.")			





	#need to check all of our conditions after checking for a tie.	
	player = False
	computer = choices[randint(0,2)]
