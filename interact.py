
class colors:
	black='\033[30m'
	red='\033[31m'
	green='\033[32m'
	orange='\033[33m'
	blue='\033[34m'
	purple='\033[35m'
	cyan='\033[36m'
	lightgrey='\033[37m'
	darkgrey='\033[90m'
	lightred='\033[91m'
	lightgreen='\033[92m'
	yellow='\033[93m'
	lightblue='\033[94m'
	pink='\033[95m'
	lightcyan='\033[96m'





# ------------------------------------HangMan Wrong Answer Prints-----------------------

def head():
	print(colors.red,'______________________1/6 Wrong So Far_________')
	print(colors.green,' O\n\n\n')
	print(colors.red,'______________________Try again________________')

def body():
	print(colors.red,'______________________2/6 Wrong So Far_________')
	print(colors.green,' O')
	print(colors.green,' |\n\n')
	print(colors.red,'______________________Try again________________')


def left_arm():
	print(colors.red,'______________________3/6 Wrong So Far_________')
	print(colors.green,' O')
	print(colors.green,'\|')
	print(colors.green,' |\n')
	print(colors.red,'______________________Try again________________')


def right_arm():
	print(colors.red,'______________________4/6 Wrong So Far_________')
	print(colors.green,' O')
	print(colors.green,'\|/')
	print(colors.green,' |\n')
	print(colors.red,'______________________Try again________________')


def left_leg():
	print(colors.red,'______________________5/6 Wrong So Far_________')
	print(colors.green,' O')
	print(colors.green,'\|/')
	print(colors.green,' |')
	print(colors.green,'/ ')
	print(colors.red,'______________________Try again________________')

	
def right_leg():
	print(colors.red,'______________________Sorry....________________')
	print(colors.lightcyan,'______________________6/6 Wrong________________')
	print(colors.purple,' O')
	print(colors.purple,'\|/')
	print(colors.purple,' |')
	print(colors.purple,'/ \\')
	print(colors.red,'______________________Sorry You Lost___________')



# IF USER IS GETTING WRONG ANSWERS PRINT THE RELEVANT L STAGES ABOVE AN CONTINUE
def wrong_answer(l):
    # written like this(no parentheses) to prevent all functions being called
	lost_spots = [head, body, left_arm, right_arm, left_leg,right_leg]
    # called like this to prevent the rest of the functions being called
	lost_spots[l]() 
	
		
# ------------------------------------HangMan Wrong Answer Prints-----------------------




# IF USER WON THE GAME
# takes the hidden word as an arguement
def won_game(word):
	print(colors.lightgreen,'______________________GOOD JOB!!!________________')
	print(colors.blue,' /\/\/\///\/\///\\\\\///\//\/\\/\/\\/\/\/\/\/\/\/')
	print(colors.blue,'\|/\\//\/\\/\/\//\/\\\/\/\/\/\/\/\/\//\\\\\\////\/\\')
	print(colors.blue,f' /\/\///\/\// HIDDEN WORD: {word} \\/\/\//\/\/')
	print(colors.blue,' /\/\/\///\/\///\\\\\///\//\/\\/\/\\/\/\/\/\/\/\/')
	print(colors.blue,'\|/\\//\/\\/\/\//\/\\\/\/\/\/\/\/\/\//\\\\\\////\/\\')
	print(colors.lightgreen,'______________________YOU WON!!!_________________')


# ask to play again
# patience is a global variable, run global statement in function to determine this fact within that scope
# pass the game function in as and argument/call back
patience = 0
def wanna_play_again(game):
	global patience

	# color control
	print(colors.cyan)

		
	# ask user to play again
	play_again = input('Want To Play Again?? Yes(y) or No(n) \n')

	if 'y' in play_again.lower():
		# playing again
		return game()

	elif 'n' in play_again.lower():
		# color control
		print(colors.red)
		# ending the game
		print('Ending Game...')
		return False

	elif patience == 4:
		# color control
		print(colors.purple)
		# too many answers (not programmed to understand)
		print('Ok idk what your saying but...you know where to find me.')
		return False
	else:
		# patience goes up...lets ask again lol
		patience += 1
		return wanna_play_again(game)







# FINDING OUT THE TYPE OF GUESS TO DO (LETTER OR WORD)--------------------------------------------------------------TYPE OF GUESS

# type of guess
def ask_4_guess_type():

	#color control 
	print(colors.blue)

	# ask user for the type of guess
	type_of_guess = input('Are You guessing a letter or word?  letter(L) or word(W)')
	

	# if its a letter, return true
	if 'l' == type_of_guess.lower():
		return True
	# if its a word, return false
	elif 'w' == type_of_guess.lower():
		return False

	# at worst ask again
	return ask_4_guess_type()

# FINDING OUT THE TYPE OF GUESS TO DO (LETTER OR WORD)--------------------------------------------------------------TYPE OF GUESS






# ASKING FOR A GUESS THAT WILL BE A WORD-------------------------------------------------------------------------------WORD GUESS 


# word guess
def ask_4_word_guess():
	# color control
	print(colors.yellow)

	# ask user for there word guess
	word_guess = input('Whats the word? \n')

	# make sure the word only has letters in it 
	# using .isalpha()
	if word_guess.isalpha():
		return word_guess


	# at worst ask again
	return ask_4_word_guess()

# ASKING FOR A GUESS THAT WILL BE A WORD-------------------------------------------------------------------------------WORD GUESS 




# ASKING FOR A GUESS THAT WILL ONLY BE A LETTER-----------------------------------------------------------------------LETTER GUESS
def ask_4_letter_guess(word_spaces):

	# color control
	print(colors.yellow)
	# ask user for there letter guess
	letter_guess = input('Guess a letter? \n')


	# make sure its a letter and only 1 character
	# if not, then let this code run to ask again (the return at the bottom)
	if letter_guess.isalpha() and len(letter_guess) == 1:

		# after input is valid
		# check if user already guessed this right
		if letter_guess in " ".join(word_spaces):
			print(colors.red,'You already guessed this letter right...')
			# let code run to ask again
		else:
			# return guess value
			return letter_guess


	# at worst asking again
	return ask_4_letter_guess()


# ASKING FOR A GUESS THAT WILL ONLY BE A LETTER-----------------------------------------------------------------------LETTER GUESS




# CONTINUE TO HANGMAN.PY