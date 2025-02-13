import random
# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")
# comRandChoise = random.randint(1, 100)
# choise = input("Choose the deficulty. Type 'easy' or 'hard':").lower()
# gameOver = False
# while not gameOver:
#     if choise == "easy":
#         level = 10
#     elif choise == "hard":
#         level = 5
#     else:
#         print("Invalid choice. Please restart the game.")
#         break

#     while level > 0:
#         print(f"You have {level} attempts remaining.")
#         userGuess = int(input("Make a guess: "))
#         if comRandChoise == userGuess:
#             print(f"You Won! {userGuess} is the correct guess.")
#             gameOver = True
#             break
#         elif comRandChoise > userGuess:
#             print("Too low.")
#         elif comRandChoise < userGuess:
#             print("Too high.")
#         level -= 1

#     if level == 0:
#         print("You've run out of guesses. Game over.")
#         gameOver = True


# print(comRandChoise)

#using functions#

easyLevel = 10
hardLevel = 5
turns = 0
def check(userGuess, actualAns, turns):
    if userGuess > actualAns:
        print("To high")
        return turns - 1
    elif userGuess < actualAns:
        print("To low")
        return turns - 1
    else:
        print("You won!")

def difficulty():
    level = input("'easy' or 'hard'").lower()
    if level == 'easy':
        return easyLevel
    else:
        return hardLevel
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    comRandChoise = random.randint(1, 100)
    print(f"The correct ans is {comRandChoise}")

    turns = difficulty()
    guess = 0
    while guess != comRandChoise:
        print(f"you have {turns} attempts left.")
        guess = int(input("Make a guess"))
        turns = check(guess, comRandChoise, turns)
        if turns == 0:
            print("You have lost the game.")
            break
game()  