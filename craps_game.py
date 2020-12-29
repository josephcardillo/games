"""Script to play craps"""
"""Rules:
- Roll two six-sided dice, each with faces containing 1 to 6 spots
- Calculate the sum of the spots on the two upward faces
- If the sum is 7 or 11 on the first roll, you win
- If the sum is 2, 3 or 12 on the first roll (called 'craps'), you lose
- If the sum is 4, 5, 6, 8, 9 or 10 on the first roll, that sum becomes your 'point'
- To win, you must continue rolling the dice until you 'make your point' (i.e., roll that same point
- You lose by rolling a 7 before making your point"""

import random

def roll_dice():
    """Rolls two dice and returns value between 1 and 6"""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2) # packs rolls into a tuple

def roll_sum(dice):
    """Calculates sum of the dice roll"""
    die1, die2 = dice # unpack the tuple into die1 and die2 variables
    return (sum(dice))

first_roll = roll_dice()
face_value = roll_sum(first_roll)
print(f"You rolled: {face_value}.")

if face_value in (7, 11):
    # When defining a variabled within an if statement, the local scope becomes global. So it's necessary here to define game_status so that the while loop works.
    game_status = "WON"
    print("You win!")
elif face_value in (2, 3, 12):
    game_status = "LOSE"
    print("You lose... crap!")
else:
    game_status = "CONTINUE"
    point = face_value

while game_status == "CONTINUE":
    # This will continue rolling until the game status changes to WIN or LOSE.
    next_roll = roll_dice()
    face_value = roll_sum(next_roll)
    if face_value == 7:
        print(f"You rolled {face_value}.")
        game_status = "LOSE"
        print("You lose... crap!")
    elif face_value == point:
        print(f"You rolled {face_value}.")
        game_status = "WIN"
        print("You win!")
    else:
        print(f"You rolled {face_value}. Roll again.")






