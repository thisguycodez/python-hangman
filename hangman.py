import random
from interact import *




# intro....

print(colors.yellow,'________________________ThisGuyCodez_________')
print(colors.green,' O')
print(colors.green,'\|/')
print(colors.green,' |')
print(colors.green,'/ \\')
print(colors.lightred,'_____________________________________________')
print(colors.orange,'__Python__HangMan_Terminal_Game______________')
print(colors.purple,'_____________________________________________')





# random names list

words = ["Sachmo","Waterfall", "Pineapple", "Island" , "Roswell", "Locksmith"]



# game scope
def game():
	#color control 
	print(colors.orange)


	# WORNG ANSWER COUNT. if reaches 6(5 in code) then its game over.
	wrong_count = -1
	

	# get the word that needs to be guessed
	word = random.choice(words)

	# creates a _ space for each letter into an array then joined as a string
	# Also a list of the empty spaces to be filled
	word_spaces = ['_' for char in word]

	print('Guess 1 letter or you can guess the word...')
	print(f"It's a {len(word)} letter word: ", " ".join(word_spaces))


	# this should continue until all spaces 
	# are filled or the deadman is all there

	def ask_4_guess(wrong_count):
		# color control
		print(colors.yellow)

		# first if/else-------------------------------------------------------running main prompts--------------------------------------------1
		
		# if true then its a letter they're guessing
		if ask_4_guess_type():
			# grab the letter
			guess = ask_4_letter_guess(word_spaces)


			# keep track whether or not the letter was found in there
			found = False



			# check if the letter is in the hidden word
			# if so then the letter should fill all the spots it is in
			for l in range(len(word)):
				# if word[l] is the users letter guess
				if word[l].lower() == guess.lower():
					# then the same exact iteration spot in 'word_spaces'
					# should == the letter 
					word_spaces[l] = guess

					# let it be known the letter was found
					found = True

			# if letter was not found, add 1 to wrong_count
			if found == False:
				# add 1 to wrong count
				wrong_count = wrong_count+1
				# print the relevant
				wrong_answer(wrong_count)



		# if false then its a word they're guessing
		else:
			# grab the word
			guess = ask_4_word_guess()

			# see if the word matches
			if guess.lower() == word.lower():
				won_game(word)
				return wanna_play_again(game)
			# if word does not match, add 1 to wrong_count
			else:
				wrong_count = wrong_count+1
				# print the relevant
				wrong_answer(wrong_count)
		
		# first if/else-------------------------------------------------------running main prompts--------------------------------------------1



		# second if/else-----------------------------------------------Games Current Result--------------------------------------------------2
		# color control
		print(colors.yellow)
		print("Progress So Far: ", " ".join(word_spaces))

		''' 
		logic....

		- if the user ran out of chances to guess then the game should end....

		- if there are still blank spots then continue the game or it should be a win
		'''
		# did user run out of guess chances 6(5 in code)
		if wrong_count == 5:
			# GAME LOST
			# ask to play again
			return wanna_play_again(game)
		
		# if there are still blank spaces
		elif '_' in " ".join(word_spaces):
			# then continue
			return ask_4_guess(wrong_count)

		# the game is over (user won)
		else:
			# GAME WON
			# print the winning msg
			won_game(word)
			# ask to play again
			return wanna_play_again(game)

		# second if/else-----------------------------------------------Games Current Result--------------------------------------------------2
	



	# run prompt loop
	return ask_4_guess(wrong_count)




	
# run game
game()