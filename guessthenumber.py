import random

def guess_the_number():
    print("Welcome to Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Set the number of attempts
    attempts = 10
    
    # Start the guessing loop
    while attempts > 0:
        try:
            # Ask the player to make a guess
            guess = int(input(f"You have {attempts} attempts left. Make a guess: "))
            
            # Check if the guess is correct
            if guess == number_to_guess:
                print("Congratulations! You guessed the number correctly!")
                break
            elif guess < number_to_guess:
                print("Too low!")
            else:
                print("Too high!")
            
            # Decrease the number of attempts
            attempts -= 1
            
        except ValueError:
            print("Please enter a valid number.")
    
    # If player runs out of attempts
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")
        print("You LOSE!")
# Run the game
guess_the_number()
