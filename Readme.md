# Learning Python With Projects (Hang Man) 
> Syntax - Comments, Prints, Variables, Strings, Integers, String Concatenations, Inputs, Comparison operators, Random(module), Functions, If/Else statements. For loops, and List(arrays).

> https://youtu.be/odrbNYA0r7A

___

## Tutorial
	    
#### test1.py file

> List - :
* list is a built-in 'collections' data type in python used to store multiple values in 1 variable.
* Created with square brackets []
* each value should be separated with commas
* you can store all data types within a list (string,integer,function,etc.)
* you can add values to it upon creation or with the 'append' attribute

```python
# make a list with 3 numbers
array = [1,2,3]

# add 3 more numbers to it
array.append(4)
array.append(5)
array.append(6)


```

* More onlist here (https://docs.python.org/3/tutorial/datastructures.html)
___

> More on Random (Module) - :	
* We will be using the 'choice' attribute in this module to pick a random value choice in any list we pass into it as an arguement.

```python
# bring in the module
import random


# make a function named 'show_num' that takes an arguement(param) name 'num' and in this function, print num
def show_num(num):
	print(num)

# make a list with 3 numbers in it and save it to a variable named 'my_nums'
my_nums = [12,33,5]

# make a list named 'actions' with 2 values in it. 'my_nums' variable 1st and the'show_num' function 2nd . Remember to add the functions name alone and not the parameters ().
actions = [my_nums,show_num]

# call the 'show_num' function through the 'actions' list and pass in a random choice from the 'my_nums' list but used actions to reference the 'my_nums' list
actions[1](random.choice(actions[0]))
```
___

#### test2.py file

> For loops - :
* A method used to iterate over a sequence (a list,tuple,set,dict, and/or string). 
* This is looping through each value within them
* This can cause you to execute code to manipulate each value within them



```python
# make a list with 5 values of your choice
valz = [2323,5,35,'ok',44,'yoooo',44422,65535]

# make a loop that iterates through the list and just print each value
for val in valz:
	# show current value
	print(val)


# make a list with 3 numbers
valz = [2323,5,35]

# make a loop that iterates through the list and print numbers lower than 50
for val in valz:
	# show current value if lower than 50
	if val < 50:
		print(val)

```
___


___

> # Hang Man Project - Follow and apply each step.
  

### interact.py
```python
'''
1.) Create functions(3 or 1) asking users for the type(1) of guess and a letter(2) or word(3) guess


2.) Create a function that prints out your wrong answer message


3.)Create a function that gives a Winning message


4.)Create a function that ends game and ask users to play again


'''

```

___

### hangman.py

```python 


''' 1.) I Created the hangman stages for us using prints. 
We will be calling them in each function, based on how many wrong answers there are.'''


# 2.) Make a list of as much words you can think of and save it to a variable


# 3.) Create a 'game' function and from here ramain within this scope
	# 3-a.) Make your top variables 
			# - 'wrong_count' to keep track of wrong answers (int)
			# - 'word' variable us random module, to pick a random word from the word list (str)
			# - 'word_spaces' to keep track of blank spaces in the word the user will need to guess right (list of str)
	
	# 3-b.)Create a 'ask_4_guess' function that takes 'wrong_count' as the arguement/param.
			# if/else statement 1
			# - If the 'ask_4_guess_type' function returns True....
				# *ask for a letter guess. len(1)-.isalpha()
				# *check if the guess was already guessed right
				# *add 1 to your 'wrong_count' variable every wrong answer


			# - else the 'ask_4_guess_type' function returned False so....
				# *ask for a word guess. len(n>1)-.isalpha()
				# *check if the guess is right
				# *add 1 to your 'wrong_count' variable every wrong answer

			# if/else statement 2 
			# (needs to be below 1st is/else)
			
			# - if 'wrong_count' == 5 (or whatever the max wrong answers number is that you use)...
				# *end the game and ask to play again

			# - elif '_' is in the 'word_spaces' list...
				# *call this function again(ask_4_guess)and pass in the 'wrong_count' variable to keep count.

			# - else the game should be a win....
				# *send a nice winning message and ask to play again





```


### Run your app
```bash
python hangman.py
```
___


> *CONGRATS YOU JUST PROGRAMMED A Hang Man GAME IN PYTHON*
---
> *SEE HOW FAR YOU CAN GO AND SHARE IN THE COMMENTS*


### Thanks For Reading 
