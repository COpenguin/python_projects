import random
from art import logo

#Global Variables
game_lives = 0
guessing = True

#Guessing function
def guess_number(guess):
    global guessing
    if guess == cpu_guess:
        print("You win!")
        guessing = False
    elif guess < cpu_guess:
        print("Too Low\nGuess again!")
        take_life()
    elif guess > cpu_guess:
        print("Too High\nGuess again!")
        take_life()

#Taking Life function
def take_life():
    global guessing
    global game_lives
    game_lives -= 1
    print(f"You have {game_lives} attempts remaining:")
    if game_lives == 0:
        print(f"Game over: The number was {cpu_guess}")
        guessing = False


#Starting Screen
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100")

#Grabbing ranndom number for CPU
cpu_guess = random.randint(0, 100)

#Difficulty selector. If this was my main project and not a daily project. I would create better limits for user inputs
difficulty = input("Choose your difficulty: Easy or Hard: ").lower()
if difficulty == "easy":
    game_lives = 10
    print(f"You have {game_lives} lives remaining")
else:
    game_lives = 5
    print(f"You have {game_lives} lives remaining")

#Guessing loop
while guessing:
    player_guess = int(input("Make a guess: "))
    guess_number(player_guess)

#End of day project. If I ever come back, will like to create a loop to continue game.


