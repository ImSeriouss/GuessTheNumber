# importing the random module
import random

# inputting the random number
print("Welcome to the Guess The Number game! MADE BY IMSERIOUSS")
x = input("Please guess a number in the range of 1 to 10: " )

# assigning a variable to the random module
y = random.randrange(1, 10)

# applying logic and other stuff
try:
    x = int(x)
    if x == y:
        print("You guessed the right number! The number was", y)
    else:
        print("Wrong! The number was", y)
except:
    print("It must be a number! Please restart this program.")
k = input("Press ENTER to close the program.")