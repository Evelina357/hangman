# %%
import random

word_list = ["banana", "kiwi", "grapes", "pineapple", "clementines"]
word = random.choice(word_list)

# %%
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        
def ask_for_input():
    guess = input ("Please enter a single letter: ")
    while len(guess) != 1 or guess.isalpha() != True:
        guess = input("Invalid letter. Please enter a single alphabetical letter: ")
    check_guess(guess)
    
ask_for_input()
# %%
