import random

user_input = raw_input("Enter your roll: ")

def parse_dice_roll(user_dice_roll):
    """ Takes the user input and parses out the number of dice to be rolled
    and how many sides the dice have, and also takes in account any modifiers. """
    try:
        quantity_of_dice, dice_and_mod_string = user_dice_roll.split('d')
        quantity_of_dice = int(quantity_of_dice)
        number_of_sides, mod_sign = parse_dice_and_modifier(dice_and_mod_string)
        print_rolls(quantity_of_dice, number_of_sides)
    except ValueError:
        print "Please type in rolls in the format '1d6'."

def add_rolls_and_mod(quantity_of_dice, number_of_sides):
    rolls = []
    for x in range(quantity_of_dice):
        rolls.append(random.randint(1,number_of_sides))
    return rolls

def print_rolls(quantity_of_dice, number_of_sides):
    for x in range(quantity_of_dice - 1):
        print "%d +" % random.randint(1,number_of_sides),
    print "%d" % random.randint(1,number_of_sides)

def parse_dice_and_modifier(dice_mod_string):
    num_sides, mod_string = dice_mod_string.split()
    num_sides = int(num_sides)
    mod_sign = mod_string[0]
    modifier = mod_string[1]
    return num_sides, mod_sign, modifier

parse_dice_roll(user_input)
