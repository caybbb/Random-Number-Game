import random
quit_words = ["q","quit", "no", "break"]
difficulty_options = [1, 2, 3]

while True:
    attempts = 0
    randomnum = random.randrange(0, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of  a number between 1 and 100.")
    print("You have 5 chances to guess the correct number.\n\n")
    trys = None

    print("Please select the difficulty level: \n 1. Easy (10 chances)\n 2. Medium (5 chances)\n 3. Hard (3 chances\n")
    
    while True:
        try:
            difficulty = int(input("Enter your choice: "))
        except ValueError:
            print("You have to choose from the given nubmers!")

        if difficulty not in difficulty_options:
            print("You must select from the three options!\n")
        elif difficulty == 1:
            print("\nGreat! You have selected the Easy difficulty level.")
            print("Let's start the game!")
            trys = 10
            break
        elif difficulty == 2:
            print("\nGreat! You have selected the Medium difficulty level.")
            print("Let's start the game!")
            trys = 5
            break
        elif difficulty == 3:
            print("\nGreat! You have selected the Hard difficulty level.")
            print("Let's start the game!\n")
            trys = 3
            break
    
    while trys != 0:
        guess = int(input("\nEnter your guess: "))
        attempts += 1
        trys = trys - 1
        if randomnum < guess:
            print(f"Incorrect! The number is less than {guess}\n")
        elif randomnum > guess:
            print(f"Incorrect! The number is greater than {guess}\n") 
        elif randomnum == guess:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.\n")
            break

    if trys == 0 and randomnum != guess:
        print(f"Sorry, you have ran out of trys! The correct number was {randomnum}.\n")

    continueInput = input("Would you like to keep playing? ")
    if continueInput.lower() in quit_words:
        break
    else:
        continue
