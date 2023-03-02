# Hl component 5 = no duplicates

# To Do
# Set up empty list called already_guessed
# when user guesses, add guess tp list
# for each guess, check that number is not already_guessed

# HL component 5 = Prevents duplicate guesses

SECRET = 7
GUESSES_ALLOWED = 5

already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))   # replace this with function

    # check that guess is not a duplicate
    if guess in already_guessed:
        print("You already guessed that number! please try again "
              "you *still* have {} guesses left".format(guesses_left)
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    if guesses_left >= 1:

        if guess < SECRET:
            print("Too low, try a higher number. Guesses left: ")

        elif guess > SECRET:
            print("Too high, try a lower number. Guesses left: ")
    else:
        if guess < SECRET:
            print("Too low!")
        elif guess > SECRET:
            print("To high!")

if guess == SECRET:
    if guesses_left == GUESSES_ALLOWED
        print("Amazing! You got it ")
    else:
        print("well done, you got it")

