import random


class Hangman:
    def __init__(self, word_list=[], num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = ""
        self.word_guessed = ['_', '_', '_', '_', '_']
        self.num_letters = 0
        self.list_of_guesses = list()
    
    def check_guess(self, guess):
          guess = guess.lower()
          if guess.isalpha():
              print(f"Good guess, {guess} is in the word!")
              for letter in self.word:
                  if letter == guess:
                      for i,word in self.list_of_guesses:
                          self.list_of_guesses[0] = letter
                  else:
                      self.num_lives -= 1
                      print(f"Sorry, {letter} is not in the word")
                      print(f"You have {self.num_lives} lives left")
                            
              self.num_letters -= 1
                          
    def ask_for_input(self):
        while True:
            guess = input("Please guess and type a letter ....  ")
            if not guess.isalpha():
                print("Invalid letter, Please enter a single alphabetical character!") 
            elif guess in self.list_of_guesses:
                print("You have already tried that letter, try again! ")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

test_hangman = Hangman()
test_hangman.ask_for_input()
    
        