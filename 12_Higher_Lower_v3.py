# random import

# play instructions
def instructions():
    print("for each game you will be asked to...")
    print()
    print("- Enter a 'low' and 'high' number."
          "The computer will randomly generate a"
          "'secret' number between you two chosen numbers."
          "It will use these numbers for all"
          "the rounds in a given game.")
    print()
    print("- The computer will calculate how many guesses you are allowed"
          "- enter the number of rounds you want to play"
          "- guess the secret number")

    print("Good Luck!")


play = input("press <Enter> to begin...").lower()

# If they press <Enter>, output 'program continues'
print("please answer yes / no")
