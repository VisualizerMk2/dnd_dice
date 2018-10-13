import random
import re

user_input = raw_input("Enter your roll: ")

def check_input_format(user_dice_roll):
    """ Takes the user input and matches it against a regex. 
    Incorrectly formatted rolls will generate an error message.

    Input: A string of the user's inputted dice roll.
    Output: The regex match object with to be used in generating the dice rolls. """
    #Regex: The order goes: at least one digit -> 'd' char -> at least one digit ->
    #   spaces -> optional '+' or '-' -> spaces -> digits -> spaces
    #Spaces are not captured for matching
    #Should be an object of 5 matches

    regex = re.compile(r'^(\d+)(d)(\d+)(?:[\s]*)?(\+|\-)?(?:[\s]*)(\d+)?(?:[\s]*)$')
    regex_matches = re.match(regex, user_dice_roll)

    #Check for correct input format. If its correct, return the match objectself.
    #   If its incorrect, print a message prompting for re-entry
    if regex_matches == None:
        print "Please enter rolls in the format '2d10 + 3'."
    else:
        return regex_matches

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

def create_dice_rolls(quantity_of_dice, number_of_sides):
    rolls = []
    for x in range(quantity_of_dice):
        rolls.append(random.randint(1,number_of_sides))
    return rolls

def print_rolls(rolls):
    for x in rolls:
        print x
    print '---'

def parse_dice_and_modifier(dice_mod_string):
    num_sides, mod_string = dice_mod_string.split()
    num_sides = int(num_sides)
    mod_sign = mod_string[0]
    modifier = mod_string[1]
    modifier = int(modifier)
    return num_sides, mod_sign, modifier

parse_dice_roll(user_input)
