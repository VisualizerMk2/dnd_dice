import random
import re

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
        return roll_regex_obj[1], roll_regex_obj[3], roll_regex_obj[4], roll_regex_obj[5]

def create_dice_rolls(quantity_of_dice, number_of_sides):
    rolls = []
    for x in range(quantity_of_dice):
        rolls.append(random.randint(1,number_of_sides))
    return rolls

def print_rolls(rolls):
    for x in rolls:
        print x
    print '---'

user_input = raw_input("Enter your roll: ")

print "User input is: ", user_input

quant_dice, num_sides, modifier_sign, modifier_val = check_input_format(user_input)


quant_dice = int(quant_dice)
num_sides = int(num_sides)
modifier_val = int(modifier_val)

rolls = create_dice_rolls(quant_dice, num_sides)
