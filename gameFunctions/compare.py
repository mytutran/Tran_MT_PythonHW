from random import randint
from gameFunctions import winlose
from gameFunctions import config


def compare ():
	print("———————————————————")	
	print("Choose your weapon!")
	print("———————————————————")		
	
	

	if config.player.lower() == "quit":
			exit()
	elif config.computer == config.player: 
			print("Draw! Fight again!")	
	
	elif config.player.lower() == "rock":
			if config.computer == "paper":
					print("You lose!", config.computer, "covers", config.player, "\n")
					config.player_lives = config.player_lives - 1
				
			else:
					print("You win!", config.player, "smashes", config.computer, "\n")
					config.computer_lives = config.computer_lives - 1
					

	elif config.player.lower() == "scissors":
			if config.computer == "rock":
				print("You lose!", config.computer, "smashes", config.player, "\n")
				config.player_lives = config.player_lives - 1
					
			else:
					print("You win!", config.player, "cuts", config.computer, "\n")
					config.computer_lives = config.computer_lives - 1
			

	elif config.player.lower() == "paper":
			if config.computer == "scissors":
				print("You lose!", config.computer, "cuts", config.player, "\n")
				config.player_lives = config.player_lives - 1
				
			else:
					print("You win!", config.player, "covers", config.computer, "\n")
					config.computer_lives = config.computer_lives - 1	
					
	else:
		print("That's not a valid choice, try again.")
	
	if config.player_lives == 0:
		winlose.winorlose("lost") 

	elif config.computer_lives == 0: 
		winlose.winorlose("won")



	else:
		#need to check all of our conditions after checking for a tie.	
		config.player = False
		config.computer = config.choices[randint(0,2)]		

