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

player = int(playerchoice)  # as input is stored a string
# so we casted it as an integer

if player < 1 or player > 3:
    sys.exit("You must enter 1,2 or 3.")
    # print("You must enter 1,2 or 3.") #  we have to exit and give the message to the user so imported sys

# computerchoice = random.choice("123")  # select one of them randomly  #method1
computerchoice = random.randint(1, 3)  # select one of them randomly

# computer = int(computerchoice)  #method1
computer = computerchoice


print("")  # print empty line

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
