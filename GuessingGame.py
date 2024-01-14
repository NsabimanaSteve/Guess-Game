import random

def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    print("Welcome to the Guessing Game!")
    print("I’m thinking of a number between 1 and 100. Can you guess it?")
    
    # Initialize variables
    guess = 0
    attempts = 0
    
    while guess != secret_number:
        guess = int(input("Guess: "))
        attempts += 1

        if guess < secret_number:
            print("Good try, but that’s too low. Try again.")
        elif guess > secret_number:
            print("Good try, but that’s too high. Try again.")

    print(f"Yes! You guessed correctly after {attempts} tries! Congratulations.")

# Run the game
guessing_game()
