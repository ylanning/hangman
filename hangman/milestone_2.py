import random

# Create a list containing the names of your 5 favorite fruits
my_fruits = ["mango", "banana", "orange", "grapes", "papaya"]

# Assign this list to a variable called word_list.
world_list = my_fruits

# Print out the newly created list to the standard output (screen).
# print(world_list)

# Create the random.choice method and pass the word_list variable into the choice method.
def choices(elements):
    word = random.choice(elements)
    return word 

word1 = choices(world_list)
word2 = choices(world_list)
word3 = choices(world_list)

# print(word1)
# print(word2)
# print(word3)

# Ask user choices 
def ask_user(elements):
    for element in elements:
        print(element)
    guess = input("Select your choice of fruit from the list:  ")
    if len(guess) >= 1 and guess.isalpha():     
        print(f"Well done!! you select {guess}")
    else:
        print("Ooops! you entered an invalid input")

ask_user(world_list)