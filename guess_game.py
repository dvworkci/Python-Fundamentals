# Guess game in python
# secret_word = "python"
# guess = ""
# i = 0

# while(i <= 5):
#     i += 1
#     if(i > 5):
#         print("You lose")
#         break
#     else:
#         guess = input("Enter guess: ")
#         if(guess == secret_word):
#             print("You win!")
#             break

secretWord = "python"
guess = ""
guessCount = 0
guessLimit = 5
outOfGuesses = False

while(guess != secretWord and not(outOfGuesses)):
    if(guessCount < guessLimit):
        guess = input("Enter guess: ")
        guessCount += 1
    else:
        outOfGuesses = True

if(outOfGuesses):
    print("Out of guess, you lose!")
else:
    print("Correct! You Won!")