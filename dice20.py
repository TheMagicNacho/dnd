import random
import sys

def main():
    while True:
        prompt_user()

def prompt_user():

    try:
        SIDES = input("How many sides? ")
        XSIDE = int(SIDES)
    except:
        SIDES = input("How many sides? [MUST BE A NUMBER] ")
        XSIDE = int(SIDES)

    try:
        MOD = input("Modifying number (enter 0 for no)? ")
        XMOD = int(MOD)
    except:
        MOD = input("Modifying number (enter 0 for no)? [MUST BE A NUMBER] ")
        XMOD = int(MOD)

    DICE_ROLL = random.randint(1, XSIDE)

    ONE = DICE_ROLL + XMOD

    print("You rolled:", DICE_ROLL)
    print("You modified by:", XMOD)
    print("\n")
    print("YOUR FINAL IS:", ONE)
    ROLL_AGAIN = input("Roll again! (Or else type 'n' to quit)\n ")

    if ROLL_AGAIN.lower() == "n":
        exit()

if __name__ == '__main__': main()
