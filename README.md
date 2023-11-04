# Hangman
### Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

### This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

![alt text](hangman_image.jpg)

**Installation instructions:** Open the milestone_5.py file and run the code as you would normally run any Python code (the code is made so that it runs the Hangman class by calling play_game(word_list) function).

**Usage instructions:** The computer picks a random word (from a hidden list of words) and then asks for a user to guess a letter of that word. The computer will inform the user if the picked letter is in the word. If the guessed letter is not in the word, computer will also inform the player of how many lives (or guesses) the player has left. If the user enters an invalid input (containing a symbol not in alphabetical order or containing more than one letter), the computer will keep asking for the user to enter a valid input until one is received. Each correct guessed letter replaces an underscore (representing hidden letter) in word_guessed variable and then the variable is printed back to the player.The player wins if he/she guesses the word before running out of 5 lives. 


**File structure of the project:** A Hangman class and a play_game(word_list) function is built to capture the game. It contains attributes: word_list (a hidden list from which computer picks a random word), num_lives (number of wrong guesses the player is allowed to have before the game ends), word (the word picked by the computer), word_guessed (instance that stores the correct guessed letter by the player), num_letters (number of unique letters in the secret word), list_of_guesses (list where all the guessed letters by the player are stored) and guess (where a letter guessed by the user is temporarily stored). The mentioned attributes then are used in two methods check_guess() (where it is checked whether the user input value is valid) and ask_for_input() (where it asks the user to guess the letter and the letter is checked against the secret word). Finally a play_game(word_list) function is created which main purpose is to activate the game and continue running it until all the missing letters are guessed (and the game is won) or until the player has used up all the lives before being able to guess the secret word (and the game is lost).


**License information:** No license present.
