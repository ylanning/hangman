import random


class Hangman:
    
    def __init__(self, word_list=[], num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = ''
        self.word_guessed = []
        self.num_letters = 0
        self.list_of_guesses = list()
    
    def check_guess(self, guess):
        # convert the user input to lower case
        guess.lower()  
 
        # check if the guess is in self.word
        if guess in self.word:
            print(f"Good guess, {guess} is in the word!")
            self.word_guessed = ['_'] * len(self.word)
            print("self word guess", self.word_guessed)
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            print("self word guesses" , self.word_guessed)
                
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} lives left")      
            return self.num_lives
              
        self.num_letters -= 1
        print("word guess", self.word_guessed)
        print("Total num letters", self.num_letters)
        return self.num_letters
              
    def ask_for_input(self):
        
        self.word = ''.join(random.choices(self.word_list))
        self.num_letters = len(self.word)
        
        while True:
            # ask the user to guess a letter and assign to var guess
            guess = input("Please guess and type a letter ....  ")
            
            # check if guess input is valid alphabetically, throw error if it's invalid
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter, Please enter a single alphabetical character!") 
            # check if the input is already guessed before
            elif guess in self.list_of_guesses:
                print("You have already tried that letter, try again! ")
            # all good, call check guess function
            else:
                self.check_guess(guess)
                # add guess word to list of guesses
                self.list_of_guesses.append(guess)
                if self.num_lives == 0:
                    break
                elif self.num_lives != 0 and self.num_letters > 0:
                    break
                    

    @classmethod
    def play_game(cls, word_list=[]):
        num_lives = 5
        game = Hangman(word_list, num_lives)
        
        while True:
            if game.num_lives == 0:
                print("You Lost!!")
                print(f"the word is : {game.word}")
                break
            elif game.num_lives > 0:
                print("total num lives ", game.num_lives)
                game.ask_for_input()
            elif game.num_lives != 0 and game.num_letters > 0:
                print("Congratulations. You won the game!")
                break
                
list_words = ['apple', 'elephant', 'airplane', 'pineaple', 'computer', 'zebra', 'house', 'garden']
test_hangman = Hangman()
test_hangman.play_game(list_words)