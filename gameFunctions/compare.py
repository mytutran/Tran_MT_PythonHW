from random import randint
from gameFunctions import winlose
from gameFunctions import config
config.glovar()

def compare():
	print("———————————————————")	
	print("Choose your weapon!")
	print("———————————————————")		
	
	player = input("Choose Rock, Paper or Scissors\n")
	player = player.lower()
	choices=["rock","paper","scissors"]
	computer= choices[randint(0,2)]


	print("Computer chose", computer, "\n")
	print("You chose", player, "\n")


	if player.lower() == "quit":
			exit()
	elif computer == player: 
			print("Draw! Fight again!")	
	
	elif player.lower() == "rock":
			if computer == "paper":
					print("You lose!", computer, "covers", player, "\n")
					config.player_lives = config.player_lives - 1
				
			else:
					print("You win!", player, "smashes", computer, "\n")
					config.computer_lives = config.computer_lives - 1
					

	elif player.lower() == "scissors":
			if computer == "rock":
				print("You lose!", computer, "smashes", player, "\n")
				config.player_lives = config.player_lives - 1
					
			else:
					print("You win!", player, "cuts", computer, "\n")
					config.computer_lives = config.computer_lives - 1
			

	elif player.lower() == "paper":
			if computer == "scissors":
				print("You lose!", computer, "cuts", player, "\n")
				config.player_lives = config.player_lives - 1
				
			else:
					print("You win!", player, "covers", computer, "\n")
					config.computer_lives = config.computer_lives - 1	
					
	else:
		print("That's not a valid choice, try again.")
	
	if config.player_lives == 0:
		winlose.winorlose("lost") 

	elif config.computer_lives == 0: 
		winlose.winorlose("won")



	else:
		#need to check all of our conditions after checking for a tie.	
		player = False
		computer = choices[randint(0,2)]		

