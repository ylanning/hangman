# Task 1
def check_guess(guess):
    """ Check the user input is a valid letter 
    Args:
        string representation of user input
    Returns:
        _type_: "str"
    """
    guess = guess.lower()  
    while True:
        if guess.isalpha():
            print(f"You typed {guess}!")
            return guess
        else:
            print("Invalid input, please try again ...")
            
# Task 2
import random
# Create a list of secrect words
secret_words = ['apple', 'elephant', 'airplane', 'pineaple', 'computer', 'zebra', 'house', 'garden']

def ask_for_input():
    """ Ask guess to type any letter.
        validate the input is the a valid letter by passing to check_guess function.
        randomly select any word from the list of secret words
        check if user input is contained in secret word.
        example 'a' is in 'apple'
    """
    while True:
        guess = input('Please type any letter ....:  ')
        guess_input = check_guess(guess)
        # Generating random word from secret word from the list
        secret_word = random.choice(secret_words)
        # Check if the input it valid letter and is contained in secret word
        if guess_input.isalpha() and guess_input in secret_word:
            print("Congratulations!, you picked the correct letter ...")
            print(f"Secret word is {secret_word}")
            break
        else:
            print("Sorry your guess is not in our secret word, try again! ..")
            print(f"Secret word is {secret_word}")
     
# Call the function
ask_for_input()