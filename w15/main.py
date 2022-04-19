
# Star Wars Character Generator
# This code is designed to produce a brand new character that can
# be used in rpgs, stories, tabletop games, etc.

from functools import reduce
from operator import getitem
import random
import art
from char_description import char_inputs

print(art.intro)

print("Welcome to the Star Wars Character Generator!\n"
      "This generator will randomly create a unique character"
      " that can be used for table-top games, rpgs, and other games!\n")


def creator():
    def name():
        """Returns a first and last name for the player based on random
        letters chosen from inputs."""
        name = input("What is your first name?\n").lower()
        city = input("What city do you live in?\n").lower()
        color = input("What is your favorite color?\n").lower()
        name_letters = list(name + city + color)

        first_name = ""
        last_name = ""
        for char in range(5):
            first_name += random.choice(name_letters)
            last_name += random.choice(name_letters)
        name = first_name + " " + last_name
        return name

    def planet(region):
        """Returns the player's origin planet based on their region choice."""
        if region == "inner":
            return random.choice(char_inputs["Inner Planets"])
        elif region == "mid":
            return random.choice(char_inputs["Mid Planets"])
        elif region == "outer":
            return random.choice(char_inputs["Outer Planets"])
        elif region == "unknown":
            return random.choice(char_inputs["Unknown Planets"])

    def species(region):
        """Returns the player's species based on their region choice."""
        if region == "inner":
            return random.choice(char_inputs["Inner Species"])
        elif region == "mid":
            return random.choice(char_inputs["Mid Species"])
        elif region == "outer":
            return random.choice(char_inputs["Outer Species"])
        elif region == "unknown":
            return random.choice(char_inputs["Unknown Species"])

    def current_sit():
        """Returns the player's current situation based on their allegiance"""
        correct_alliance = False
        while not correct_alliance:
            allegiance = int(input("Who do you swear allegiance to? "
                                   "Type 1 for Rebellion, 2 for Empire, "
                                   "or 3 For Neither.\n"))
            if allegiance == 1:
                return random.choice(char_inputs["Rebellion"])
            elif allegiance == 2:
                return random.choice(char_inputs["Empire"])
            elif allegiance == 3:
                return random.choice(char_inputs["Neither"])
            else:
                print(art.c3po)

                print("R2, I believe there was an error for allegiance choice!"
                      " We're doomed! Please try again.\n")

    def appearance():
        """Returns the player's physical appearance based on inputted age."""
        correct_age = False
        while not correct_age:
            age = int(input("What age would you like your character to be? "
                            "Please type a number above 15.\n"))
            if age >= 50:
                return random.choice(char_inputs["Old"])
            elif age >= 30 and age < 50:
                return random.choice(char_inputs["Mid"])
            elif age >= 15 and age < 30:
                return random.choice(char_inputs["Young"])
            else:
                print(art.c3po)

                print("R2, I believe there was an error for age!"
                      " We're doomed! Please try again.\n")

    char_name = name()
    region_correct = False
    while not region_correct:
        region = input("What is your favorite region in Star Wars? Type one of"
                       " the following: inner, mid, outer, unknown.\n").lower()
        if (region == "inner" or region == "mid" or region == "outer" or
                region == "unknown"):
            region_correct = True
        else:
            print(art.c3po)

            print("R2, I believe there was an error for age!"
                  " We're doomed! Please try again.\n")

    char_physical = appearance()
    char_job = random.choice(char_inputs["Occupation"])
    char_personality = random.choice(char_inputs["Personality"])
    char_situation = current_sit()

# Final printed outcome:
    print(art.end)

    print(f"You are a {species(region)} named {char_name}.\n"
          f"You have been working as a {char_job} on {planet(region)} "
          f"for some time.\n"
          f"Many would describe you as someone who {char_personality}\n"
          f"{char_physical}\n"
          f"Currently, you are {char_situation}\n")


creator()
while input("Would you like to continue with this character or"
            " make a new character?"
            " Type 'y' to continue or 'n' to restart. ") == "n":
    creator()


# Part 2: Assigning Character Attributes

EASY_LEVEL_MODIFIER = 0
HARD_LEVEL_MODIFIER = -1

attributes = {
    "Strength": {
        "value": 10,
        },
    "Constitution": {
        "value": 10,
        },

    "Dexterity": {
        "value": 10,
        },
    "Intelligence": {
        "value": 10
        },
    "Charisma": {
        "value": 10,
        },
    "Wisdom": {
        "value": 10,
    },
}


def set_difficulty():
    """Returns starting modifier score based on choice of difficulty made."""
    difficulty_complete = False
    while not difficulty_complete:
        level = input("Choose your difficulty: "
                      "type 'easy' or 'hard'. ").lower()
        if level == "easy":
            print(f"Your starting modifier is {EASY_LEVEL_MODIFIER}.")
            return EASY_LEVEL_MODIFIER
        elif level == "hard":
            print(f"Your starting modifier is {HARD_LEVEL_MODIFIER}")
            return HARD_LEVEL_MODIFIER
        else:
            print("ERORR, please choose either easy or hard.")


def user_check(points_spent):
    """Checks if all points are spent. Returns True if user
    accepts point allocation, or restarts add_points() if False."""
    if points_spent == 0:
        print(attributes)
        user_continue = input("Here are your attribute stats."
                              " Would you like to continue"
                              " with these values, or"
                              " would you like to start over?"
                              " Type 'continue' or 'restart'. ")
        if user_continue == "continue":
            return True
        elif user_continue == "restart":
            add_points()


def add_points():
    """Allocates points to the values key in the attributes dictionary
    for each specific attribute."""
    points = 10
    while points > 0:
        for ability in attributes:
            allocation = int(input(f"How many points would you like to"
                                   f" allocate to {ability}? "))
            if points < allocation:
                allocation - allocation
                print("ERROR: You've assigned more points than you have."
                      " Please Try Again.")
            else:
                points -= allocation
                attributes[ability]["value"] += allocation
                if user_check(points):
                    return True
                print(f"You have {points} points remaining.")


def modifier_creator(modifier):
    """Creates a new dictionary key for the modifier, adjusts the modifier
    score depending on the values assigned for each attribute."""
    for key in attributes:
        value = attributes[key]["value"]
        if value <= 10:
            modifier
        elif value == 11:
            modifier += 1
        elif value == 12:
            modifier += 2
        elif value > 12 and value < 15:
            modifier += 3
        elif value >= 15 and value < 17:
            modifier += 4
        else:
            modifier += 5
        attributes[key]["modifier"] = modifier
        modifier = start_modifier


start_modifier = set_difficulty()
add_points()
modifier_creator(start_modifier)

# This final bit of code gives the user their
# attribute score with value and modifier added together.
# This was a test for using the reduce/getitem functions from
# functools and operator.
# Was really challenging, and I do realize there's probably
# an easier way to isolate the value/modifier, but
# I came across this as a solution that gave me some experience
# using a python modules we haven't used in class.
for key in attributes:
    value = "value"
    value_items = [key, value]
    modifier = "modifier"
    modifier_items = [key, modifier]
    value_score = reduce(getitem, value_items, attributes)
    modifier_score = reduce(getitem, modifier_items, attributes)
    total_score = modifier_score + value_score
    print(f"\n Here is your modified attribute score for {key}: {total_score}")

print("\nThank you for using the Star Wars Character generator!")
