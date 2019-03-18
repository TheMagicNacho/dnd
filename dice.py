""" Dice Roller V1 - 20190314 """
import random
import sys

def main():
    while True:
        prompt_user()

def prompt_user():
# grab user deffinitions
    try:
        dice_number = input("How many dice? [default 1] ")
        xdice_number = int(dice_number)
    except:
        xdice_number = int(1)

    try:
        sides = input("How many sides? [default 20] ")
        xside = int(sides)
    except:
        xside = int(20)

    try:
        mod = input("modifying number? ['enter' for no modifyer] ")
        xmod = int(mod)
    except:
        xmod = int(0)

# generate adaptive list of dice rolls from user
    roll_list = []
    for i in range(xdice_number):
        roll_list.append(random.randint(1, xside))  # append to our_list

# conduct required math
    final = sum(roll_list) + xmod

# Print the outputs
    print("You rolled:", roll_list )
    print("You modified by:", xmod)
    print("\n")
    print("YOUR FINAL IS:", final)

# Keep the fun going or pussy out
    again = input("Roll again! (Or else type 'n' to quit)\n ")

    if again.lower() == "n":
        exit()

if __name__ == '__main__': main()
