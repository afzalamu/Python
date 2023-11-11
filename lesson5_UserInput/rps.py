import random
import sys
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# print(RPS(2))
# print(RPS.ROCK)
# print(RPS["ROCK"])
# print(RPS.ROCK.value)
# sys.exit()

# Rock paper and scissor

# # value = input('message to the user')
# value = input("Please enter the value\n")
# print(value)


# --------------------------------------------------
# making of Rock Paper Scissor game

print("")
playerchoice = input(
    "Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissor\n\n"
)  # coices for rock paper or scissors

player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit("You must enter 1,2 or 3.")
    # print("You must enter 1,2 or 3.") #  we have to exit and give the message to the user so imported sys

computerchoice = random.choice("123")  # select one of them randomly

computer = int(computerchoice)
print("")
print("You chose" + " " + str(RPS(player)).replace("RPS.", "") + ("."))
print("Python chose" + " " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")

if player == 1 and computer == 3:
    print("🙌you wins")
elif player == 2 and computer == 1:
    print("🙌you wins")
elif player == 3 and computer == 2:
    print("🙌you wins")
elif player == computer:
    print("😲tie game")
else:
    print("🐍python won")
