import random

user_input = raw_input("Enter your roll: ")

def parse_dice_roll(user_dice_roll):
    """ Takes the user input and parses out the number of dice to be rolled
    and how many sides the dice have, and also takes in account any modifiers. """
    try:
        quantity_of_dice, dice_and_mod_string = user_dice_roll.split('d')
        quantity_of_dice = int(quantity_of_dice)
        number_of_sides = int(number_of_sides)
        print_rolls(quantity_of_dice, number_of_sides)
    except ValueError:
        print "Please type in rolls in the format '1d6'."

def print_rolls(quantity_of_dice, number_of_sides):
    for x in range(quantity_of_dice - 1):
        print "%d +" % random.randint(1,number_of_sides),
    print "%d" % random.randint(1,number_of_sides)

def parse_dice_and_modifier():


parse_dice_roll(user_input)
