import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Try to guess the number!")

    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            # Get user input
            guess = int(input("Enter your guess: "))
            attempts += 1  # Increment attempt count

            # Check the guess
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
                guessed_correctly = True
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

# Run the game
guessing_game()
