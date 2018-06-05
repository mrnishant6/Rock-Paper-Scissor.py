	print("Rock....")
print("Paper....")
print("Scissor....")

player1=input("Player1,Make Your Move:  ")
player2=input("Player2,Make Your Move:  ")

if player1 == player2:
	print("It's a Tie")
elif player1 == "rock":
	if player2 == "scissor":
		print("player1 wins")

	elif player2 == "paper":
		print("player2 wins")

if player1 == "paper":
	if player2 == "scissor":
		print("player2 wins")

	elif player2 == "rock":
		print("player1 wins")

if player1 == "scissor":
	if player2 == "rock":
		print("player2 wins")

	elif player2 == "paper":
		print("player2 wins")

else:
	print("Something Went Wrong")	
