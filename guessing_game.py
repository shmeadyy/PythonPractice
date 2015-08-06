#prompt user for start of game
#user guesses once
#test the guess against the number it should be
#if not the guess then allow to guess again
#if it is, break and finish game

import random

rand_num = random.randint(1,10)

def game():
	i = 6
	while i > 0:
		# prompt user for input
		user_guess = raw_input("Enter a number: ")
		if guess(user_guess) == True:
			break
		elif guess(user_guess) == False:
			i -= 1
			print("Sorry, that's incorrect.  You have {} more guesses.".format(i))
		else:
			print("Oops, that's not valid input.  Try again.")
	print("That's it, folks!  The random number was {}.  But give this game another try why don't ya?".format(rand_num))

			

def guess(guessed_number):
	if int(guessed_number) == rand_num:
		print("You guessed correctly!  The random number is {}.  Good job!".format(rand_num))
		return True
	else:
		return False

print("Hey there! Let's play a game! You have 5 chances to guess a number between 1 and 10.  Let's go:")
game()