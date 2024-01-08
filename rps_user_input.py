import sys
import random
from enum import Enum

# Taking user input syntax
"""
value = input('Please enter a value : \n')
# print(value)
playerchoice = input("Enter .. \n 1 for Rock,\n 2 for Paper or \n 3 for Scissors: \n \n")
player =int(playerchoice) # casting str into int
if player <1 or player>3:
     sys.exit("You must enter 1,2 or 3 .") # to exit the program after invalid choice
"""
#Data Type enum to assign constant value
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
print("")
playerchoice = input(
    "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

player = int(playerchoice)

# if player < 1 | player > 3:
if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.") # sys.exit to exit the program after wrong input

computerchoice = random.choice("123")  # Random function to generate random numbers
computer = int(computerchoice)
print("")
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")  # str to type cast int variable player into str as print o/p is string
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")  # Replace method to remove RPS.paper input to simply paper
print("")
if player == 1 and computer == 3:
    print("🎉 You win!")
elif player == 2 and computer == 1:
    print("🎉 You win!")
elif player == 3 and computer == 2:
    print("🎉 You win!")
elif player == computer:
    print("😲 Tie game!")
else:
    print("🐍 Python wins!")