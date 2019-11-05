
def compare(choice)
	print("called compare weapons")
		if player.lower() == "Quit":
				exit()
			elif computer == player:
				print("Draw!")

			elif player.lower() == "rock":
				if computer == "paper":
						print("You lose!", computer, "covers", player, "\n")
						player_lives = player_lives - 1
				else:
						print("You win!", player, "smashes", computer, "\n")
						computer_lives = computer_lives - 1

			elif player.lower() == "scissors":
				if computer == "rock":
					print("You lose!", computer, "smashes", player, "\n")
					player_lives = player_lives - 1
				else:
						print("You win!", player, "cuts", computer, "\n")
						computer_lives = computer_lives - 1

			elif player.lower() == "paper":
				if computer == "scissors":
					print("You lose!", computer, "cuts", player, "\n")
					player_lives = player_lives - 1
				else:
						print("You win!", player, "covers", computer, "\n")
						computer_lives = computer_lives - 1	



			else:
				print("That's not a valid choice, try again.")